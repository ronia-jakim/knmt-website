#!/usr/bin/env bash
rm -rf build
mkdir build

./base/build.sh
./wss/build.sh

mkdir -p build/assets/

# sass assets/stylesheets/basic-style.scss build/assets/stylesheets/basic-style.css
# sass --sourcemap=none assets/stylesheets:build/assets/stylesheets

# for f in assets/stylesheets/*.scss; do
#   sass "$f" "build/assets/stylesheets/$(basename "${f%.scss}.css")"
# done

cp -r assets/stylesheets build/assets

cp -r assets/img build/assets
cp -r assets/fonts build/assets


