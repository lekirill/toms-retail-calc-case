-- discount reference:

CREATE SEQUENCE IF NOT EXISTS public.discount_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE TABLE IF NOT EXISTS public.discount (
	id                      bigint NOT NULL DEFAULT nextval('public.discount_seq'),
	min_price               float NOT NULL,
	max_price               float NOT NULL,
	rate                    float NOT NULL,
	created_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	updated_at              timestamp NULL,
	CONSTRAINT discount_pk PRIMARY KEY (id)
);

INSERT INTO public.discount(min_price, max_price, rate)
VALUES
       (1000, 4999.9999, 0.03),
       (5000, 6999.9999, 0.05),
       (7000, 9999.9999, 0.07),
       (10000, 49999.9999, 0.10),
       (50000, 'Infinity', 0.15);


-- tax rates:

CREATE SEQUENCE IF NOT EXISTS public.tax_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE TABLE IF NOT EXISTS public.tax (
	id                      bigint NOT NULL DEFAULT nextval('public.tax_seq'),
    state_code              text NOT NULL,
	rate                    float NOT NULL,
	created_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	updated_at              timestamp NULL,
	CONSTRAINT tax_pk PRIMARY KEY (id)
);

INSERT INTO public.tax(state_code, rate)
VALUES
       ('UT', 0.0685),
       ('NV', 0.0800),
       ('TX', 0.0625),
       ('AL', 0.0400),
       ('CA', 0.0825);


-- calculations history:

CREATE SEQUENCE IF NOT EXISTS public.calculation_seq
    INCREMENT 1
    START 1
    MINVALUE 1
    MAXVALUE 9223372036854775807
    CACHE 1;

CREATE TABLE IF NOT EXISTS public.calculation (
	id                      bigint NOT NULL DEFAULT nextval('public.calculation_seq'),
	goods_qty               bigint NOT NULL,
	unit_price              bigint NOT NULL,
    state_code              text NOT NULL,
	total_price             float NOT NULL,
	discount_rate           float NOT NULL DEFAULT 0,
    discounted_price        float NOT NULL,
	tax_rate                float NOT NULL,
	final_price             float NOT NULL,
	created_at              timestamp NOT NULL DEFAULT now()::timestamp without time zone,
	updated_at              timestamp NULL,
	CONSTRAINT calculation_pk PRIMARY KEY (id)
);

