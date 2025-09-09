from basic_functions import getEnvironment, getSubpages

BASE_INFORMATION = 'content/wss/wss_info.md'

def build_index():
    subpages = getSubpages() 

    env = getEnvironment()
    template = env.get_template("index.html")

    
