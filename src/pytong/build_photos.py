from jinja2 import Environment, FileSystemLoader
import frontmatter

import os

photo_path = 'content/photos/'

def build_main_photos(environment):
    
    # get list of all albums in photo directory
    album_lst = os.listdir(photo_path)

    # get parsed info about all albums
    album_info = build_album_pages(environment, album_lst)
        
    # set template
    template = environment.get_template("photos_main.html")

    html_cnt = template.render(photo_lst = album_info)
    with open("build/content/photos/index.html", mode="w", encoding="utf-8") as m:
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

       
        img_list = list( filter( lambda x : x[-3:] != '.md', img_list) )

        if 'preview' in a_info:
            a_info['preview'] = "/"+ photo_path + a + '/' + a_info['preview']
        else:
            a_info['preview'] = "/" +photo_path + a + '/' + img_list[0]

        
        a_info['album_path'] = '/content/photos/' + a

        album_meta_data.append(a_info)

        # set template
        template = environment.get_template("photo_page.html")

        html_cnt = template.render(photo_lst = img_list)
        with open("build/content/photos/" + a + "/index.html", mode="w", encoding="utf-8") as m:
            m.write(html_cnt)

    return album_meta_data
    

