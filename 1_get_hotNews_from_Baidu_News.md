# 目标：
该简单脚本用来演示爬虫的效果

# 知识点：
1. python3使用 urllib.request.urlopen 去打开一个特定网址
2. 中文可以加 decode('gbk') 来避免乱码
3. re.S 用来解决跨行匹配的问题，用法： re.compile(pattern, re.S)


# hotnews from baidu:

![](http://o7ubfyghw.bkt.clouddn.com/baidu%20hotnews.jpg)

# script excute result:

![](http://o7ubfyghw.bkt.clouddn.com/crawler%20baidu%20hotNews.jpg)