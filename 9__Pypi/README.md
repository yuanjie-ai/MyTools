<h1 align = "center">:rocket: PypiFlow :facepunch:</h1>

---

```sh

# https://packaging.python.org/tutorials/packaging-projects/#setup-args
# http://python.jobbole.com/82077/
vim setup.py 

pip install setuptools twine wheel -U
python setup.py sdist bdist_wheel && twine upload --repository-url https://test.pypi.org/legacy/ ./dist/*

# 185502882338643188a
python setup.py sdist bdist_wheel && twine upload ./dist/* 
```

