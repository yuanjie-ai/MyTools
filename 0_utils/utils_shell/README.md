- 首行插入
```sh
sed -i 3i"xx" temp.txt # sed -i 3ixx temp.txt
```

- n行插入 
```sh
sed -i ni"xx" temp.txt
```

- 末尾插入
```sh
echo aaaaa >> temp.txt
```

- 快速删除操作
  - 删除光标之前的全部内容: Ctrl + U
  - 删除光标之后的全部内容: Ctrl + K
  - 撤销之前的删除操作: Ctrl + Y
  - 删除之前的一个参数: Ctrl + W
  
- sudo!!: 对上一行sh授权
