import urllib.request
import re

url = 'http://news.baidu.com/'
content = urllib.request.urlopen(url).read().decode('gbk')

#Example��
#<li class="hdline0">
#<i class="dot"></i>
#<strong>
#<a href="http://china.huanqiu.com/article/2016-07/9209287.html?from=bdwz " target="_blank" class="a3" mon="ct=1&amp;a=1&amp;c=top&amp;pn=0">xxx����ƶ�������������</a>
#</strong>
#</li>

pattern = re.compile('<li class="hd.*?<strong>.*?<a.*?>(.*?)</a>.*?strong>', re.S)
hotNews = re.findall(pattern, content)

for i in hotNews:
  print(i)
