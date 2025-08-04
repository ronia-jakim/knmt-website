#!/usr/bin/env python
import frontmatter
import os
import traceback

from base.src.basic_functions import getEnvironment, getSubpages

BOOKS_FILE_PATH = 'content/book_list.md'

def main():
    env = getEnvironment()

    template = env.get_template('subpages/books/index.html')
    html_cnt = ''
    subpages = getSubpages()
    try:
        with open(BOOKS_FILE_PATH) as f:
            info = frontmatter.load(f)
            html_cnt = template.render(book_lst = info.metadata['books'], subpages=subpages)
    except Exception:
        print('could not read book_lst')
        traceback.print_exc()

    try:
        os.makedirs('build/books')
    except Exception as inst:
        print(f'could not create a directory for books page: {inst}')

    try:
        with open("build/books/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to books/index.html: {inst}')

if __name__ == '__main__':
    main()
