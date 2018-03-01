from scrapy import cmdline  

cmdline.execute(r"scrapy crawl zhihu -s JOBDIR=result/crawls/zhihu-1".split())  

