#!/usr/bin/env python
import frontmatter 
import os 
import traceback 

from wss.src.basic_functions import getEnvironment, getSubpages

from build_index import build_index

def main():
    try: 
        build_index()
    except Exception as inst: 
        print('could not build wss main page')
        print(inst)

if __name__ == '__main__':
    main()

