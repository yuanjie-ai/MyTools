```python
class colors:
    ok = '\033[92m'
    fail = '\033[91m'
    close = '\033[0m'
    
print(colors.ok + '☑' + colors.close, end=' ')
print(colors.fail + '☒' + colors.close, end=' ')
```
