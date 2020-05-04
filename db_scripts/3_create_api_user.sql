CREATE USER api_user with PASSWORD '!qazZaq1';

\connect kenanga_db

GRANT CONNECT ON DATABASE kenanga_db TO api_user;
GRANT USAGE ON SCHEMA kenanga_schema to api_user;
GRANT SELECT ON kenanga_schema.history_monthly TO api_user;
