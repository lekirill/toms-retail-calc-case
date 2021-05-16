def get_tax_rate(app, data):
    sql_result = app.db.select(
        """
        SELECT rate
        FROM public.tax
        WHERE state_code = %(state_code)s
        """, data
    )
    tax_rate = sql_result[0][0]
    return tax_rate


def get_discount_rate(app, data):
    sql_result = app.db.select(
        """
        SELECT rate
        FROM public.discount
        WHERE max_price >= %(total_price)s and min_price <= %(total_price)s
        """, data
    )
    discount_rate = sql_result[0][0] if sql_result else 0
    return discount_rate
