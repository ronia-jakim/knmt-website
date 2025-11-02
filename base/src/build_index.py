import math

from basic_functions import getEnvironment, getSubpages
from build_posts import build_post_pages

def build_index():
    subpages = getSubpages()

    env = getEnvironment()
    news_metadata = build_post_pages(env, subpages)
    template = env.get_template("index.html")

    i = 1
    meta_len = len(news_metadata)
    all_pages = create_index_links(meta_len)

    sliced_data = split_index_data(news_metadata, meta_len, all_pages)
    create_index_pages(sliced_data, template, subpages)


def split_index_data(news_metadata, posts_length, all_pages):
    sliced_data = []
    i = 1
    while i  <= math.ceil(posts_length/5):
        lower = 0
        upper = i + 5
        if i > 5:
            lower = i-5

        pp = ""
        if i != 1:
            pp = f"build/index{i-1}.html"
        nn = ""
        if posts_length > 5 and (i+1) * 5 < posts_length: 
            nn = f"build/index{i+1}.html"
            

        sliced_data.append({
            "post_data": news_metadata[5*(i-1):5*i],
            "relevant_pages": all_pages[lower:upper], 
            "prev": pp, 
            "nxt": nn
            })
        i += 1
    return sliced_data

def create_index_links(posts_length):
    i = 1
    all_pages = []

    while i <= math.ceil(posts_length/5):
        u = f"index{i}.html"
        if i == 1:
            u = "/"

        all_pages.append({
            "url": u,
            "number": i 
            })
        i += 1 

    return all_pages

def create_index_pages(sliced_data: list, template, subpages):
    i = 1 
    for d in sliced_data:
        try:
            html_cnt = template.render(posts = d["post_data"], 
                                       pages=d["relevant_pages"], 
                                       prev=d["prev"], 
                                       nxt=d["nxt"], 
                                       subpages = subpages )
            target_file = "build/index.html"
            if i != 1: 
                target_file = f"build/index{i}.html"

            with open (target_file, mode="w", encoding="utf-8") as m:
                m.write(html_cnt)
            i += 1
        except Exception as inst:
            print(f'failed to create index file number {i}')
            print(inst)

