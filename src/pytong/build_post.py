import frontmatter 
import markdown

from jinja2 import Environment, FileSystemLoader

content_dir = 'content/news/'

def build_post_pages ():
    post_list = os.listdir(content_dir)
