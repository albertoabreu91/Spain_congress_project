-- GETTING TO KNOW OUR DATA.

-- Creating province table
CREATE TABLE province (
	prov_id INT,
	prov_name VARCHAR(30),
	PRIMARY KEY (prov_id)
);

-- Inserting data into our province table
INSERT INTO province (prov_id, prov_name)
VALUES 
(8,'Barcelona'),
(25,'Lleida'),
(43,'Girona'),
(17,'Tarragona');

-- Adding the primary key
ALTER TABLE MUN_ID_TABLE
ADD PRIMARY KEY(muni_id);

-- Adding the foreign key
ALTER TABLE MUN_ID_TABLE
ADD FOREIGN KEY(prov_id) REFERENCES province(prov_id);

-- Adding foreign keys
ALTER TABLE MUN_POL_AGE
ADD FOREIGN KEY(muni_id) REFERENCES MUN_ID_TABLE(muni_id),
ADD FOREIGN KEY(prov_id) REFERENCES province(prov_id);





