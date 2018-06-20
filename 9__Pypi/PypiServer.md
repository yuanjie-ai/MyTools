```sh
pip install pypiserver
mkdir ~/packages

pypi-server -p 8080 ~/packages &

pip install --extra-index-url http://localhost:8080 xx
pip install --extra-index-url http://localhost:8080/simple/ xx
pip install --extra-index-url file:///algor/zhouc/packages xx
```
