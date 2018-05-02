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

```python
class Base(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        
     def f(self):
        print(1)

# 可调用父类的所有方法
class A(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)
        self.c = c

A(1,3,4).f()
```
---
继承A类所有参数及方法
```python
class A(object):

    def __init__(self, a, b, c=1, **kwargs):
        self.a = a
        self.b = b
        self.c = c

    def f(self):
        print(self.c)

class MyClass(A):

    def __init__(self, c, **kwargs):
        super().__init__(c=c, **kwargs) # 必须显示调用：c=c
```
---
[1]: http://www.runoob.com/python/python-func-super.html
