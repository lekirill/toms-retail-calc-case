from app import make_calculations


def test_middle_case(monkeypatch, test_app):
    data = {
        'qty': 1,
        'unit_price': 100,
        'code_state': 'CA'
    }

    def select(query, params):
        if 'tax' in query:
            return [(0.065,)]
        if 'discount' in query:
            return [(0.07,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    data = make_calculations(test_app, data)
    assert data == {'qty': 1, 'unit_price': 100, 'code_state': 'CA', 'total_price': 100, 'discount_rate': 0.07,
                    'discounted_price': 93.0, 'tax_rate': 0.065, 'final_price': 99.045}


def test_no_discount_case(monkeypatch, test_app):
    data = {
        'qty': 1,
        'unit_price': 100,
        'code_state': 'CA'
    }

    def select(query, params):
        if 'tax' in query:
            return [(0.065,)]
        if 'discount' in query:
            return None

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    data = make_calculations(test_app, data)
    assert data == {'qty': 1, 'unit_price': 100, 'code_state': 'CA', 'total_price': 100, 'discount_rate': 0,
                    'discounted_price': 100, 'tax_rate': 0.065, 'final_price': 106.5}
