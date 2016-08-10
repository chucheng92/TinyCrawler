# -*- coding=utf-8 -*-
# Created by hztaoran at 2015/8/5
# GitHub:Lemonjing

import threading

from pic_crawler import html_downloader
from pic_crawler import html_outputer
from pic_crawler import html_parser
from pic_crawler import url_manager

'''
多线程爬虫
'''


class PicMain(threading.Thread):
    def __init__(self, thread_name, root_url, outputAddr):
        threading.Thread.__init__(self)
        self.urls = url_manager.UrlManager()
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()
        self.name = thread_name
        self.root_url = root_url
        self.outputAddr = outputAddr

    def crawl(self, root_url, outputAddr):
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

                if count == 10:
                    break
                count += 1
        except:
            print 'crawl failed'
        self.outputer.save_pics(outputAddr)

    def run(self):
        print "Starting " + self.name
        threadLock.acquire()
        self.crawl(self.root_url, self.outputAddr)
        threadLock.release()
        print "Exiting " + self.name

if __name__ == "__main__":
    root_url1 = "http://tinymood.com"
    root_url2 = "http://tinymood.com/2016/07/06/spring-aop.html"

    threadLock = threading.Lock()
    threads = []

    # 创建新线程
    thread1 = PicMain("Thread-1", root_url1, "D:/images1/")
    thread2 = PicMain("Thread-2", root_url2, "D:/images2/")

    # 开启线程
    thread1.start()
    thread2.start()

    # 添加线程到线程列表
    threads.append(thread1)
    threads.append(thread2)

    # 等待所有线程完成
    for t in threads:
        t.join()
    print "Exiting Main Thread"
