用于实现interface的方法校验功能，如果子类不具备@abstractmethod的方法，那么就会抛出异常。
```python
import abc

class AbstractClass(metaclass=abc.ABCMeta):

  @abc.abstractmethod
  def abstractMethod(self):
      return
```
