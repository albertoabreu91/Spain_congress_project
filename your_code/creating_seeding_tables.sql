
-- Creating provinces table
CREATE TABLE provinces (
	prov_id INT AUTO_INCREMENT,
	prov_name VARCHAR(30),
	PRIMARY KEY (prov_id)
);


-- Seeding the provinces table

INSERT INTO provinces (prov_name)
VALUES 
('Barcelona'),
('Lleida'),
('Girona'),
('Tarragona');

-- Left Join with cat_mun as left table with spain_mun

SELECT *
FROM cat_mun
LEFT JOIN spain_mun
USING(RegionName);

