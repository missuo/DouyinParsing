# DouyinParsing
抖音(中国区)无水印视频、背景音乐、作者ID、作者昵称、作品标题等的全能解析和下载

# 电脑端/安卓端推荐使用网页版 [https://dy.nisekoo.com](https://dy.nisekoo.com)
# 苹果端推荐使用 [快捷指令](https://www.icloud.com/shortcuts/b84daadd617149b7b3066f0c39305d95)

## 写在前面
* 本项目纯属个人爱好创作
* 所有视频的版权始终属于「字节跳动」
* 严禁用于任何商业用途，如果构成侵权概不负责
* PHP接口的代码暂不开源，但您仍可以使用 [解析接口](https://api.missuo.me/douyin)
* **强烈推荐使用** 我搭建的解析网站为 [抖音解析平台](https://dy.nisekoo.com)
* 由于iOS保存视频比较麻烦，推荐使用我的「[快捷指令](https://www.icloud.com/shortcuts/b84daadd617149b7b3066f0c39305d95)」版本

### 快捷指令版本使用指南
在抖音App内点击分享 -> 复制链接 -> 运行指令。即可自动完成下载。

与网页版使用的是同样的接口，所以我会同时维护两个版本。

网站截图
![截图](https://telegraph.eowo.us/file/152e74557fae149d5b8ad.png)

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
### 2022年4月更新
- [x] 修改已知Bug（感谢[@Nunnber](https://github.com/Nunnber)的[反馈](https://github.com/missuo/DouyinParsing/issues/6)）

### 2021年1月更新
- [x] 稳定性提升
- [x] 速度提升
- [x] PHP接口

## 接口使用
对于接口的使用次数，我没有做任何限制。大家可以无限次调用，来完成小程序或者别的版本的解析。

**接口和网页解析一致，都无需去除中文和多余字符**

接口：[https://api.missuo.me/douyin](https://api.missuo.me/douyin)

- [x] 支持POST
- [x] 支持GET

请求时需要提交的参数为：url = XXX

你可以打开抖音APP，在某个视频右下角点击「分享」按钮，再选择「复制链接」来获取url参数的Value。

例如：

发送GET请求
```
https://api.missuo.me/douyin?url=https://v.douyin.com/JHC3f6U/
```

正常返回为：
```json
{
    "code": 200,
    "status": "success",
    "mp4": "https://aweme.snssdk.com/aweme/v1/play/?video_id=v0300fac0000bunodsrcdphlft5871u0&ratio=720p&line=0",
    "mp3": "https://sf6-cdn-tos.douyinstatic.com/obj/ies-music/6889721604616899336.mp3",
    "desc": "与其隔空要求的忠诚 不如让彼此自由",
    "id": "20377085",
    "nickname": "拔刀小爱神"
}
```

错误返回为：
```json
{
    "code": 404,
    "status": "failed",
    "msg": "Missing URL parameter!"
}
```
```json
{
    "code": 404,
    "status": "failed",
    "msg": "Incomputive URL is incorrect!"
}
```
