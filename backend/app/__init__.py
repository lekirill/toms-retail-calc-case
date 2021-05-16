import logging
from flask import Flask, request
from flask_cors import CORS

from app.utils.http_responses import http_ok
from app.utils.decorators import validate_json
from app.utils.extract_data import get_tax_rate, get_discount_rate
from app.utils.insert_data import save_calculated_data
from app.schema.calculate import CalculateSchema

app = Flask(__name__)
logger = logging.getLogger('waitress')

CORS(app)


@app.route('/calculate', methods=['POST'])
@validate_json(CalculateSchema)
def calculations():
    data = request.get_json()
    data = make_calculations(app, data)
    logger.info(data)
    save_calculated_data(app, data)
    return http_ok(data)


@app.route('/ping', methods=['GET'])
def ping():
    return http_ok()


def make_calculations(app, data):
    data['total_price'] = data['qty'] * data['unit_price']
    data['discount_rate'] = get_discount_rate(app, data)
    data['discounted_price'] = data['total_price'] * (1 - data['discount_rate'])
    data['tax_rate'] = get_tax_rate(app, data)
    data['final_price'] = data['discounted_price'] * (1 + data['tax_rate'])
    return data
