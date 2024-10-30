import frontmatter 

from jinja2 import Environment, FileSystemLoader

def build_conf(environment):
    template = environment.get_template("calendar.html")
    with open('content/conf_list.md') as f:
        i = frontmatter.load(f) 

        html_cnt = template.render(conf_list = i.metadata['conferences'])
    with open("build/calendar/index.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)
