import logging

from marshmallow import Schema, ValidationError
from flask import request
from functools import wraps

from app.utils.http_responses import http_bad_request

logger = logging.getLogger('request_validation')


def validate_json(schema: Schema):
    def decorator(func):
        @wraps(func)
        def wrapper(**kwargs):
            try:
                schema().load(data=request.get_json())
                return func(**kwargs)
            except ValidationError as err:
                logger.info(err.messages)
                return http_bad_request(err.messages)

        return wrapper

    return decorator
