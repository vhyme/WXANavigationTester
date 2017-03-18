# WXANavigationTester
微信小程序跳转层数检测工具

## 配置需求
- 该脚本采用Python3编写，理论上兼容Python2
- 无需任何依赖包

## 用法
将 testNavigation.py 拷贝到有 `app.json` 的微信小程序根目录并运行即可。另外具有调试参数 `-d` 可以完整展示整个遍历过程。

## 原理
该脚本先利用文件系统操作，列出当前小程序目录下所有的 `navigateTo` 跳转和 `redirectTo` 重定向；然后采用带权有向图结构，按照跳转权为1、重定向权为0，作出相应的出边表，然后从每个入度为0的节点开始，对这个图结构采用深度优先遍历，查找长度超过5的路径以及长度不为0的环。

## 示例输出
```javascript
$ python testNavigate.py
微信小程序跳转层数检查工具
支持 Python 2/3 全版本

Usage:
加参数 -d 可显示所有跳转栈遍历结果；
'->' 表示进入一级页面或 redirectTo，'~>' 表示 navigateTo。

 -> /pages/my/my [ ~> /pages/postDetail/postDetail ~> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail]
 [!] 跳转栈存在不全是重定向的环。删除其中的某个跳转，或将循环中的所有跳转改为重定向。

 -> /pages/circle/circle [ ~> /pages/postDetail/postDetail ~> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail]
 [!] 跳转栈存在不全是重定向的环。删除其中的某个跳转，或将循环中的所有跳转改为重定向。

请修正以上问题后，再次运行本工具进行检查
```
```javascript
$ python testNavigate.py -d
微信小程序跳转层数检查工具
支持 Python 2/3 全版本

Usage:
加参数 -d 可显示所有跳转栈遍历结果；
'->' 表示进入一级页面或 redirectTo，'~>' 表示 navigateTo。

 -> /pages/index/index ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/index/index ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/index/index ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/index/index ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/index/index ~> /pages/masterDetail/masterDetail
 -> /pages/index/index ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/index/index ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/index/index ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/index/index ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/index/index ~> /pages/courseDetail/courseDetail
 -> /pages/index/index ~> /pages/myOrder/myOrder ~> /pages/orderDetail/orderDetail
 -> /pages/index/index ~> /pages/myOrder/myOrder
 -> /pages/index/index ~> /pages/allMaster/allMaster ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/index/index ~> /pages/allMaster/allMaster ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/index/index ~> /pages/allMaster/allMaster ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/index/index ~> /pages/allMaster/allMaster ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/index/index ~> /pages/allMaster/allMaster ~> /pages/masterDetail/masterDetail
 -> /pages/index/index ~> /pages/allMaster/allMaster
 -> /pages/index/index ~> /pages/masterApply/masterApply
 -> /pages/index/index ~> /pages/allCourse/allCourse ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/index/index ~> /pages/allCourse/allCourse ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/index/index ~> /pages/allCourse/allCourse ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/index/index ~> /pages/allCourse/allCourse ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/index/index ~> /pages/allCourse/allCourse ~> /pages/courseDetail/courseDetail
 -> /pages/index/index ~> /pages/allCourse/allCourse
 -> /pages/index/index
 -> /pages/my/my ~> /pages/myOrder/myOrder ~> /pages/orderDetail/orderDetail
 -> /pages/my/my ~> /pages/myOrder/myOrder
 -> /pages/my/my ~> /pages/myInfo/myInfo ~> /pages/editInfo/editInfo
 -> /pages/my/my ~> /pages/myInfo/myInfo
 -> /pages/my/my ~> /pages/masterApply/masterApply
 -> /pages/my/my ~> /pages/postDetail/postDetail ~> /pages/publish/publish
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/publish/publish
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail
 -> /pages/my/my ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay
 -> /pages/my/my ~> /pages/postDetail/postDetail
 -> /pages/my/my ~> /pages/myFollowee/myFollowee
 -> /pages/my/my
 -> /pages/circle/circle ~> /pages/publish/publish
 -> /pages/circle/circle ~> /pages/postDetail/postDetail ~> /pages/publish/publish
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/publish/publish
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail
 -> /pages/circle/circle ~> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay
 -> /pages/circle/circle ~> /pages/postDetail/postDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/masterDetail/masterDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail ~> /pages/publish/publish
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail -> /pages/masterDisplay/masterDisplay
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay -> /pages/postDetail/postDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/publish/publish
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply -> /pages/orderDetail/orderDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail ~> /pages/courseApply/courseApply
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail -> /pages/courseDetail/courseDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail -> /pages/masterDetail/masterDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay ~> /pages/courseDetail/courseDetail
 -> /pages/circle/circle ~> /pages/masterDisplay/masterDisplay
 -> /pages/circle/circle
没有发现问题。
```
