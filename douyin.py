#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# https://github.com/missuo/douyin


import requests
import re
import webbrowser

# 用户输入抖音
all_url = input("请输入需要解析的链接:(支持包含中文)") 
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    # 匹配模式
url_list = re.findall(pattern,all_url) 
url = url_list[0]
#print(url)

def get_redirect_url(url):
	header = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
		'Upgrade-Insecure-Requests': '1'
	}
	data = requests.get(headers=header, url=url, timeout=5)
	vid = re.findall(r'\d+',data.url)
	return vid[0]
vid = get_redirect_url(url)
# print(vid)

headers = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
	'Upgrade-Insecure-Requests': '1'
}

response = requests.get(
	url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+str(vid), 
	headers = headers
	)
item = response.json().get("item_list")[0]
# print(item.get("video"))

mp4 = item.get("video").get("play_addr").get("url_list")[0].replace("playwm", "play")
print('真实的视频链接为:',mp4)


res = requests.get(mp4, headers=headers, allow_redirects=True)
mp4url = res.url
desc = item.get("desc")
video = requests.get(url=mp4url, headers=headers)
with open(desc+".mp4", 'wb') as f:
	f.write(video.content)
	f.close()
	print(u"已经完成下载。")
	