参考文章:

https://python3-cookbook.readthedocs.io/zh_CN/latest/c08/p07_calling_method_on_parent_class.html

https://docs.python.org/zh-cn/3/library/functions.html#super

`class super([type[, object-or-type]])`

返回一个代理对象, 会将方法调用委托给 type 的父类或者兄弟类.

`object-or-type`决定了 `__mro__` 的搜索路径, 会从路径链之后的类型开始搜索

​	例如: object-or-type的 `__mro__` 为 `D->B->C->A->object`, 如果type是B, 那么 super() 的搜索路径是 `C-A-Object`



难点在于多重继承的时候应该怎么应用?

​	

