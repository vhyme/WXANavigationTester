# -*- coding: utf-8 -*-
import os
import re
import sys


debug = False
has_problem = False


def wxa_standard_file_path(path, root='.', base='.'):
    if root == ".":
        root = os.getcwd()
    if base == ".":
        base = os.getcwd()
    if os.path.isfile(base):
        base = os.path.dirname(base)
    while str(path).startswith('..'):
        base = re.compile('[^/]+$').sub(str(''), str(base))
        path = re.compile('^\.\./').sub(str(''), str(path))
    path = os.path.join(base, path)
    path = re.compile('^' + root).sub('', str(path))
    return path


def find_file_by_pattern(pattern='.*', base=".", circle=True):
    re_file = re.compile(pattern)
    if base == ".":
        base = os.getcwd()

    final_file_list = []
    cur_list = os.listdir(base)
    for item in cur_list:
        if item == ".git":
            continue

        full_path = os.path.join(base, item)

        # print full_path
        if os.path.isfile(full_path):
            if re_file.search(full_path):
                final_file_list.append(full_path)
        else:
            final_file_list += find_file_by_pattern(pattern, full_path)

    return final_file_list


def find_js():
    return find_file_by_pattern(pattern='\.js$')


def describe_node(node_step):
    return str((' -> ' if node_step[1] == 0 else ' ~> ') + node_step[0])


def print_path_normal(path):
    if debug:
        print(''.join(list(map(describe_node, path))))


def print_path_too_long(path):
    global has_problem
    has_problem = True
    print(''.join(list(map(describe_node, path))))
    print('\n [!] 跳转栈超过5层。尝试减少其中的部分跳转。\n')


def print_path_circle(path, circle):
    global has_problem
    has_problem = True
    for item in circle:
        path.pop()
    print(''.join(list(map(describe_node, path))) + ' [' + ''.join(list(map(describe_node, circle))) + ']')
    print('\n [!] 跳转栈存在不全是重定向的环。删除其中的某个跳转，或将循环中的所有跳转改为重定向。\n')


def find_path(length, from_node, from_step, graph, cur_path):
    circle_len = 0
    has_circle = False
    circle = []
    for (node, step) in cur_path:
        if has_circle:
            circle_len += step
        if node == from_node:
            has_circle = True
        if has_circle:
            circle += [(node, step)]
    if circle_len > 0:
        print_path_circle(cur_path + [(from_node, from_step)], circle + [(from_node, from_step)])
        return
    elif has_circle:
        print_path_normal(cur_path + [(from_node, from_step)])
        return

    if len(graph[from_node]) == 0:
        if length > 5:
            print_path_too_long(cur_path + [(from_node, from_step)])
            return
        print_path_normal(cur_path + [(from_node, from_step)])
        return
    for (node, step) in graph[from_node]:
        find_path(length + step, node, step, graph, cur_path + [(from_node, from_step)])
    print_path_normal(cur_path + [(from_node, from_step)])


def test_and_show():
    print('微信小程序跳转层数检查工具')
    print('支持 Python 2/3 全版本')
    print('')
    print('Usage: ')
    print('加参数 -d 可显示所有跳转栈遍历结果；')
    print('\'->\' 表示进入一级页面或 redirectTo，\'~>\' 表示 navigateTo。')
    print('')

    if not os.path.exists('app.json'):
        print('错误: 请在含有 app.json 文件的小程序根目录运行此脚本。')
        return

    pages = set()
    graph, ideg = dict(), dict()
    for file_name in find_js():
        content = ''
        for line in open(file_name):
            content += line + '\n'
        result = re.compile('(redirectTo|navigateTo)[\s\r\n]*\([\s\r\n]*\{[\s\r\n]*url[\s\r\n]*:[\s\r\n]*[\'\"]*([^?\"\']+)?')\
                   .findall(content)
        if result:
            def transform_key(path):
                return re.compile('\.js$').sub('', wxa_standard_file_path(path, '.', file_name))

            def transform_value(step_path):
                return (re.compile('\.js$').sub('', wxa_standard_file_path(step_path[1], '.', file_name)),
                        1 if step_path[0] == 'navigateTo' else 0)

            key, value = transform_key(file_name), set(map(transform_value, result))
            pages.add(key)
            graph[key] = value
            if key not in graph:
                graph[key] = {}
            if key not in ideg:
                ideg[key] = 0
            for page, step in value:
                pages.add(page)
                if page not in graph:
                    graph[page] = {}
                if page not in ideg:
                    ideg[page] = 0
                ideg[page] += 1

    for key in ideg:
        if ideg[key] == 0:
            find_path(0, key, 0, graph, [])

    if has_problem:
        print('请修正以上问题后，再次运行本工具进行检查')
    else:
        print('没有发现问题。')

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '-d':
        debug = True
    test_and_show()
