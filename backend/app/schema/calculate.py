from marshmallow import Schema, fields, validate

import settings


class CalculateSchema(Schema):
    qty = fields.Float(required=True)
    unit_price = fields.Float(required=True)
    state_code = fields.Str(required=True, validate=validate.OneOf(settings.STATE_CODES))
