#!/usr/bin/env bash

rm -rf build

mkdir build
cp -r content/ build/content/

PYTHONPATH=. python base/src/main.py


for dir in base/subpages/*/; do
    [ -d "$dir" ] && [ -x "$dir/build.sh" ] && "$dir/build.sh"
done
