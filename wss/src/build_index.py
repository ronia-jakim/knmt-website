import frontmatter

from basic_functions import getEnvironment, getSubpages

BASE_INFORMATION = 'content/wss/wss_info.md'
TARGET_PATH = 'build/wss/index.html'

def build_index():
    subpages = getSubpages() 

    env = getEnvironment()
    template = env.get_template("index.html")

    with open(BASE_INFORMATION) as info_file:
        info = frontmatter.load(info_file)

    wss_info = info.metadata
    
    html_cnt = template.render(
            subpages = subpages,
            data = wss_info['data'],
            oplata = wss_info['oplata'],
            koszt_obiadu = wss_info['koszt_obiadu'],
            nr_rachunku = wss_info['nr_rachunku'],
            email_kontaktowy = wss_info['email_kontaktowy']
    )
    with open(TARGET_PATH, mode="w", encoding="utf-8") as m:
        m.write(html_cnt)

    
