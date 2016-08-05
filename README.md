## 爬虫架构

1、爬虫调度端（调度器）

2、核心模块：URL管理器、（网页）下载器、（网页）解析器

- URL管理器
- 下载器 urllib2 request
- 解析器 正则表达式 html.parser(python自带) BeautilfulSoup lxml

**区别**

正则表达式: 模糊匹配

html.parser(python自带) BeautilfulSoup lxml: 结构化解析(DOM树的方式)


本例
----


以抓取百度百科为例

入口url：http://baike.baidu.com/view/21087.htm（Python词条）