#!/usr/bin/env python
import frontmatter
import os
import traceback

from base.src.basic_functions import getEnvironment, getSubpages

INFORMATION_FILE_PATH = 'content/info.md'

def main():
    env = getEnvironment()

    template = env.get_template('subpages/info/index.html')
    html_cnt = ''
    subpages = getSubpages()
    try:
        with open(INFORMATION_FILE_PATH) as f:
            info = frontmatter.load(f)
            html_cnt = template.render(p = info, subpages=subpages)
    except Exception:
        print('could not read info')
        traceback.print_exc()

    try:
        os.makedirs('build/info')
    except Exception as inst:
        print(f'could not create a directory for info page: {inst}')

    try:
        with open("build/info/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to info/index.html: {inst}')

if __name__ == '__main__':
    main()
