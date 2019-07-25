# coding:utf-8
#


class UrlManager(object):
    new_urls = set()
    old_urls = set()

    def __init__(self):
        pass

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls:
            self.new_urls.add(url)
        pass

    def add_new_urls(self, urls):
        if urls is None or len(urls)==0:
            return
        for url in urls:
            if url is None:
                return
            if url not in self.new_urls and url not in self.old_urls:
                self.new_urls.add(url)
        pass

    def has_new_url(self):
        return len(self.new_urls)!=0
        pass

    def get_new_url(self):
        new_url=self.new_urls.pop()
        self.old_urls.add(new_url)
        return new_url
        pass
