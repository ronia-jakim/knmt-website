#!/usr/bin/env python
import frontmatter

from build_index import build_index

def main():
    try:
        build_index()

    except Exception as inst:
        print('could not build main page')
        print(inst)


if __name__ == '__main__':
    main()
