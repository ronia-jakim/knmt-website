#!/usr/bin/env python
import frontmatter
import os
import traceback

from base.src.basic_functions import getEnvironment, getSubpages


def main():
    env = getEnvironment()

    template = env.get_template('subpages/sign-up/index.html')
    subpages = getSubpages()
    html_cnt = template.render(subpages=subpages)

    try:
        os.makedirs('build/sign-up')
    except Exception as inst:
        print(f'could not create a directory for sign-up page: {inst}')

    try:
        with open("build/sign-up/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to sign-up/index.html: {inst}')

if __name__ == '__main__':
    main()
