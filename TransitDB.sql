-- Node Tables

CREATE TABLE Station (
  id INT64 NOT NULL,
  name STRING(MAX),
  latitude FLOAT64,
  longitude FLOAT64
) PRIMARY KEY (id);

-- Edge Tables

CREATE TABLE Route (
  id INT64 NOT NULL,
  to_station INT64,
  distance FLOAT64,
  time FLOAT64,
  line STRING(MAX),
  FOREIGN KEY(to_station) REFERENCES Station(id)
) PRIMARY KEY (id, to_station),
INTERLEAVE IN PARENT Station ON DELETE CASCADE;

CREATE TABLE ShortestRoute (
  from_station INT64 NOT NULL,
  to_station INT64 NOT NULL,
  hops INT64 NOT NULL,
  distance FLOAT64,
  time FLOAT64,
  line STRING(MAX),
--  FOREIGN KEY(from_station) REFERENCES Station(id)
) PRIMARY KEY (from_station, to_station);
-- INTERLEAVE IN PARENT Station ON DELETE CASCADE;

-- Create the Graph

CREATE OR REPLACE PROPERTY GRAPH TransitGraph
  NODE TABLES (
    Station,
  )

  EDGE TABLES (
    Route
      SOURCE KEY (id) REFERENCES Station (id)
      DESTINATION KEY (to_station) REFERENCES Station (id)
      LABEL ROUTE
  );


