#!/usr/bin/env bash

mkdir -p build
mkdir -p build/content/news
mkdir -p build/stylesheets

cp -r assets build

sass ./src/stylesheets/colors_fonts.scss ./build/stylesheets/colors_fonts.css
sass ./src/stylesheets/basic-style.scss ./build/stylesheets/basic-style.css
sass ./src/stylesheets/news.scss ./build/stylesheets/news.css

python -m flask --app ./src/pytong/build_main.py run --debug
