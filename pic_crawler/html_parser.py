# -*- coding:utf-8 -*-
import re
import urlparse

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_urls(self, page_url, soup):
        new_urls = set()
        # /2016/07/09/learn-redis.html
        links = soup.find_all('a', href=re.compile(r"^/\d{4}/\d{2}/\d{2}/.*html$"))
        for link in links:
            url = link['href']
            new_full_url = urlparse.urljoin(page_url, url)
            new_urls.add(new_full_url)
        return new_urls

    def _get_new_data(self, page_url, soup):
        img_src = set()
        img_nodes = soup.find_all('img')
        if img_nodes is not None:
            for img in img_nodes:
                img_src.add(urlparse.urljoin(page_url, img['src']))
        return img_src

    def parse(self, page_url, html_content):
        if page_url is None or html_content is None:
            return

        soup = BeautifulSoup(html_content, 'html.parser', from_encoding='utf-8')
        new_urls = self._get_new_urls(page_url, soup)
        new_data = self._get_new_data(page_url, soup)

        return new_urls, new_data
