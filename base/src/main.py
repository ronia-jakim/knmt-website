#!/usr/bin/env python

import frontmatter
import markdown


from jinja2 import Environment, FileSystemLoader


def main():
    subpages = []
    try:

    except Exception as inst:
        print('could not find subpages of base')
        print(inst)


if __name__ == '__main__':
    main()
