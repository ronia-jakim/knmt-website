from jinja2 import Environment, FileSystemLoader
import frontmatter

import os
import re

photo_path = 'content/photos/'

def build_main_photos(environment):
    
    # get list of all albums in photo directory
    album_lst = os.listdir(photo_path)

    # get parsed info about all albums
    album_info = build_album_pages(environment, album_lst)
        
    # set template
    template = environment.get_template("photos.html")

    html_cnt = template.render(photo_lst = album_info)
    with open("build/photo.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)

def build_album_pages(environment, album_lst):
    album_meta_data = []

    for a in album_lst:
        # open file with information about album
        with open(photo_path + a + '/info.md') as i_file:
            a_md = frontmatter.load(i_file)

        # dictionary with information
        a_info = a_md.metadata

        img_list = os.listdir(photo_path + a)

        # no preview set
        if 'preview' not in a_info:
            # find the first file that does not have .md extension
            a_info['preview'] = re.findall("/^[^.]+$|\.(?!(md)$)([^.]+$)/", img_list)[0]

        
        a_info['album_path'] = 'content/photos/' + a + 'index.html'

        album_meta_data.append(a_info)
    return album_meta_data
    

