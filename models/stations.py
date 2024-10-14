#! /usr/bin/env python

from dataclasses import dataclass
import csv

@dataclass
class Station:
    id: int
    name: str
    latitude: float
    longitude: float

    def __init__(self, station):
        self.id = int(station['id'])
        self.name = station['station']
        self.latitude = float(station['latitude'])
        self.longitude = float(station['longitude'])

@dataclass
class Stations:
    list_items: list[Station]

    def __init__(self):
        with open("data/station.csv") as f:
            reader = csv.DictReader(f)
            self.list_items = [Station(row) for row in reader]

@dataclass
class Route:
    id: int
    to_station: int
    distance: float
    time: float

    def __init__(self, route):
        self.id = int(route['from'])
        self.to_station = int(route['to'])
        self.distance = float(route['distance'])
        self.time = float(route['time'])

@dataclass
class Routes:
    list_items: list[Route]

    def __init__(self):
        with open("data/transit_edge.csv") as f:
            reader = csv.DictReader(f)
            self.list_items = [Route(row) for row in reader]
