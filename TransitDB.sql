-- Node Tables

CREATE TABLE Station (
  id INT64 NOT NULL,
  name STRING(MAX),
  latitude FLOAT64,
  longitude FLOAT64,
  name_Tokens TOKENLIST AS (TOKENIZE_NGRAMS(name, ngram_size_min=>3, ngram_size_max=>4)) HIDDEN,
) PRIMARY KEY (id);

CREATE TABLE Person (
  id INT64 NOT NULL,
  firstname STRING(MAX),
  lastname STRING(MAX),
  email STRING(MAX),
  phone STRING(MAX),
  age INT64,
) PRIMARY KEY (id);

CREATE TABLE ShortestRoute (
  from_station INT64 NOT NULL,
  to_station INT64 NOT NULL,
  hops INT64 NOT NULL,
  distance FLOAT64,
  time FLOAT64,
  line STRING(MAX),
) PRIMARY KEY (from_station, to_station);

CREATE TABLE Address (
  id INT64 NOT NULL,
  address STRING(MAX),
  address_Tokens TOKENLIST AS (TOKENIZE_NGRAMS(address, ngram_size_min=>3, ngram_size_max=>4)) HIDDEN,
) PRIMARY KEY (id);

-- Create the Search Indexes
CREATE SEARCH INDEX StationIndex ON Station(name_Tokens);
CREATE SEARCH INDEX StreetIndex ON Address(address_Tokens);

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

CREATE TABLE HasInhabitant (
  id INT64 NOT NULL,
  to_person INT64,
  FOREIGN KEY(to_person) REFERENCES Person(id)
) PRIMARY KEY (id, to_person),
INTERLEAVE IN PARENT Person ON DELETE CASCADE;
  

-- Create the Graph

CREATE OR REPLACE PROPERTY GRAPH TransitGraph
  NODE TABLES (
    Station,
    Address,
    Person,
  )

  EDGE TABLES (
    HasInhabitant
      SOURCE KEY (id) REFERENCES Address (id)
      DESTINATION KEY (to_person) REFERENCES Person (id)
      LABEL HAS_INHABITANT,
    Route
      SOURCE KEY (id) REFERENCES Station (id)
      DESTINATION KEY (to_station) REFERENCES Station (id)
      LABEL ROUTE
  );
