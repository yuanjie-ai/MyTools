- python 模块：

python 的模块就是天然的单例模式，因为模块在第一次导入时，会生成 .pyc 文件，当第二次导入时，就会直接加载 .pyc 文件，而不会再次执行模块代码。因此我们只需把相关的函数和数据定义在一个模块中，就可以获得一个单例对象了。

- `__new__`
```python
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        """
        关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        """
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls, *args, **kwargs)  # cls.instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls.instance
```
