
```bash
gcloud spanner  databases execute-sql transitdb --instance transit --sql='SELECT * from Station WHERE SEARCH_NGRAMS(name_Tokens, "Canar") LIMIT 10'
```

```sql
GRAPH TransitGraph 
MATCH(src:Station{name: "Bond Street"})-[r:ROUTE]->{1,7}(dest:Station{name: "Westminster"})
    RETURN src.name AS Start, ARRAY_LENGTH(r) AS stops, dest.name AS Dest 
    ORDER BY stops LIMIT 4
```

```sql
GRAPH TransitGraph
MATCH(src:Station{name: "Bond Street"})-[r:ROUTE]->{1,7}(dest:Station{name: "Westminster"})
    LET total_distance = SUM(r.distance) 
    LET total_time = SUM(r.time) 
    RETURN src.name AS Start, ARRAY_LENGTH(r) AS stops, total_distance as Distance, total_time as Time,  dest.name AS Dest ORDER BY stops LIMIT 4
```

## Let see if we can catch a cloned card

```sql
SELECT time AS ShortestPossibleTime, latest_ride.timestamp, 
  TIMESTAMP_ADD(latest_ride.timestamp, INTERVAL CAST(time AS INT64) SECOND) AS timeLimit from ShortestRoute
    INNER JOIN (
      SELECT station_id, timestamp from Ride ride where oyster_id=122 ORDER BY timestamp DESC LIMIT 1
    ) as latest_ride
  ON ShortestRoute.to_station = latest_ride.station_id 
WHERE from_station = 100;
```

## Find a bad actor and the other cards associated with them

```bash
./check_clone.py -c 122 -s 100 -t 2024-10-25:22:15:12Z
```
