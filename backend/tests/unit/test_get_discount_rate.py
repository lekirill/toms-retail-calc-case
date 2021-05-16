from app.utils.extract_data import get_discount_rate


def test_no_discount(monkeypatch, test_app):
    data = {
        'qty': 1,
        'unit_price': 100,
        'code_state': 'CA'
    }

    def select(query, params):
        return None

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    discount_rate = get_discount_rate(test_app, data)
    assert discount_rate == 0


def test_with_discount(monkeypatch, test_app):
    data = {
        'qty': 1,
        'unit_price': 100,
        'code_state': 'CA'
    }

    def select(query, params):
        return [(0.07,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    discount_rate = get_discount_rate(test_app, data)
    assert discount_rate == 0.07
