from app.utils.extract_data import get_tax_rate


def test_ordinary_case(monkeypatch, test_app):
    data = {
        'qty': 1,
        'unit_price': 100,
        'code_state': 'CA'
    }

    def select(query, params):
        return [(0.065,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    tax_rate = get_tax_rate(test_app, data)
    assert tax_rate == 0.065
