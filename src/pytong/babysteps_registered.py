#!/usr/bin/env python

import csv

online = []
offline = []

with open('./src/pytong/babysteps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader: 
        name = row['First Name']
        surname = row['Last Name']
        affiliation = row['Affiliation']
        participant_info = {
        "name": name, 
        "surname": surname, 
        "affiliation": affiliation
        }
        if row['Please select the type of participation in the conference:'] == "Onsite":
            offline.append(participant_info)
        else:
            online.append(participant_info)


from jinja2 import Environment, FileSystemLoader

environment = Environment(loader=FileSystemLoader("src/templates/babysteps"))
template = environment.get_template("base.html")

html_cnt = template.render(online = online, offline = offline)
with open("build/content/babysteps.html", mode="w", encoding="utf-8") as m:
    m.write(html_cnt)

