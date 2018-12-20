#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
__title__ = '__main__'
__author__ = 'JieYuan'
__mtime__ = '18-11-23'
"""

from flask import Flask
from flask_restful import Resource, Api
from flask_restful.reqparse import RequestParser


class Model(object):
    parser = RequestParser()
    parser.add_argument("id_", type=str, default='xxxxxxxxxxxx', required=True)
    parser.add_argument("id", type=str,  # type=lambda x: x.split(',')
                        location="args", required=True, case_sensitive=False, help=None)
    routing = '/xx'

    def __init__(self, *args, **kwargs):
        pass

    def predict(self, *args, **kwargs):
        return kwargs


    def preprocessing(self, *args, **kwargs):
        pass



class Restful(Resource, Model):

    def __init__(self):
        super().__init__()

    def get(self):
        request = self.parser.parse_args(strict=True)
        return self.predict(**request)

    @classmethod
    def app(cls):
        app = Flask(__name__)
        api = Api(app)
        api.add_resource(cls, cls.routing)
        app.run(debug=True)

if __name__ == '__main__':
    Restful.app()
