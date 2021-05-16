import json
from flask import Response


def _error_response(msg: str, code: int):
    return Response(json.dumps({
        'success': False,
        'error': msg
    }), status=code, mimetype='application/json')


def _success_response(msg: str, code: int):
    return Response(json.dumps({
        'success': True,
        'result': msg
    }), status=code, mimetype='application/json')


def http_ok(msg='OK'):
    code = 200
    return _success_response(msg, code)


def http_bad_request(msg='Bad request'):
    code = 400
    return _error_response(msg, code)


def http_db_error(msg='DB error'):
    code = 503
    return _error_response(msg, code)
