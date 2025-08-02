#!/usr/bin/env python

import frontmatter

from jinja2 import Environment, FileSystemLoader

from build_index import build_index

def main():
    subpages = []
    try:
        with open('base/subpages/list.md') as f:
            subpages = frontmatter.load(f).metadata['subpages']
    except Exception as inst:
        print('could not find subpages of base')
        print(inst)

    try:
        environment = Environment(loader = FileSystemLoader('base/'))
        build_index(environment, subpages)

    except Exception as inst:
        print('could not build main page')
        print(inst)


if __name__ == '__main__':
    main()
