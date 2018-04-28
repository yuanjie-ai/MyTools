## [super(): 用于调用父类(超类)的一个方法][1]

```python
class Base(object):
    def __init__(self):
        print 'Base create'
 
class childA(Base):
    def __init__(self):
        print 'creat A ',
        Base.__init__(self)
 
# 使用super()继承时不用显式引用基类
class childB(Base):
    def __init__(self):
        print 'creat B ',
        super(childB, self).__init__()
```

super 的一个最常见用法可以说是在子类中调用父类的初始化方法了，比如：

```
class Base(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
 
class A(Base):
    def __init__(self, a, b, c):
        super(A, self).__init__(a, b)  # Python3 可使用 super().__init__(a, b)
        self.c = c
```
---
[1]: http://www.runoob.com/python/python-func-super.html
