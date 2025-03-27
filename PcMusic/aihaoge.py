import requests
from bs4 import BeautifulSoup
import re 
import time
import pandas as pd

urls="https://www.ihaoge.net/song"

cookies={
    "cookie":"mid_460357210=https%3A%2F%2Fer-sycdn.kuwo.cn%2Fb27e47c94e0003d062d348c5b3f9cf5a%2F67c65570%2Fresource%2F30106%2Ftrackmedia%2FM500003MOYVz0dkl14.mp3; mid_460086146=https%3A%2F%2Fer-sycdn.kuwo.cn%2Fa201f27af6ba6d062da43cd1507e767c%2F67c6588c%2Fresource%2F30106%2Ftrackmedia%2FM500001f9LSi0JUTZT.mp3; mid_459700945=https%3A%2F%2Fer-sycdn.kuwo.cn%2F9b76ef82ec1668901d181c8a0e57be6c%2F67c66108%2Fresource%2F30106%2Ftrackmedia%2FM800002Ugb4T1I4kPd.mp3; mid_459471270=https%3A%2F%2Fer-sycdn.kuwo.cn%2F204ef82efc4cc169c8c69664fc93ecba%2F67c66126%2Fresource%2F30106%2Ftrackmedia%2FM80000098klX2HijYz.mp3; mid_460040051=https%3A%2F%2Fer-sycdn.kuwo.cn%2F9e91631e462128b7ae365c6a7c498937%2F67c6657d%2Fresource%2F30106%2Ftrackmedia%2FM50000063P4b285XyR.mp3; mid_257275669=https%3A%2F%2Flt-sycdn.kuwo.cn%2Feeac5305cc6b04a2d032b1b2c3e978e4%2F67c675ba%2Fresource%2Fn3%2F65%2F47%2F488640543.mp3; mid_460966431=https%3A%2F%2Flx-sycdn.kuwo.cn%2F58e6922fb0465129a3a01dc5559a0498%2F67c675c3%2Fresource%2Fn1%2F59%2F23%2F3200022182.mp3; mid_456266462=https%3A%2F%2Fer-sycdn.kuwo.cn%2F3e209a34539d1ff4ef554a120b5480d6%2F67c675c6%2Fresource%2F30106%2Ftrackmedia%2FM500003mxncQ1BvfPz.mp3; mid_460937881=https%3A%2F%2Fer-sycdn.kuwo.cn%2Fdf9c70d69b609c1f6230a0dbc90a794f%2F67c675d7%2Fresource%2F30106%2Ftrackmedia%2FM500001sGpuz3l1gNL.mp3; mid_452074631=https%3A%2F%2Fer-sycdn.kuwo.cn%2F4cf0fc0444813b92a83c2ad3b5448a21%2F67c6947a%2Fresource%2F30106%2Ftrackmedia%2FM800002hHVfm45eQwc.mp3; Hm_key=Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324; Hm_lvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740989823,1741047746; HMACCOUNT=6646E76054CBD02A; Hm_lpvt_36ec17e5f302aa77ee4b02ebb3f1658d=1741067453; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=KRmddnkMw4Z4TeZCea6hE6TsEKtDEHK6",
    "cookie":"Hm_key=Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324; Hm_lvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740989823; HMACCOUNT=6646E76054CBD02A; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=fbxJ3CpSJRHzX8EwWxTfSACZeeRwpkSQ; Hm_lpvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740990534"
}
headers={
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

res =requests.get(url=urls,headers=headers,cookies=cookies)
# print(res.text)

soup=BeautifulSoup(res.text,"lxml")
# print(soup.a["href"])
a_list=soup.find_all('a',rel="bookmark")
# print(len(a_list))
# print(a_list[:80])
href_list=[]
for a in a_list[:80]:
    href_list.append(a.get("href"))

title_all=[]
author_all=[]
url_all=[]
br_all=[]

for i in href_list:
    url1=i
    res1 =requests.get(url=url1,headers=headers,cookies=cookies)
    soup1=BeautifulSoup(res1.text,"lxml")
    scripts=soup1.find_all("script")
    sd=" ".join(map(str,scripts[5]))
    # print(sd)
    title = re.search(r"title: '([^']*)'", sd).group(1)
    title_all.append(title)
    author = re.search(r"author: '([^']*)'", sd).group(1)
    author_all.append(author)
    url = re.search(r"url: '([^']*)'", sd).group(1)
    url_all.append(url)
    br=re.search(r'br=([^&]*)', url).group(1)
    br_all.append(br)
    time.sleep(2)

music_info = {
    "title": title_all,
    "author": author_all,
    "url": url_all,
    "br": br_all
}

df=pd.DataFrame(music_info)


# df.to_excel("music.xlsx",sheet_name="Sheet1",index=False)
df.to_csv("music.csv")






