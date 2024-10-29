import frontmatter 

from jinja2 import Environment, FileSystemLoader

def build_book_list(environment):
    template = environment.get_template("books.html")
    with open('content/book_list.md') as f:
        i = frontmatter.load(f) 

        # print(i.metadata['books'])
        html_cnt = template.render(book_lst = i.metadata['books'])
    with open("build/books/index.html", mode="w", encoding="utf-8") as m:
        m.write(html_cnt)
