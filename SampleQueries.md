```sql
GRAPH TransitGraph 
MATCH(src:Station{name: "Bond Street"})-[r:ROUTE]->{1,7}(dest:Station{name: "Westminster"})
RETURN src.name AS Start, ARRAY_LENGTH(r) AS stops, dest.name AS Dest 
ORDER BY stops LIMIT 4




```
