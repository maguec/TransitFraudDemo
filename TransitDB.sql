-- Node Tables

CREATE TABLE Stations (
  id INT64 NOT NULL,
  name STRING(MAX),
  latitude FLOAT64,
  longitude FLOAT64
) PRIMARY KEY (id);

-- Edge Tables

CREATE TABLE Routes (
  id INT64 NOT NULL,
  to_station INT64,
  distance FLOAT64,
  time FLOAT64,
  line STRING(MAX),
  FOREIGN KEY(to_station) REFERENCES Stations(id)
) PRIMARY KEY (id, to_station),
INTERLEAVE IN PARENT Stations ON DELETE CASCADE;

-- Create the Graph

CREATE OR REPLACE PROPERTY GRAPH TransitGraph
  NODE TABLES (
    Stations,
  )

  EDGE TABLES (
    Routes
      SOURCE KEY (id) REFERENCES Stations (id)
      DESTINATION KEY (to_station) REFERENCES Stations (id)
      LABEL ROUTE
  );


