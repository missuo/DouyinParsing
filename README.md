English / [简体中文](https://github.com/missuo/DouyinParsing/blob/main/README_CN.md)


# DouyinParsing
All-in-one analysis and download of TikTok(China) no-watermark videos, background music, author IDs, author nicknames, work titles, etc.

## Features
- [x] Parse no-watermark videos
- [x] Parse background music
- [x] Parse video titles
- [x] Parse author nickname
- [x] Parse author ID
- [x] No need to remove extra characters
- [ ] TikTok parsing
- [ ] Download all videos with one click

## Update
### April, 2022
- [x] Fixed known bugs（Thanks to [@Nunnber](https://github.com/Nunnber) For [#6](https://github.com/missuo/DouyinParsing/issues/6)）

### January, 2021
- [x] improved stability
- [x] speed increase
- [x] PHP interface

## Usage
### Web Version(Recommended)
[https://dy.nisekoo.com](https://dy.nisekoo.com)
![web](https://telegraph.eowo.us/file/152e74557fae149d5b8ad.png)

### iOS Shortcuts
[Add Shortcuts](https://www.icloud.com/shortcuts/b84daadd617149b7b3066f0c39305d95)

Click Share -> Copy link -> Run Shortcuts. The download will be completed automatically.

### Android App
Developing...Coming soon...

## Call Interface - For Developers
- **Please be careful not to use my interface for any profit-making activities.**
- **I don't have any restrictions on the number of times the interface can be used.**
- **Developers can call it an unlimited number of times to finish the parsing of the applet or other versions.**
- **No need to remove any Chinese characters when passing in parameters.**
- **Support GET and POST requests**
- **Please remove the referrer in the jump**
> `rel="noopener noreferrer"` or `<meta name="referrer" content="never">`

API: *[https://api.missuo.me/douyin](https://api.missuo.me/douyin)*

Example: (Send GET Request)
```
https://api.missuo.me/douyin?url=https://v.douyin.com/JHC3f6U/
```
Response(Success):
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

Response(Failed):
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

## Python Version
The open source code for this repository.

## License
[Apache License 2.0](https://github.com/missuo/DouyinParsing/blob/main/LICENSE) 

**Forbidden for any commercial use**








