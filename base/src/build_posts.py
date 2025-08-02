import frontmatter 
import markdown

from jinja2 import Environment, FileSystemLoader

import os
import datetime

CONTENT_DIRECTORY = 'content/news/'
TARGET_PATH = 'build/content/news/'

DEFAULT_IMAGE = '/assets/img/referat_preview.jpg'

def build_post_pages (env, subpages):
    post_list = os.listdir(CONTENT_DIRECTORY)
    news_metadata = []

    template = env.get_template("post.html")
    
    for p in post_list:
        with open(CONTENT_DIRECTORY + p + '/info.md') as p_file:
            post = frontmatter.load(p_file)

        p_info = post.metadata
        
        try:
            p_info['content'] = markdown.markdown(post.content)
        except Exception as inst:
            print("failed to make post page: " + p)
            print(inst)

        try:
            p_info['date'] = datetime.datetime.strptime(str(p_info['date']), '%Y.%m.%d').date()
        except Exception as inst:
            print("failed to convert date for post: " + p)
            print(inst)
    
        if 'preview_image' not in p_info: 
            p_info['preview_image'] = DEFAULT_IMAGE 
        else: 
            p_info['preview_image'] = '/' + CONTENT_DIRECTORY + p + "/" + str(p_info['preview_image'])

        if 'description' not in p_info:
            p_info['description'] = post.content[:100]+"..."

        p_info['path'] = CONTENT_DIRECTORY + p 

        try:
            html_cnt = template.render(f = p_info, subpages = subpages)
            with open(TARGET_PATH + p + "/index.html", mode="w", encoding="utf-8") as m:
                m.write(html_cnt)
        except Exception as inst:
            print("failed to write on html file for post: " + p)
            print(inst)

    
        news_metadata.append(p_info)

    news_metadata = sorted(news_metadata, key=lambda d: d['date'])
    news_metadata.reverse()

    return news_metadata

