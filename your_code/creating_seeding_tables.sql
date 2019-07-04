-- GETTING TO KNOW OUR DATA.


-- Creating the province table with the re_id from the spanish political table
CREATE TABLE province (
	re_id INT,
	prov_name VARCHAR(30),
	PRIMARY KEY (re_id)
);

-- Inserting data into our province table
INSERT INTO province (re_id, prov_name)
VALUES 
(8,'Barcelona'),
(25,'Lleida'),
(43,'Girona'),
(17,'Tarragona');





