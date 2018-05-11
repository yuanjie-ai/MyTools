- exec 被当成一个函数 ，可以通过以下的方法来进行将字符串变成变量的名字进行赋值

```python
x='myVar'
exec("%s = %s" % (x, [1,2,3]))
print(myVar) # [1, 2, 3]
```

