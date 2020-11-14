# 抖音 Douyin
**抖音无水印视频下载** <br><br>
**暂时还不支持TikTok** <br><br>
**网页版稍后会上线**
<br>

# 更新 Update
**增加了对背景音乐的下载** <br><br>
**已完成网页版解析项目** [抖音解析](https://dy.nisekoo.com) <br><br>
**已完成API接口**
<br><br>
*请求参数*
<br>
功能 | 接口 |
----------|----------|
请求方式  | GET |
URL  | https://dy.nisekoo.com/api/ |
请求参数  | url |
<br><br>
*返回类型*
<br>
| 参数名称  | 类型 |  实例值 |
|----------|----------|----------|
| url | String | https://aweme.snssdk.com/aweme/v1/play/?video_id=v0300fac0000bunodsrcdphlft5871u0&ratio=720p&line=0  |
| status  | String | success |
~~~
{"url": "https://aweme.snssdk.com/aweme/v1/play/?video_id=v0300fac0000bunodsrcdphlft5871u0&ratio=720p&line=0", "status": "success"}
~~~

# 说明 Description
**本项目纯属个人爱好，学习Python所创作，严禁用于任何商业用途**
<br>

# 用法 Usage
~~~
# 请确保已经安装requests。如果没有安装，请执行以下代码
pip3 install requests
python3 douyin.py
~~~
<br>

# 源代码 Source code
~~~
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
# https://github.com/missuo/douyin


import requests
import re
import webbrowser

# 输入链接，不用去除中文
all_url = input("请输入需要解析的链接:(支持包含中文)") 
pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')    # 正则表达式匹配URL
url_list = re.findall(pattern,all_url) # 在这里会自动从字符串中提取URL链接，返回的是一个列表
url = url_list[0]
#print(url)

# 定义函数用于获取抖音视频的id
def get_redirect_url(url):
	header = {
		'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
		'Upgrade-Insecure-Requests': '1',
	}
	data = requests.get(headers=header, url=url, timeout=5)
	vid = re.findall(r'\d+',data.url)
	return vid[0]
vid = get_redirect_url(url)
#print(vid)

# 向API发送GET请求
response = requests.get('https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids='+str(vid))
item = response.json().get("item_list")[0]
#print(item)

# 提取play_addr,也就是真实的视频链接，将playvm替换为play，以获得无水印的视频链接
mp4 = item.get("video").get("play_addr").get("url_list")[0].replace("playwm", "play")
print('真实的视频链接为:',mp4)

# 进行下载，会保存在和 .py文件 同一目录下
headers = {
	'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1',
	'Upgrade-Insecure-Requests': '1',
}
res = requests.get(mp4, headers=headers, allow_redirects=True)
mp4url = res.url
desc = item.get("desc")
video = requests.get(url=mp4url, headers=headers)
with open(desc+".mp4", 'wb') as f:
	f.write(video.content)
	f.close()
	print(u"已经完成下载。")
~~~

