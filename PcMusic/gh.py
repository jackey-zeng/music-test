import requests
from mutagen.mp3 import MP3
from io import BytesIO

def get_mp3_bitrate(url):
    # 设置请求头，添加Referer以避免403错误
    headers = {
        "Referer": "https://www.kuwo.cn/"
    }

    # 下载文件的前4KB（通常包含元数据）
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()

    # 读取前4KB数据
    fragment = BytesIO(response.content[:4096])

    # 使用mutagen解析MP3文件
    audio = MP3(fragment)
    bitrate = audio.info.bitrate // 1000  # 转换为kbps

    return bitrate

# MP3文件URL
mp3_url = "https://lx-sycdn.kuwo.cn/141f654b66ddb70f6edab989dfb53a23/67c661a1/resource/n1/59/23/3200022182.mp3"

# 获取比特率
try:
    bitrate = get_mp3_bitrate(mp3_url)
    print(f"MP3文件的比特率为: {bitrate} kbps")
except Exception as e:
    print(f"无法获取比特率: {e}")


    