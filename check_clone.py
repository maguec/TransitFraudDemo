#!/usr/bin/env python

from google.cloud import spanner
import argparse
from sys import exit
from datetime import datetime

def is_teleport(client, card_id, station_id, timestamp):
    query = """
    SELECT time AS ShortestPossibleTime, latest_ride.timestamp, 
      TIMESTAMP_ADD(latest_ride.timestamp, INTERVAL CAST(time AS INT64) SECOND) AS timeLimit from ShortestRoute
        INNER JOIN (
          SELECT station_id, timestamp from Ride ride where oyster_id={} ORDER BY timestamp DESC LIMIT 1
        ) as latest_ride
      ON ShortestRoute.to_station = latest_ride.station_id 
    WHERE from_station = {};
    """.format(args.card_id, args.station_id)
    with client.snapshot() as snapshot:
        results = snapshot.execute_sql(query)

        for row in results:
            if (row[1]-args.timestamp).total_seconds() < row[0]:
                return True
            else:
                return False

def get_linked_addresses(client, card_id):
    query = """
    GRAPH TransitGraph
        MATCH (o:Oyster{{id: {}}})-[o1:HAS_OYSTER]->(p:Person)<-[o2:HAS_OYSTER]-(q:Oyster)
        RETURN p.id as person_id, p.firstname, p.lastname, q.id as linked_card_id, q.is_suspect as sus
    """.format(card_id)
    with client.snapshot() as snapshot:
        results = snapshot.execute_sql(query)
        for row in results:
            print(row)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(prog='check_clone')
    parser.add_argument('-c', '--card-id', type=int, help='The Oyster Card ID')
    parser.add_argument('-s', '--station-id', type=int, help='The Station ID')
    parser.add_argument('-t', '--timestamp', type=datetime.fromisoformat, help='ISOformat - YYYY-MM-DD:HH:mm:ssZ')
    args = parser.parse_args()
    if any( arg is None for arg in [args.card_id, args.station_id, args.timestamp]):
        parser.print_help()
        exit(1)

    s = spanner.Client()
    instance = s.instance("transit")
    client = instance.database("transitdb")
    if is_teleport(client, args.card_id, args.station_id, args.timestamp):
        print("duplicate card detected for card# {}".format(args.card_id))
        print("investigating graph")
        get_linked_addresses(client, args.card_id)
    else:
        print("Pass for card# {}".format(args.card_id))
