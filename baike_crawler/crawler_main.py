# -*- coding:utf-8 -*-

from baike_crawler import html_downloader
from baike_crawler import html_outputer
from baike_crawler import html_parser
from baike_crawler import url_manager


'''
以抓取百度百科为例
入口url：http://baike.baidu.com/view/21087.htm（Python词条）
'''

class CrawlerMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def crawl(self, root_url):
        count = 1
        self.urls.add_new_url(root_url)
        try:
            while self.urls.has_new_url():
                new_url = self.urls.get_new_url()
                print 'craw %d : %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.urls.add_new_urls(new_urls)
                self.outputer.collect_data(new_data)

                if count == 70:
                    break
                count += 1
        except:
            print 'crawl failed'
        self.outputer.output_html()


if __name__ == "__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"
    obj_crawler = CrawlerMain()
    obj_crawler.crawl(root_url)
