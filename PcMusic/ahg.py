import requests
from bs4 import BeautifulSoup
import re
import json 


cookies={
    "cookie":"Hm_key=Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324; Hm_lvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740989823; HMACCOUNT=6646E76054CBD02A; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=fbxJ3CpSJRHzX8EwWxTfSACZeeRwpkSQ; Hm_lpvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740990534"
}
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}



def get_html(url):
    html = requests.get(url,headers=headers,cookies=cookies)
    html.encoding='utf-8'
    # print(html.text)
    return html.text

def parse_html(html):
    pass

def save_data():
    pass

def main():
    urls="https://www.ihaoge.net/song"
    get_html(urls)