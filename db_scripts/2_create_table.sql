\connect kenanga_db

CREATE TABLE kenanga_schema.history_monthly
(
    history_date date NOT NULL,
    soybean_oil_future numeric(6, 2) NOT NULL,
    crude_oil_future numeric(6, 2) NOT NULL,
    gas_oil_future numeric(7, 2) NOT NULL,
    crude_palm_oil_fob_spot numeric(8, 2) NOT NULL,
    dollar_to_ringgit numeric(7, 4) NOT NULL,
    oceanic_nino_index numeric(4, 1) NOT NULL,
    palm_oil_inventory numeric(9, 3) NOT NULL,
    dollar_index_spot numeric(7, 3) NOT NULL
)

TABLESPACE pg_default;

ALTER TABLE kenanga_schema.history_monthly
    OWNER to postgres;
	
-- Update table 

SET DateStyle TO European;

COPY kenanga_schema.history_monthly(history_date, soybean_oil_future, crude_oil_future, gas_oil_future, 
			   crude_palm_oil_fob_spot, dollar_to_ringgit, oceanic_nino_index, 
			   palm_oil_inventory, dollar_index_spot)
			  FROM '/var/lib/postgresql/csv/Assignment-monthlyexcerpt_upd.csv' DELIMITER ',' CSV HEADER;
