import requests
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad
import base64
import json
import binascii

# 加密密钥
PUBLIC_KEY = '010001'
MODULUS = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
IV = '0102030405060708'

def encrypted_request(text):
    text = json.dumps(text)
    sec_key = create_secret_key(16)
    enc_text = aes_encrypt(text, sec_key)
    enc_sec_key = rsa_encrypt(sec_key)
    return {'params': enc_text, 'encSecKey': enc_sec_key}

def aes_encrypt(text, key):
    pad_text = pad(text.encode(), AES.block_size)
    encryptor = AES.new(key.encode(), AES.MODE_CBC, IV.encode())
    ciphertext = encryptor.encrypt(pad_text)
    return base64.b64encode(ciphertext).decode()

def rsa_encrypt(text):
    text = text[::-1]
    rs = pow(int(binascii.hexlify(text.encode()), int(PUBLIC_KEY, 16), int(MODULUS, 16)))
    return format(rs, 'x').zfill(256)

def create_secret_key(size):
    return binascii.hexlify(bytes.fromhex('0'*size)).decode()

# 获取歌曲信息
def get_song_info(keyword):
    url = 'https://music.163.com/weapi/cloudsearch/get/web?csrf_token='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://music.163.com/'
    }
    data = {
        's': keyword,
        'type': 1,
        'offset': 0,
        'limit': 10
    }
    response = requests.post(url, data=encrypted_request(data), headers=headers)
    return response.json()

# 获取播放地址
def get_song_url(song_id, bitrate=320000):
    url = 'https://music.163.com/weapi/song/enhance/player/url?csrf_token='
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://music.163.com/'
    }
    data = {
        'ids': [song_id],
        'br': bitrate
    }
    response = requests.post(url, data=encrypted_request(data), headers=headers)
    return response.json()

# 主程序
if __name__ == '__main__':
    keyword = input("请输入歌曲名称: ")
    song_info = get_song_info(keyword)
    songs = song_info.get('result', {}).get('songs', [])
    
    for song in songs:
        song_id = song['id']
        song_name = song['name']
        print(f"歌曲名称: {song_name}")
        
        # 获取不同比特率
        for br in [128000, 192000, 320000, 999000]:
            url_data = get_song_url(song_id, br)
            if url_data['data']:
                print(f"比特率: {br//1000}k, URL: {url_data['data'][0]['url']}")
        print("-" * 50)