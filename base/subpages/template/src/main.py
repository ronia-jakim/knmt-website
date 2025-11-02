#!/usr/bin/env python
# import frontmatter # important for reading *.md files from content/ folder
import os
# import traceback # traceback.print_exc() in except block for detailed debugging

from base.src.basic_functions import getEnvironment, getSubpages

def main():
    env = getEnvironment()

    template = env.get_template('subpages/TEMPLATE/index.html')
    subpages = getSubpages()
    html_cnt = template.render(OTHER TEMPLATE VARIABLES, subpages = subpages)

    try:
        os.makedirs('build/TEMPLATE')
    except Exception as inst:
        print(f'could not create a directory for TEMPLATE page: {inst}')

    try:
        with open("build/TEMPLATE/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to TEMPLATE/index.html: {inst}')

if __name__ == '__main__':
    main()
