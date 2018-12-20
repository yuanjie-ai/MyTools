# Api

#### `from flask_restful.reqparse import RequestParser`

- `RequestParser().add_argument(...)`
  - type=int
  - required=True
  - case_sensitive=True
  - operators=('=',)
  - default=None
  - help=None
  - location
    - json: u'the JSON body'
    - form: u'the post body'
    - args: u'the query string'
    - values: u'the post body or the query string'
    - headers: u'the HTTP headers'
    - cookies: u'the request\'s cookies'
    - files: u'an uploaded file'

