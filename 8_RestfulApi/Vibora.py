# -*- coding: utf-8 -*-
"""
__title__ = 'vibora_test'
__author__ = 'JieYuan'
__mtime__ = '18-11-6'
"""
import jieba
from vibora.utils import RequestParams
from vibora import Vibora, Response, Request
from vibora.responses import JsonResponse
from urllib import parse
from vibora.router import RouterStrategy, uuid

app = Vibora()  # Vibora(router_strategy=RouterStrategy.STRICT)

from poetry.poetry_gen import PoetryGen
p = PoetryGen(False)

# @app.route('/aa/<corpus>', methods=['GET'])  # @app.route(re.compile('/product/(?P<product_id>[0-9]+)'))
# async def page(corpus: str):
#     corpus = parse.unquote(corpus)  # parse.unquote(parse.quote('中文'))
#     _ = jieba.lcut(corpus)
#     return JsonResponse({'中国': _})


# @app.route('/', methods=['POST'])
# async def home(request: Request):
#     uploaded_files = []
#     for file in (await request.files):
#         print(file)
#         file.save('/tmp/' + str(uuid.uuid4()))
#         print(f'Received uploaded file: {file.filename}')
#         uploaded_files.append(file.filename)
#     return JsonResponse(uploaded_files)

# @app.route('/')
# async def home(request: Request):
#     print(dict(request.args))
#     return Response(f"Name: {request.args['name']}")


@app.route('/poetry/<corpus>', methods=['GET'])  # @app.route(re.compile('/product/(?P<product_id>[0-9]+)'))
async def page(corpus: str):
    corpus = parse.unquote(corpus)  # parse.unquote(parse.quote('中文'))
    _ = p.gen(start_words=corpus).split()
    return JsonResponse({'中国': _})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, workers=4, debug=True)
