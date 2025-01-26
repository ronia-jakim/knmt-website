import frontmatter 

from jinja2 import Environment, FileSystemLoader

def build_wss_index(environment):
    template = environment.get_template("wss/index.html")

    html_cnt = template.render()
    with open("build/wss/index.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)

    print("build/wss/index.html")

def build_wss_registration(environment):
    template = environment.get_template("wss/registration.html")

    html_cnt = template.render()

    with open("build/wss/registration.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)


def build_wss_programme(environment):
    template = environment.get_template("wss/programme.html")

    html_cnt = template.render()

    with open("build/wss/programme.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)
