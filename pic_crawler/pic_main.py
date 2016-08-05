# -*- coding=utf-8 -*-
# Created by hztaoran at 2015/8/5
# GitHub:Lemonjing

from pic_crawler import html_downloader
from pic_crawler import html_outputer
from pic_crawler import html_parser
from pic_crawler import url_manager


'''
以http://tinymood.com为例抓取图片并保存在D:/images
'''


class PicMain(object):
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
                print 'crawl %d : %s' % (count, new_url)
                html_content = self.downloader.download(new_url)
                new_urls, new_data = self.parser.parse(new_url, html_content)
                self.outputer.collect_data(new_data)
                self.urls.add_new_urls(new_urls)

                if count == 50:
                    break
                count += 1
        except:
            print 'crawl failed'

        self.outputer.save_pics()

if __name__ == "__main__":
    root_url = "http://tinymood.com"
    obj_crawler = PicMain()
    obj_crawler.crawl(root_url)
