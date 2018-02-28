import requests
import chardet

class HtmlDownloader(object):
    def download(self, url):
        if url != None:
            headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'};
            req = requests.get(url, headers = headers);
            req.encoding = chardet.detect(req.content)['encoding'];
            return req.text;
        else:
            return None;


if __name__ == '__main__':
    #test
    url = r'https://baike.baidu.com/item/%E6%99%BA%E8%83%BD%E7%94%B5%E7%BD%91';
    print(HtmlDownloader().download(url));