import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


def get_page(url):
    try:
        r = requests.get(url, verify=False)
    except:
        print("Unable to retrieve URL: %s" % (url))
        raise
    page = r.text
    soup = BeautifulSoup(page, "html.parser")
    return soup


def get_js_sources(soup):
    src_lst = []
    inline_js = False
    for asset in soup.find_all("script"):
        js_src = asset.get("src")
        if js_src:
            url = urlparse(js_src)
            if url.netloc and url.scheme:
                dom = url.scheme + "://" + url.netloc
            elif url.netloc:
                dom = url.netloc
            elif not url.netloc and url.path:
                dom = "HOME"
            src_lst.append(dom)
        else:
            inline_js = True
    return set(src_lst), inline_js


def get_images(page):
    img_lst = []
    soup = BeautifulSoup(page, "html.parser")
    for img in soup.find_all("img"):
        src = img.get("src")
        img_lst.append(src)
    return set(img_lst)


def get_scripts(page):
    scrpt_lst = []
    for script in soup.find_all("script"):
        src = script.get("src")
        scrpt_lst.append(src)
    return set(scrpt_lst)
