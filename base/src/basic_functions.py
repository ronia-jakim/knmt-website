import frontmatter
from jinja2 import Environment, FileSystemLoader

def getEnvironment():
    return Environment(loader = FileSystemLoader('base/'))

def getSubpages():
    try:
        with open('base/subpages/list.md') as f:
            subpages = frontmatter.load(f).metadata['subpages']
            return subpages
    except Exception as inst:
        print('could not find subpages of base')
        print(inst)

