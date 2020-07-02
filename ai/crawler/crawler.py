import os
import argparse

# BeautifulSoup - crawling module
from bs4 import BeautifulSoup

# webdriver를 통해 브라우저를 제어하는 python library
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# url 처리 모듈, urllib.request는 url을 열고 읽기 위함
import urllib, urllib.request


# argument parser를 이용해 keyword, limit, directory를 인자로 추가
parser = argparse.ArgumentParser()
parser.add_argument("--key", type = str, required = True, default = '')
parser.add_argument("--siz", type = int, default = 200)
parser.add_argument("--dir", type = str, default = './datasets/image/')

# Initial Setting
args = parser.parse_args()
keyword = args.key
size = args.siz
directory = args.dir

params = {
    "q" : keyword,
    "tbm" : "isch",
    "sa" : "1",
    "source" : "lnms&tbm=isch"
}

url = "https://www.google.com/search?" + urllib.parse.urlencode(params)
webDriver = "./chromedriver.exe"

# Main
def main():
    # browser 구동
    browser = webdriver.Chrome(webDriver)
    browser.get(url)
    html = browser.page_source

    soup = BeautifulSoup(html, 'html.parser')
    el = browser.find_element_by_tag_name("body")

    # size 만큼 pagedown 및 데이터 추출
    cnt = 0
    while cnt < size:
        el.send_keys(Keys.PAGE_DOWN)
        imgcnt = len(soup.find_all("img", limit = size))
        cnt += imgcnt

    imgs = soup.find_all("img")
    browser.find_element_by_tag_name("img")

    fileNum = 0
    source = []

    # 다운로드할 source를 src에 저장
    for img in imgs:
        if str(img).find('data-src') != -1:
            print(fileNum + 1, ":", img['data-src'])
            source.append(img['data-src'])
            fileNum += 1

    # 이미지가 저장될 디렉토리 지정
    saveDir = directory + keyword

    if not(os.path.isdir(directory)):
        os.mkdir(directory)
    if not(os.path.isdir(saveDir)):
        os.mkdir(saveDir)

    # 이미지 저장
    for fn, src in zip(range(fileNum), source):
        urllib.request.urlretrieve(src, saveDir + "/" + keyword + "_" + str(fn + 1) + ".jpg")
        print(fn + 1, "saved")

if __name__ == "__main__":
    main()