```python
# -*- coding: utf-8 -*-
"""
__title__ = 'decorator'
__author__ = 'JieYuan'
__mtime__ = '2018/5/16'
"""


class MyDecorator(object):
    def __init__(self):
        pass

    class Singleton:
        def __init__(self, cls):
            self.cls = cls
            self.instance = None

        def __call__(self, *args, **kwargs):
            if self.instance is None:
                self.instance = self.cls(*args, **kwargs)
            return self.instance

    def singleton(cls):
        instances = {}

        def getinstance(*args, **kwargs):
            if cls not in instances:
                instances[cls] = cls(*args, **kwargs)
            return instances[cls]

        return getinstance

    class ExecutionTime:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            import time
            t1 = time.time()
            self.func(*args)
            t2 = time.time()
            print("%s run time: %.5f s" % (self.func.__name__, t2 - t1))

    def execution_time(func):
        def wrapper(*args, **kwargs):
            import time
            t1 = time.time()
            func(*args, **kwargs)
            t2 = time.time()
            print("%s run time: %.5f s" % (func.__name__, t2 - t1))

        return wrapper

```
