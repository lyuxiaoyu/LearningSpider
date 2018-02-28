from bs4 import BeautifulSoup
import lxml

class HtmlParser(object):
    def parser(self, url, html):
        if not html or not url:
            return None, None;
        else:
            try:
                soup = BeautifulSoup(html, 'lxml');
                title = soup.find(class_ = 'lemmaWgt-lemmaTitle-title');
                summary = soup.find(class_ = 'lemma-summary');
                # data
                data = {}
                data['url'] = url;
                data['title'] = title.find('h1').get_text();
                data['summary'] = summary.get_text();
                # urls
                newUrls = set();
                links = summary.select('a');
                for link in links:
                    href = link.get('href');
                    if href is not None:
                        newUrls.add('https://baike.baidu.com' + href);
                return newUrls, data;
            except Exception as e:
                print('HtmlParser error');
                return None, None;
            

if __name__ == '__main__':
    from HtmlDownloader import HtmlDownloader;
    url = r'https://baike.baidu.com/item/%E9%B2%81%E8%BF%85';
    html = HtmlDownloader().download(url);
    newUrls, data = HtmlParser().parser(url, html);
    print(newUrls);
    print(data);


