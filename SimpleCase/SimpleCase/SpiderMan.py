from UrlManager import UrlManager
from HtmlDownloader import HtmlDownloader
from HtmlParser import HtmlParser
from DataOutput import DataOutput

class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager();
        self.downloader = HtmlDownloader();
        self.parser = HtmlParser();
        self.output = DataOutput();

    def start(self, url, numMax=50):
        self.manager.addUrl(url);
        num = 0; errorsNum = 0;
        while self.manager.sizeofNew() != 0 and num < numMax:
            try:
                num = num + 1;
                url = self.manager.getUrl();
                print('%d\n %s' % (num, url));
                html = self.downloader.download(url);
                newUrls, data = self.parser.parser(url, html);
                self.output.addData(data);
                if self.manager.sizeofNew() + self.manager.sizeofOld() < numMax:
                    self.manager.addUrls(newUrls);
                print(data['title']);
            except:
                num = num - 1;
                errorsNum = errorsNum + 1;
                print('crawl failed %d' % errorsNum);
        self.output.outputData();


if __name__ == '__main__':
    url = r'https://baike.baidu.com/item/%E6%99%BA%E8%83%BD%E7%94%B5%E7%BD%91';
    crawl = SpiderMan();
    crawl.start(url, 500);
