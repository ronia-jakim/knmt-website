#!/usr/bin/env python
import frontmatter
import os
import traceback

from wss.src.basic_functions import getEnvironment, getSubpages

PRGORAMME_FILE_PATH = 'content/wss/programme.md'

def main():
    env = getEnvironment()

    template = env.get_template('subpages/programme/index.html')
    html_cnt = ''
    subpages = getSubpages()
    try:
        with open(PRGORAMME_FILE_PATH) as f:
            info = frontmatter.load(f)
            obiady = info['obiady']
            szatnia = info['szatnia']
            days = info['days']

            html_cnt = template.render(obiady=obiady, szatnia=szatnia, days=days, subpages=subpages)
    except Exception:
        print('could not read wss programme')
        traceback.print_exc()

    try:
        os.makedirs('build/wss/programme')
    except Exception as inst:
        print(f'could not create a directory for wss programme page: {inst}')

    try:
        with open("build/wss/programme/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to programme/index.html: {inst}')

if __name__ == '__main__':
    main()
