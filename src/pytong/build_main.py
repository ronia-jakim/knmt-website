#!/usr/bin/env python

import frontmatter 
import markdown

from jinja2 import Environment, FileSystemLoader
from sys import argv

import datetime

# setting up jinja with template directory
environment = Environment(loader=FileSystemLoader("src/templates/"))
template = environment.get_template("post.html")




default_img = '/assets/img/referat_preview.jpg'

chronological_news = ['bargiela_25X2024', 'kandybo_old']

news_path = 'content/news/'
target_path = 'build/content/news/'

news_metadata = []

for n in chronological_news: 
    with open(news_path + n + '/info.md') as n_file:
        post = frontmatter.load(n_file)

        meta_data = post.metadata 
        meta_data['content'] = markdown.markdown(post.content)
        meta_data['path'] = "content/news/"+n+"/index.html"

        meta_data['date'] = datetime.datetime.strptime(meta_data['date'], '%Y.%m.%d').date()

        if 'preview_image' not in meta_data:
            meta_data['preview_image'] = default_img
        else:
            meta_data['preview_image'] = "content/news/"+n+'/'+meta_data['preview_image']

        if 'description' not in meta_data:
            meta_data['description'] = post.content[:100]+"..."

        html_cnt = template.render(f = meta_data, github=is_github_pages)
        with open(target_path+n+"/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)

        news_metadata.append(meta_data)

news_metadata = sorted(news_metadata, key=lambda d: d['date'])
news_metadata.reverse()

template = environment.get_template("index.html")

html_cnt = template.render(posts = news_metadata[:5], github=is_github_pages)
with open("build/index.html", mode="w", encoding="utf-8") as m:
    m.write(html_cnt)

template = environment.get_template("info.html")
with open('content/info.md') as f:
    i = frontmatter.load(f) 

    html_cnt = template.render(p = i)
with open("build/info.html", mode="w", encoding="utf-8") as m:
    m.write(html_cnt)
