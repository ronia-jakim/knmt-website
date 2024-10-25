#!/usr/bin/env python

import frontmatter 
import markdown

from jinja2 import Environment, FileSystemLoader
from sys import argv


import datetime





is_github_pages = False
if "--github-pages" in argv:
    is_github_pages = True




environment = Environment(loader=FileSystemLoader("src/templates/"))
template = environment.get_template("post.html")

chronological_news = ['bargiela_25X2024.md', 'kandybo_old.md']

news_path = 'content/news/'
target_path = 'build/content/news/'

news_metadata = []

for n in chronological_news: 
    with open(news_path + n) as n_file:
        post = frontmatter.load(n_file)

        meta_data = post.metadata 
        meta_data['content'] = markdown.markdown(post.content)
        meta_data['path'] = "content/news/"+n+".html"

        meta_data['date'] = datetime.datetime.strptime(meta_data['date'], '%Y.%m.%d').date()

        if 'description' not in meta_data:
            meta_data['description'] = post.content[:100]+"..."

        html_cnt = template.render(f = meta_data, github=is_github_pages)
        with open(target_path+n+".html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)

        news_metadata.append(meta_data)

news_metadata = sorted(news_metadata, key=lambda d: d['date'])
news_metadata.reverse()

template = environment.get_template("index.html")

html_cnt = template.render(posts = news_metadata[:5], github=is_github_pages)
with open("build/index.html", mode="w", encoding="utf-8") as m:
    m.write(html_cnt)


