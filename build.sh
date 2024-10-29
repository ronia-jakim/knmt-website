#!/usr/bin/env bash

rm -rf build

mkdir -p build
# mkdir -p build/content/news
mkdir -p build/stylesheets

mkdir build/books build/info

cp -r assets build 
cp -r content build/content

# sass ./src/stylesheets/colors_fonts.scss ./build/stylesheets/colors_fonts.css
sass ./src/stylesheets/basic-style.scss ./build/stylesheets/basic-style.css
sass ./src/stylesheets/news.scss ./build/stylesheets/news.css
sass ./src/stylesheets/photos.scss ./build/stylesheets/photos.css


if [[ " $* " == *" --github-pages "* ]]; then
  ./src/pytong/build_main.py --github-pages
else
  ./src/pytong/build_main.py 
fi

# python -m flask --app ./src/pytong/build_main.py run --debug
