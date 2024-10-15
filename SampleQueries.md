
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
