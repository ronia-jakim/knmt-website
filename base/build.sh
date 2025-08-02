#!/usr/bin/env bash

rm -rf base/build

mkdir base/build
cp -r content/ base/build/content/

python base/src/main.py


