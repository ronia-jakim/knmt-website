#!/usr/bin/env python

import csv

participants = []

with open('./src/pytong/babysteps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: 
        name = row['First Name']
        surname = row['Last Name']
        affiliation = row['Affiliation']
        participants.append({
            "name": name, 
            "surname": surname, 
            "affiliation": affiliation
            })
        print(affiliation)


from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("src/templates/babysteps"))
template = environment.get_template("base.html")

html_cnt = template.render(participants = participants)
with open("build/content/babysteps.html", mode="w", encoding="utf-8") as m:
    m.write(html_cnt)

