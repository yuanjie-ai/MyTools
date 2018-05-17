```python
# -*- coding: utf-8 -*-
from MyNLP.utils.word_embedding import MyGlove

import jieba
import flask
from flask import Flask, request, url_for, Response
import time
a = time.time()
app = Flask(__name__)
#------------------
glove = MyGlove('/DATA/1_DataCache/FinCorpus/vectors.txt')
#------------------
@app.route("/", methods=["GET"])
def index():
    with app.test_request_context():
        # 生成每个函数监听的url以及该url的参数
        result = {"Get Key Words": {"url": url_for("keywords"),
                                   "params": ["sentence"]}}

        result_body = flask.json.dumps(result, encoding='utf-8')
        return Response(result_body, mimetype="application/json")


@app.route("/glove/keywords", methods=["GET"])
def keywords():
    request_args = request.args

    # 如果没有传入参数，返回提示信息
    if not request_args:
        result = {
            "message": "sentence=__keywords__"
        }
        result_body = flask.json.dumps(result, ensure_ascii=False)
        return Response(result_body, mimetype="application/json")

    # 获取请求参数
    sentence = request_args.get("sentence", "默认文本")

    # 构造返回数据
    result = {
        "Corpus": {
            "sentence": sentence,
        },
        "result": glove.keywords(jieba.lcut(sentence))
    }
    result_body = flask.json.dumps(result, ensure_ascii=False, encoding='utf-8')
    return Response(result_body,  mimetype="application/json")

if __name__ == "__main__":
    app.run(host='10.244.2.3', port=9955)
```
