#!/usr/bin/env python

import frontmatter 
import markdown

from jinja2 import Environment, FileSystemLoader
from sys import argv

import datetime

# setting up jinja with template directory
environment = Environment(loader=FileSystemLoader("src/templates/"))

import build_post 
import build_index 
import build_info 
import build_photos 
import build_books
import build_calendar

news_metadata = []

try:
    news_metadata = build_post.build_post_pages(environment)
except:
    print("error building post pages")
try:
    build_index.build_index_pages(environment, news_metadata)
except:
    print("error building main page")
try:
    build_info.build_information(environment)
except:
    print("error building information page")

try:
    build_photos.build_main_photos(environment)
except:
    print("error building photo pages")

try:
    build_books.build_book_list(environment)
except:
    print("error building book list")

try:
    build_calendar.build_conf(environment)
except:
    print("error building event page")
