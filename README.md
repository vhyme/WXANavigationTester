# WXANavigationTester
微信小程序跳转层数检测工具

## 配置需求
Python 2/3 通用

## 用法
将 testNavigation.py 拷贝到有 `app.json` 的微信小程序根目录并运行即可。

## 原理
使用了深度优先遍历，向下遍历时会检查有无环路，回溯时会检测这条路径的长度；有环路或长度超过5时会进行输出。

## 示例输出
```python
python testNavigate.py -d
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