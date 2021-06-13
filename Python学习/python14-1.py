import pdb

class MyScrapy:
    urls = []

    def start_url(self, urls):
        pdb.set_trace()
        for url in urls:
            print(url)
            self.urls.append(url)

    def parse(self):
        pdb.set_trace()
        for url in self.urls:
            result = self.request_something(url)

    def request_something(self, url):
        print('requesting...')
        data = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
</body>
</html>'''
        return data


scrapy= MyScrapy()
scrapy.start_url(["http://www.zone7.cn", "http://www.zone7.cn", "http://www.zone7.cn", "http://www.zone7.cn", ])
scrapy.parse()
