#!/usr/bin/env python
import frontmatter
import os
import traceback

from base.src.basic_functions import getEnvironment, getSubpages

CONFERENCE_LIST_FILE_PATH = 'content/conf_list.md'

def main():
    env = getEnvironment()

    template = env.get_template('subpages/events/index.html')
    html_cnt = ''
    subpages = getSubpages()
    try:
        with open(CONFERENCE_LIST_FILE_PATH) as f:
            conf_list = frontmatter.load(f)
            html_cnt = template.render(conf_list = conf_list.metadata['conferences'], subpages=subpages)
    except Exception:
        print('could not read conference list')
        traceback.print_exc()

    try:
        os.makedirs('build/events')
    except Exception as inst:
        print(f'could not create a directory for events page: {inst}')

    try:
        with open("build/events/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to events/index.html: {inst}')

if __name__ == '__main__':
    main()
