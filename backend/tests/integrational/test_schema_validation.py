def test_success_case(monkeypatch, test_app):
    def select(query, params):
        if 'tax' in query:
            return [(0.065,)]
        if 'discount' in query:
            return [(0.07,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    resp = test_app.post('/calculate',
                         json=({
                             'qty': 5,
                             'unit_price': 100,
                             'state_code': 'TX'
                         })
                         )
    assert resp.status_code == 200


def test_wrong_data(monkeypatch, test_app):
    def select(query, params):
        if 'tax' in query:
            return [(0.065,)]
        if 'discount' in query:
            return [(0.07,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    resp = test_app.post('/calculate',
                         json=({
                             'qty': 5,
                             'unit_price': 100,
                         })
                         )
    assert resp.status_code == 400


def test_wrong_data_format(monkeypatch, test_app):
    def select(query, params):
        if 'tax' in query:
            return [(0.065,)]
        if 'discount' in query:
            return [(0.07,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    resp = test_app.post('/calculate',
                         json=({
                             'qty': 5,
                             'unit_price': 100,
                             'state_code': 100,
                         })
                         )
    assert resp.status_code == 400


def test_wrong_state_code(monkeypatch, test_app):
    def select(query, params):
        if 'tax' in query:
            return [(0.065,)]
        if 'discount' in query:
            return [(0.07,)]

    monkeypatch.setattr(test_app.db, 'select', select, raising=True)
    resp = test_app.post('/calculate',
                         json=({
                             'qty': 5,
                             'unit_price': 100,
                             'state_code': 'NY',
                         })
                         )
    assert resp.status_code == 400
