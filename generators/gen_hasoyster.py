#!/usr/bin/env python

from faker import Faker
import csv

fake = Faker()

with open('../data/has_oyster.csv', 'w') as csvfile:
    fieldnames = ['id', 'to_person']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(1000):
        writer.writerow({
            'id': fake.random_int(min=0, max=1349),
            'to_person': i,
        })

