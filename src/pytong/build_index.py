import frontmatter 

from jinja2 import Environment, FileSystemLoader
import math

def build_index_pages(environment, news_metadata):
    template = environment.get_template("index.html")

    i = 1
    meta_len = len(news_metadata)
    all_pages = []

    while i <= math.ceil(meta_len/5):
        u = f"index{i}.html"
        if i == 1:
            u = "/"

        all_pages.append({
            "url": u,
            "number": i 
            })
        i += 1 

    sliced_data = []

    i = 1
    while i  <= math.ceil(meta_len/5):
        lower = 0
        upper = i + 5
        if i > 5:
            lower = i-5

        pp = ""
        if i != 1:
            pp = f"build/index{i-1}.html"
        nn = ""
        if meta_len > 5 and (i+1) * 5 < meta_len: 
            nn = f"build/index{i+1}.html"
            

        sliced_data.append({
            "post_data": news_metadata[5*(i-1):5*i],
            "relevant_pages": all_pages[lower:upper], 
            "prev": pp, 
            "nxt": nn
            })
        i += 1

    i = 1 
    for d in sliced_data:
        html_cnt = template.render(posts = d["post_data"], pages=d["relevant_pages"], prev=d["prev"], nxt=d["nxt"])
        target_file = "build/index.html"
        if i != 1: 
            target_file = f"build/index{i}.html"

        print(target_file)
        with open (target_file, mode="w", encoding="utf-8") as m:
            m.write(html_cnt)
        i += 1

    # while i * 5 < meta_len:
    #     if i == 1:
    #         html_cnt = template.render(posts = news_metadata[:5], pages=pages_nr)
    #         if meta_len > 5:
    #             html_cnt = template.render(posts = news_metadata[:5], nxt="build/index2.html", pages=pages_nr)
    #         with open("build/index.html", mode="w", encoding="utf-8") as m:
    #             m.write(html_cnt)
    #
    #     else:
    #         html_cnt = template.render(posts = news_metadata[(5*(i-1) + 1):5*i], prev="build/index"+str(i-1)+".html", nxt="build/index"+str(i+1)+".html", pages=pages_nr)
    #         with open("build/index"+str(i)+".html", mode="w", encoding="utf-8") as m:
    #             m.write(html_cnt)
    #     i += 1

