#!/usr/bin/env bash
cp -r content/ build/content/

PYTHONPATH=. python base/src/main.py
echo "base"

for dir in base/subpages/*/; do
  if [ "$(basename "$dir")" = "template" ]; then
    continue
  fi
  echo $dir
  [ -d "$dir" ] && [ -x "$dir/build.sh" ] && "$dir/build.sh"
done
