```python
import pickle


class Pickle(object):
    """
    https://blog.csdn.net/justin18chan/article/details/78516452
    json，用于字符串 和 python数据类型间进行转换:
        json只能处理简单的数据类型，比如字典，列表等，不支持复杂数据类型，如类等数据类型。
    """

    @staticmethod
    def serialize(obj, file):
        with open(file, 'wb') as f:
            pickle.dump(obj, f)

    @staticmethod
    def deserialize(file):
        with open(file, 'rb') as f:
            return pickle.load(f)

```
