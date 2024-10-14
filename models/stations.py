#! /usr/bin/env python

from dataclasses import dataclass
import csv

@dataclass
class Station:
    station_id: str
    name: str
    latitude: float
    longitude: float

@dataclass
class Stations:
    stations: list[Station]

    def __init__(self):
        with open("data/station.csv") as f:
            reader = csv.reader(f)
            self.stations = [Station(*row) for row in reader]
