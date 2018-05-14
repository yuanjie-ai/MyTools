```python
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)   # 制作翻译表
 
str = "this is string example....wow!!!"
print(str.translate(trantab)) # th3s 3s str3ng 2x1mpl2....w4w!!!
```
