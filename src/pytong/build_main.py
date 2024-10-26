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

news_metadata = build_post.build_post_pages(environment)
build_index.build_index_pages(environment, news_metadata)
build_info.build_information(environment)

build_photos.build_main_photos(environment)
