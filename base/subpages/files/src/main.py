#!/usr/bin/env python
import frontmatter
import os
import traceback

from base.src.basic_functions import getEnvironment, getSubpages

ABSTRACT_FILE_PATH = 'content/files/abstract-template.tex'
PREZENTACJA_A_FILE_PATH = 'content/files/prezentacja-template-A.tex'
PREZENTACJA_B_FILE_PATH = 'content/files/prezentacja-template-B.tex'

def main():
    env = getEnvironment()

    template = env.get_template('subpages/files/index.html')
    html_cnt = ''
    subpages = getSubpages()
    abstract_tex = ''
    prezentacja_A = ''
    prezentacja_B = ''
    try:
        with open(ABSTRACT_FILE_PATH, "r", encoding="utf-8") as f:
            tex_content = f.read()
            abstract_tex = tex_content 

        with open(PREZENTACJA_A_FILE_PATH, "r", encoding="utf-8") as f:
            tex_content = f.read()
            prezentacja_A = tex_content 
        with open(PREZENTACJA_B_FILE_PATH, "r", encoding="utf-8") as f:
            tex_content = f.read()
            prezentacja_B = tex_content 

        html_cnt = template.render(abstract = abstract_tex, prezentacjaA=prezentacja_A, prezentacjaB=prezentacja_B, subpages=subpages)
    except Exception:
        print('could not read info')
        traceback.print_exc()

    try:
        os.makedirs('build/files')
    except Exception as inst:
        print(f'could not create a directory for files page: {inst}')

    try:
        with open("build/files/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
    except Exception as inst:
        print(f'could not write to files/index.html: {inst}')

if __name__ == '__main__':
    main()
