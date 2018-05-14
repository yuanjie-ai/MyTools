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
