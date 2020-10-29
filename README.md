# Boss-python说明文档

## 介绍

Boss-python是一个基于Scrapy的爬虫，是使用selenium自动化测试平台模拟登录Boss直聘网站获取页面数据



本程序使用了selenium自动化框架用于模拟登录，需提前安装

本程序使用了scrapy爬虫框架，需要提前安装

本程序使用了图鉴打码平台解决验证码，需提前注册账号使用，网址如下

http://www.ttshitu.com/



数据库使用Mongodb存储，运行需要安装Mongodb



## 运行

命令在Boss目录下，运行命令：

scrapy crawl python



## MongoDB部分数据

{
    "_id" : ObjectId("5f995c04e11cf829dc9bc4e3"),
    "name" : "少儿编程讲师Python/Java/C++",
    "name_link" : "https://www.zhipin.com/job_detail/49a25e9ea797185f3nZz2ty8E1A~.html",
    "address" : "长沙·芙蓉区·晚报",
    "salary" : "6-10K",
    "company" : "童程童美"
}
{
    "_id" : ObjectId("5f995c04e11cf829dc9bc4e4"),
    "name" : "少儿编程讲师/Python讲师/机器人老师",
    "name_link" : "https://www.zhipin.com/job_detail/e94943057c4df47a3nV63Nq5E1Y~.html",
    "address" : "长沙·开福区·万国城",
    "salary" : "6-11K",
    "company" : "童程创客教育"
}
{
    "_id" : ObjectId("5f995c04e11cf829dc9bc4e5"),
    "name" : "python程序员",
    "name_link" : "https://www.zhipin.com/job_detail/d7fe4dc4085f4b0e1nR_3dy5ElJT.html",
    "address" : "长沙·雨花区·德思勤城市广场",
    "salary" : "6-7K",
    "company" : "锦阁装饰"
}
{
    "_id" : ObjectId("5f995c04e11cf829dc9bc4e6"),
    "name" : "Python开发",
    "name_link" : "https://www.zhipin.com/job_detail/869269b9a7b740c71nR809u6EVtS.html",
    "address" : "长沙·长沙县·星沙一桥",
    "salary" : "6-11K",
    "company" : "绯逸信息"
}
{
    "_id" : ObjectId("5f995c04e11cf829dc9bc4e7"),
    "name" : "程序员(兼职)",
    "name_link" : "https://www.zhipin.com/job_detail/170628d8c34687741nR5392_FFJX.html",
    "address" : "长沙·岳麓区·汽车西站",
    "salary" : "10-13K",
    "company" : "奇迹互动"
