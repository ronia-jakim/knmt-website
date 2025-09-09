#!/usr/bin/env bash
rm -rf build
mkdir build

./base/build.sh
./wss/build.sh

mkdir -p build/assets/stylesheets/

# sass assets/stylesheets/basic-style.scss build/assets/stylesheets/basic-style.css
sass assets/stylesheets:build/assets/stylesheets

cp -r assets/img build/assets
cp -r assets/fonts build/assets


