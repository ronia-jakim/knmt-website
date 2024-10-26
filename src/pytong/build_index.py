import frontmatter 

from jinja2 import Environment, FileSystemLoader

def build_index_pages(environment, news_metadata):
    template = environment.get_template("index.html")

    html_cnt = template.render(posts = news_metadata[:5])
    with open("build/index.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)

