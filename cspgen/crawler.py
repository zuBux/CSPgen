import requests
from bs4 import BeautifulSoup


def get_page(url):
    try:
        r = requests.get(url)
    except:
        print "Unable to retrieve URL: %s" % (url)
        raise
    page = r.text
    soup = BeautifulSoup(page, 'html.parser')
    return soup


def get_asset_sources(soup, elem):
    src_lst = []
    for asset in soup.find_all(elem):
        try:
            url = urlparse(asset.get('src'))
        except:
            print asset
            continue
        if url.netloc:
            dom = url.scheme + '://' + url.netloc
            src_lst.append(dom)
    return set(src_lst)


def get_images(page):
    img_lst = []
    soup = BeautifulSoup(page, 'html.parser')
    for img in soup.find_all('img'):
        src = img.get('src')
        img_lst.append(src)
    return set(img_lst)


def get_scripts(page):
    scrpt_lst = []
    for script in soup.find_all('script'):
        src = script.get('src')
        scrpt_lst.append(src)
    return set(scrpt_lst)
