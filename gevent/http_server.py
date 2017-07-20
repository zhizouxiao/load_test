#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gevent.wsgi import WSGIServer


def application(environ, start_response):
    status = '200 OK'
    body = '<p>Hello World</p>'

    headers = [
        ('Content-Type', 'text/html')
    ]

    start_response(status, headers)
    return [body]


print "the server is started, please access: http://127.0.0.1:8080"

WSGIServer(('', 8080), application).serve_forever()
