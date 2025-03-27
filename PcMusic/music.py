import requests
from bs4 import BeautifulSoup
import re


urls="https://www.ihaoge.net/song/1036186.html"
headers={
    "cookie":"mid_452074631=https%3A%2F%2Fer-sycdn.kuwo.cn%2F7cf4ff49047344e5c82d4480ed24e072%2F67c647bf%2Fresource%2F30106%2Ftrackmedia%2FM800002hHVfm45eQwc.mp3; mid_460357210=https%3A%2F%2Fer-sycdn.kuwo.cn%2Fb27e47c94e0003d062d348c5b3f9cf5a%2F67c65570%2Fresource%2F30106%2Ftrackmedia%2FM500003MOYVz0dkl14.mp3; mid_460086146=https%3A%2F%2Fer-sycdn.kuwo.cn%2Fa201f27af6ba6d062da43cd1507e767c%2F67c6588c%2Fresource%2F30106%2Ftrackmedia%2FM500001f9LSi0JUTZT.mp3; mid_459700945=https%3A%2F%2Fer-sycdn.kuwo.cn%2F9b76ef82ec1668901d181c8a0e57be6c%2F67c66108%2Fresource%2F30106%2Ftrackmedia%2FM800002Ugb4T1I4kPd.mp3; mid_459471270=https%3A%2F%2Fer-sycdn.kuwo.cn%2F204ef82efc4cc169c8c69664fc93ecba%2F67c66126%2Fresource%2F30106%2Ftrackmedia%2FM80000098klX2HijYz.mp3; mid_460966431=https%3A%2F%2Flx-sycdn.kuwo.cn%2F141f654b66ddb70f6edab989dfb53a23%2F67c661a1%2Fresource%2Fn1%2F59%2F23%2F3200022182.mp3; mid_460040051=https%3A%2F%2Fer-sycdn.kuwo.cn%2F9e91631e462128b7ae365c6a7c498937%2F67c6657d%2Fresource%2F30106%2Ftrackmedia%2FM50000063P4b285XyR.mp3; Hm_key=Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324; Hm_lvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740989823,1741047746; HMACCOUNT=6646E76054CBD02A; Hm_lpvt_36ec17e5f302aa77ee4b02ebb3f1658d=1741055360; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=sKPiKappbHAFWhez2hctetmHJ2tRieSB",
    "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
res=requests.get(url=urls,headers=headers)
html=BeautifulSoup(res.text,"lxml")
# print(html)
c=0
scripts=html.find_all("script")
# for i in scripts:
    
#     print(i,c)
#     c=c+1
# print(scripts[5])


sd=" ".join(map(str,scripts[5]))
# print(scripts[:4])
# print(sd)


    






title = re.search(r"title: '([^']*)'", sd).group(1)
print(title)
author = re.search(r"author: '([^']*)'", sd).group(1)
print(author)
url = re.search(r"url: '([^']*)'", sd).group(1)
print(url)
br=re.search(r'br=([^&]*)', url).group(1)
print(br)


# # 组合为字典
# music_info = {
#     "title": title,
#     "author": author,
#     "url": url,
#     "pic": pic
# }

# print(music_info)