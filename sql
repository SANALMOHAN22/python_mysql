CREATE DATABASE pizza_delivery_db;
USE pizza_delivery_db;

CREATE TABLE customers (
    customer_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    address VARCHAR(200),
    contact_number VARCHAR(15)
);
