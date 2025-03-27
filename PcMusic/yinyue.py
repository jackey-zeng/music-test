import requests
from bs4 import BeautifulSoup
import re
import time

# 定义音乐网站的URL，这里以示例URL代替，实际使用时需要替换为真实有效的音乐网站URL
url ='https://www.ihaoge.net/song'

# 发送HTTP请求
cookies={
    'Hm_key':"Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324; Hm_lvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740625980,1740646445; HMACCOUNT=D3C9FCE6E3ED44C5; Hm_Iuvt_cdb524f42f23cer9b268564v7y735ewrq2324=AeyJDkN6syFpG86SiBSFQGYwCdmAbaTM; Hm_lpvt_36ec17e5f302aa77ee4b02ebb3f1658d=1740649022"
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.47'}
response = requests.get(url, headers=headers,cookies=cookies)

# 检查请求是否成功
if response.status_code == 200:
    # 解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 假设音乐信息存储在<a>标签中，且标签有特定的class属性，这里需要根据实际情况修改
    music_links = soup.find_all('a')

    # 用于存储音乐名称和下载链接的字典
    music_dict = {}

    for link in music_links:
        # 获取音乐名称
        music_name = link.text.strip()
        # 获取音乐下载链接
        music_url = link.get('href')

        if music_name and music_url:
            # 将音乐名称和下载链接添加到字典中
            music_dict[music_name] = music_url

    # 打印分类结果
    for name, url in music_dict.items():
        print(f"音乐名称: {name}, 音乐网址: {url}")
else:
    print(f"请求失败，状态码: {response.status_code}")