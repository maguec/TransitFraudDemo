#! /usr/bin/env python

from dataclasses import dataclass
import csv

@dataclass
class Person:
    id: int
    firstname: str
    lastname: str
    email: str
    phone: str
    age: int
    def __init__(self, person):
        self.id = int(person['id'])
        self.firstname = person['first_name']
        self.lastname = person['last_name']
        self.email = person['email']
        self.phone = person['phone']
        self.age = person['age']


@dataclass
class Persons:
    list_items: list[Person]

    def __init__(self):
        with open("data/people.csv") as f:
            reader = csv.DictReader(f)
            self.list_items = [Person(row) for row in reader]


@dataclass
class Address:
    id: int
    address: str
    def __init__(self, address):
        self.id = int(address['id'])
        self.address = address['address']


@dataclass
class Addresses:
    list_items: list[Address]

    def __init__(self):
        with open("data/addresses.csv") as f:
            reader = csv.DictReader(f)
            self.list_items = [Address(row) for row in reader]


#@dataclass
#class Routes:
#    list_items: list[Route]
#
#    def __init__(self):
#        with open("data/transit_edge.csv") as f:
#            reader = csv.DictReader(f)
#            self.list_items = [Route(row) for row in reader]
#
