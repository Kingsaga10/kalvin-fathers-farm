CREATE DATABASE kalvin_farm;
USE kalvin_farm;
CREATE TABLE crops (
    id INT AUTO_INCREMENT PRIMARY KEY,
    crop_type VARCHAR(50) NOT NULL,
    yield_amount FLOAT NOT NULL,
    harvest_date DATE NOT NULL
);

CREATE TABLE inputs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    crop_id INT NOT NULL,
    input_type VARCHAR(50) NOT NULL,
    quantity FLOAT NOT NULL,
    usage_date DATE NOT NULL,
    FOREIGN KEY (crop_id) REFERENCES crops(id)
);

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    temperature FLOAT NOT NULL,
    rainfall FLOAT NOT NULL,
    advice TEXT
);
DROP TABLE IF EXISTS weather;
CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    temperature FLOAT NOT NULL,
    rainfall FLOAT NOT NULL,
    advice TEXT
);
SHOW TABLES;
DESCRIBE weather;