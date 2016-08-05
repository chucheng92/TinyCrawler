# -*- coding:utf-8 -*-
import os
import urllib2


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def save_pics(self):
        if not os.path.exists("D:/images"):
            os.mkdir("D:/images")

        number = 1
        for urls in self.datas:
            for url in urls:
                url = url.lower()
                print url

                if url.rfind('gravatar.png') != -1:
                    continue
                if url.rfind('.jpg') != -1:
                    index = url.rfind('.jpg')
                elif url.rfind('.png') != -1:
                    index = url.rfind('.png')
                elif url.rfind('.jpeg') != -1:
                    index = url.rfind('.jpeg')
                elif url.rfind('.bmp') != -1:
                    index = url.rfind('.bmp')
                elif url.rfind('.gif') != -1:
                    index = url.rfind('.gif')
                elif url.rfind('.jpeg') != -1:
                    index = url.rfind('.jpeg')
                else:
                    print number, "后缀不符合规则，被跳过."
                    continue
                name = str(number) + url[index:]
                response = urllib2.urlopen(url)
                fout = open("D:/images/" + name, 'wb')
                print '文件%d写入...稍等' % number
                fout.write(response.read())
                fout.flush()
                fout.close()
                number += 1

        print '全部抓取完毕'
        return
