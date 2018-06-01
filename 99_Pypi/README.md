<h1 align = "center">:rocket: PypiFlow :facepunch:</h1>

---

```sh
vim setup.py

python setup.py sdist bdist_wheel

twine upload --repository-url https://test.pypi.org/legacy/ ./dist/*

twine upload ./dist/* # 185502882338643188a
```

