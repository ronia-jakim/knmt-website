#!/usr/bin/env bash

mkdir -p build
mkdir -p build/content/news

cp -r assets build

sass src/stylesheets:build/stylesheets

./src/pytong/build_main.py
