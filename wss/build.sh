#!/usr/bin/env bash
rm -rf build/wss
mkdir build/wss/

PYTHONPATH=. python wss/src/main.py
echo "wss"

for dir in wss/subpages/*/; do
  echo $dir
  [ -d "$dir" ] && [ -x "$dir/build.sh" ] && "$dir/build.sh"
done
