#!/usr/bin/env bash

mkdir -p build
mkdir -p build/content/news
mkdir -p build/stylesheets

cp -r assets build

sass ./src/stylesheets:./build/stylesheets

./src/pytong/build_main.py
