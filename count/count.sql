-- Change EPSG
ALTER TABLE observations
ALTER COLUMN geometry TYPE geometry(MultiPolygon,2154) 
USING ST_SetSRID(geometry,2154);

--change EPSG
SELECT UpdateGeometrySRID('public', 'observations', 'geometry', 2154);

-- Test EPSG
SELECT ST_SRID(geom) FROM observations LIMIT 1;


-- spatial index generation
CREATE INDEX idx_obs_geom ON observations USING gist (geom);
CREATE INDEX idx_grid_geom ON grid USING gist (geom);

-- remove invalid data
DELETE FROM observations WHERE nom_latin = 'Odonata';

-- check number of data per species. (i.e. anax imperator)
SELECT COUNT (*) FROM observations WHERE nom_latin = 'Anax imperator';

-- count number of point per species and per grid part (table name to adapt)
SELECT observations.nom_latin, grid.fid, COUNT(observations.n_bd_dep) AS nombre_donnees,  grid.geom   
FROM observations JOIN grid ON ST_Intersects(observations.geom, grid.geom)  
GROUP BY observations.nom_latin, grid.fid, grid.geom
;

-- select list of species (unique name)
select distinct nom_latin from all_observations;

-- select species only
select distinct nom_latin from all_observations WHERE nombre > 0  AND nom_latin NOT IN ('Anisoptera','Odonata','Zygoptera') AND nom_latin NOT LIKE '%ae' AND nom_latin NOT LIKE '%sp.';