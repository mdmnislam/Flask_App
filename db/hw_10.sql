CREATE DATABASE heightWeight;
use heightWeight;

CREATE TABLE IF NOT EXISTS hw10 (
    `Index` INT,
    `Height_Inches` NUMERIC(4, 2),
    `Weight_Pounds` NUMERIC(5, 2)
);
INSERT INTO hw10 VALUES
    (1,60.73,110.90),
    (2,71.50,130.47),
    (3,67.40,153.03),
    (4,68.27,140.30),
    (5,67.70,147.30),
    (6,68.73,123.57),
    (7,63.80,150.60),
    (8,70.03,137.43),
    (9,67.90,113.37),
    (10,66.73,120.67);

