import frontmatter 
import markdown

from jinja2 import Environment, FileSystemLoader

import os
import datetime

content_dir = 'content/news/'
target_path = 'build/content/news/'

def build_post_pages (environment):
    # get all subdirectories in content/news/
    post_list = os.listdir(content_dir)

    # data for the main page
    news_metadata = []

    default_img = '/assets/img/referat_preview.jpg'


    # set jinja template
    template = environment.get_template("post.html")
    
    for p in post_list:
        with open(content_dir + p + '/info.md') as p_file:
            post = frontmatter.load(p_file)

        # load information about the post as a dictionary
        p_info = post.metadata
        
        # parse markdown in info.md file as html
        try:
            p_info['content'] = markdown.markdown(post.content)
        except:
            print(p + " failed to make post page")

        # parse the date from string to date object
        try:
            p_info['date'] = datetime.datetime.strptime(p_info['date'], '%Y.%m.%d').date()
        except:
            print("failed to convert date for post " + p)
    
        if 'preview_image' not in p_info: 
            # no preview image set, use the default 
            p_info['preview_image'] = default_img 
        else: 
            # preview image set, adjust its path 
            p_info['preview_image'] = '/' + content_dir + p + "/" + p_info['preview_image']

        # add description if not set
        if 'description' not in p_info:
            p_info['description'] = post.content[:100]+"..."

        # save path to post website
        p_info['path'] = content_dir + p # + "/index.html"

        try:
            html_cnt = template.render(f = p_info)
            with open(target_path + p + "/index.html", mode="w", encoding="utf-8") as m:
                m.write(html_cnt)
        except:
            print("failed to write on html file for " + p)

    
        news_metadata.append(p_info)

    # sort posts by given date
    news_metadata = sorted(news_metadata, key=lambda d: d['date'])
    news_metadata.reverse()

    return news_metadata
