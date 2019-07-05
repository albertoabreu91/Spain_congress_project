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

-- ANALISIS---------------------------
-- Which province have the most population
SELECT prov_name, SUM(poblacion) AS total_population
FROM MUN_POL_AGE as m
JOIN province as p
USING(prov_id)
GROUP BY prov_name
ORDER BY total_population DESC;

-- How many municipalities are in each provinces
SELECT prov_name, COUNT(municipalities) as Municipalities_count
FROM MUN_ID_TABLE as m
JOIN province as p
USING(prov_id)
GROUP BY prov_name
ORDER BY Municipalities_count DESC;

-- Whats the mean of the political parties percentage votes per region
SELECT prov_name, AVG(`PP_per`) AS pp_avg
FROM MUN_POL_AGE as m
JOIN province as p
USING(prov_id)
GROUP BY prov_name
ORDER BY pp_avg DESC;

-- Whats the mean of the political parties percentage votes per region
SELECT prov_name, AVG(`PP_per`) AS pp_avg, AVG(`Age_20-34`), AVG(`Age_35-49`), AVG(`Age_50-64`), AVG(`Age_65-79`)
FROM MUN_POL_AGE as m
JOIN province as p
USING(prov_id)
GROUP BY prov_name
ORDER BY pp_avg DESC;

-- Which is the municipe with more catalan parties influence
SELECT municipalities, votes_rate, `ECP_per`, `ERC-CATSÍ_per`, `CDC_per`
FROM MUN_POL_AGE
ORDER BY `ECP_per`;

-- Comparing by catalonian regions the most popular parties in Spain against the most popular party in Catalonia
SELECT p.prov_name AS provinces, AVG(`PP_per`) AS PP_per_avg, AVG(`PSOE_per`) AS PSOE_per_avg , AVG(`Cs_per`) AS Ciudadanos_per_avg, AVG(`ERC-CATSÍ_per`) AS Esquerra_Rep_per_avg
FROM MUN_POL_AGE as m
JOIN province as p
USING(prov_id)
GROUP BY prov_name;

-- Comparing the main catalan parties together with the most important catalan party per average per region
SELECT p.prov_name AS provinces, AVG(`PP_per`) + AVG(`PSOE_per`) + AVG(`Cs_per`) AS sum_popluar_spain_parties_per_avg, AVG(`ERC-CATSÍ_per`) AS Esquerra_Rep_per_avg
FROM MUN_POL_AGE as m
JOIN province as p
USING(prov_id)
GROUP BY prov_name;


