#!/usr/bin/env python

from models.stations import *
from models.utils import *
from google.cloud import spanner

if __name__ == "__main__":
    s = spanner.Client()
    instance = s.instance("transit")
    client = instance.database("transitdb")
    stations = Stations()
    client.run_in_transaction(writeSpanner, stations)
