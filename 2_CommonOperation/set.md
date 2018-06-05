- 并集
```python
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

set1 | set2
set1.union(set2)
```

- 交集
```python
set1 & set2
set1.intersection(set2)

# 保存在set1
set1.intersection_update(set2)
```


- 差集
```python
set1 - set2
set1.difference(set2)

# 保存在set1
set1.discard(1)
set1.difference_update(set2) 
```
