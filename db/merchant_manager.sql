DROP TABLE IF EXISTS spendings;
DROP TABLE IF EXISTS merchants;

CREATE TABLE merchants(
    id SERIAL PRIMARY KEY, 
    name VARCHAR(255)
);

CREATE TABLE spendings (
    id SERIAL PRIMARY KEY, 
    tag VARCHAR(255),
    amount INT,
    merchant_id INT NOT NULL REFERENCES merchants(id)
);