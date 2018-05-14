<h1 align = "center">:rocket: __func__ :facepunch:</h1>

---
- `__new__`:
对象的创建，是一个静态方法，第一个参数是cls。(想想也是，不可能是self，对象还没创建，哪来的self)

在Python 中存在于类里面的构造方法init()负责将类的实例化，而在init()调用之前，new()决定是否要使用该init()方法，因为new()可以调用其他类的构造方法或者直接返回别的对象来作为本类 的实例。 
- `__init__`:
创建一个类的实例，第一个参数是self。
- `__del__`:
类的析构函数
- `__call__`:
对象可call，注意不是类，是对象。
```python
class MyClass():
    def __call__(self, x):
        return self.__f(x)
    
    def __f(self, x):
        print(x)

MyClass()('xx')
MyClass().__call__('xx')
```
- `__str__`
- `__repr__`: 
__repr__和__str__这两个方法都是用于显示的，__str__是面向用户的，而__repr__面向程序员
```python
class MyClass:
    def __init__(self, name='yuanjie'):
        self.name = name
        
class Repr(MyClass):
    def __repr__(self):
        return '__repr__(%s)' % self.name

class Str(MyClass):
    def __str__(self):
        return '__str__(%s)' % self.name
        
Repr()
print(Repr())

Str()
print(Str())
```


- `__setattr__`
- `__class__`

- `__delattr__`
- `__dict__`
- `__doc__`
- `__format__`
- `__getattribute__`
- `__hash__`
- `__module__`

- `__reduce__`
- `__reduce_ex__`

- `__setattr__`
- `__sizeof__`

- `__subclasshook__`
- `__weakref__`
