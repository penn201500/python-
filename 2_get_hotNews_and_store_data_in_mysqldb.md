# 目标：
爬取到数据之后，存放到数据库

# 知识点：
1. python3.x 使用pymysql来与mysqlDB交互；可以使用 pip install pymysql 命令安装pymysql
2. pymysql的使用： http://www.runoob.com/python3/python3-mysql.html
3. mysql的一些用法：
   show databases;
   use test;
   show tables;
   drop tables;
4. 格式化时间：time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
5. 某表不存在时创建该表：
   sql = """CREATE TABLE IF NOT EXISTS %s (
               text  VARCHAR(200),
               time  VARCHAR(200),
               date VARCHAR(200))""" % (table,)
               
               
               
---
excute and output is:
```
E:\github_projects\python-crawler>python 2_get_hotNews_and_store_data_in_mysqldb.py
习近平：扶贫工作不搞层层加码
7月20日的国务院常务会定了这3件大事
《寒战2》3D电影引争议 特效渣渣有圈钱之嫌

习近平：扶贫工作不搞层层加码
7月20日的国务院常务会定了这3件大事
《寒战2》3D电影引争议 特效渣渣有圈钱之嫌

(('习近平：扶贫工作不搞层层加码', '2016-07-22 03:12:12', '2016-07-22'),)          
```
