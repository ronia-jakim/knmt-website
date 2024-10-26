import frontmatter 

from jinja2 import Environment, FileSystemLoader

def build_index_pages(environment, news_metadata):
    template = environment.get_template("index.html")

    html_cnt = template.render(posts = news_metadata[:5])
    with open("build/index.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)

    template = environment.get_template("info.html")
    with open('content/info.md') as f:
        i = frontmatter.load(f) 

        html_cnt = template.render(p = i)
    with open("build/info.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)
