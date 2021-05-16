def save_calculated_data(app, data):
    app.db.insert(
        """
        INSERT INTO public.calculation
            (goods_qty, unit_price, state_code, total_price, discounted_price, tax_rate, final_price)
        VALUES(%(qty)s, %(unit_price)s, %(state_code)s, %(total_price)s, %(discounted_price)s, %(tax_rate)s, %(final_price)s);
        """, data
    )
