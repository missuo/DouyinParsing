# DouyinParsing
抖音(中国区)无水印视频、背景音乐、作者ID、作者昵称、作品标题等的全能解析和下载

## 写在前面
* 本项目纯属个人爱好创作。
* 所有视频的版权始终属于「字节跳动」。
* 严禁用于任何商业用途，如果构成侵权概不负责。
* PHP接口的代码暂不开源，但您仍可以使用 [接口](https://dy.nisekoo.com/api)
* 我搭建的解析网站域名为 [dy.nisekoo.com](https://dy.nisekoo.com)

网站截图
![截图](https://cdn.nisekoo.com/123.png)

## 目前功能
- [x] 解析无水印视频
- [x] 解析背景音乐
- [x] 解析视频标题
- [x] 解析作者昵称
- [x] 解析作者ID
- [x] 不需要去除多余字符
- [ ] TikTok解析
- [ ] 一键下载所有视频

## 关于更新
### 2021年1月更新
- [x] 稳定性提升
- [x] 速度提升
- [x] PHP接口

## 接口使用
对于接口的使用次数，我没有做任何限制。大家可以无限次调用，来完成小程序或者别的版本的解析。

**接口和网页解析一致，都无需去除中文和多余字符**

接口：[https://dy.nisekoo.com/api](https://dy.nisekoo.com/api)

- [x] 支持POST
- [x] 支持GET

请求时需要提交的参数为：url = XXX

你可以打开抖音APP，在某个视频右下角点击「分享」按钮，再选择「复制链接」来获取url参数的Value。

例如：

发送GET请求
```
https://dy.nisekoo.com/api?url=与其隔空要求的忠诚不如让彼此自由https://v.douyin.com/JHC3f6U/复制此链接，打开抖音，直接观看视频！
```

正常返回为：
```
{
    "code": "500",
    "status": "success",
    "mp4": "https://aweme.snssdk.com/aweme/v1/play/?video_id=v0300fac0000bunodsrcdphlft5871u0&ratio=720p&line=0",
    "mp3": "https://sf3-cdn-tos.douyinstatic.com/obj/ies-music/6889721604616899336.mp3",
    "desc": "与其隔空要求的忠诚 不如让彼此自由",
    "id": "20377085",
    "nickname": "拔刀小爱神"
}
```

错误返回为：
```
{
    "code": "404",
    "status": "failed",
    "msg": "请传入URL，支持GET/POST，只需传入url参数即可"
}
```

## Python版的使用
请确保已经安装requests。如果没有安装，请执行以下代码
```
pip3 install requests
```
如果已经安装，请直接执行：
```
python3 douyin.py
```


## Python版本代码
```python
#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

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
```

