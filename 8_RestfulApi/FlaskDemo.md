```python
# -*- coding: utf-8 -*-
"""
__title__ = 'main'
__author__ = 'JieYuan'
__mtime__ = '2018/5/18'
"""

import flask
from flask import Flask, Response, request, url_for

# -------------------------------
import jieba
from MyNLP.utils.word_embedding import MyGlove

glove = MyGlove('/DATA/1_DataCache/FinCorpus/vectors.txt')
# -------------------------------

app = Flask(__name__)


@app.route("/keywords/glove", methods=["GET"])
def keywords():
    values = request.args.get("var", "default_values")  # 获取请求参数/keywords/glove?var=default_values
    result = {
        "values": values,
        "result": '无处理逻辑',
        "苏宁金融关键词": glove.keywords(jieba.lcut(values))
    }
    return get_result(result)


@app.route("/cut/jieba", methods=["GET"])
def cut():
    values = request.args.get("var", "default_values")
    result = {
        "values": values,
        "result": '无处理逻辑',
        "苏宁金融关键词": ' '.join(jieba.lcut(values))
    }
    return get_result(result)


# Api说明书
@app.route("/", methods=["GET"])
def index():
    with app.test_request_context():
        # 生成每个函数监听的url以及该url的参数（不要也行）
        result = {
            "Api说明书":
                {
                    "url_1": url_for("keywords") + "?var=default_values",
                    "url_2": url_for("cut") + "?var=default_values"
                }
        }

        result_body = flask.json.dumps(result, encoding='utf-8')
        return Response(result_body, mimetype="application/json")


def get_result(result):
    """
    :param result: 构造返回数据
    """
    result_body = flask.json.dumps(result, ensure_ascii=False, encoding='utf-8')
    return Response(result_body, mimetype="application/json")


if __name__ == "__main__":
    app.config['JSON_AS_ASCII'] = False
    app.run(host='10.244.2.3', port=9955)

```
