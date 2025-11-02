import frontmatter
from jinja2 import Environment, FileSystemLoader

def getEnvironment():
    return Environment(loader = FileSystemLoader('wss/'))

def getSubpages():
    try:
        with open('wss/subpages/list.md') as f:
            subpages = frontmatter.load(f).metadata['subpages']
            return subpages
    except Exception as inst:
        print('could not find subpages of base')
        print(inst)

