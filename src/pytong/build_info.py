import frontmatter 

from jinja2 import Environment, FileSystemLoader

def build_information(environment):
    template = environment.get_template("info.html")
    with open('content/info.md') as f:
        i = frontmatter.load(f) 

        html_cnt = template.render(p = i)
    with open("build/info/index.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)
