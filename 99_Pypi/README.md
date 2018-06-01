<h1 align = "center">:rocket: PypiFlow :facepunch:</h1>

---

```sh
vim setup.py # https://packaging.python.org/tutorials/packaging-projects/#setup-args

python setup.py sdist bdist_wheel && twine upload --repository-url https://test.pypi.org/legacy/ ./dist/*

# 185502882338643188a
twine upload ./dist/* 
```

