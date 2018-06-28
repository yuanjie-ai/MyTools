<h1 align = "center">:rocket: Utils :facepunch:</h1>

---

- [MyDecorator][1]

- 脱敏词替换
```python
def repalce_words(s1, s2):
    idx = [chr(i) for i in range(45,123)]
    _s1 = s1.split(' ')
    _s2 = s2.split(' ')
    dic = dict(zip(set(_s1 + _s2), idx))
    _ = lambda s: ' '.join([dic[i] for i in s])
    return _(_s1), _(_s2)
    
repalce_words("L0000 L0001", "L0002 L0003") # ('- .', '/ 0')
```









---
[1]: https://github.com/Jie-Yuan/MyTools/blob/master/2_CommonOperation/2_Decorator/MyDecorator.md
