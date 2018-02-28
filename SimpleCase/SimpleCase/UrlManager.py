
class UrlManager(object):
    def __init__(self):
        self.newUrlSet = set();
        self.oldUrlSet = set();


    def addUrl(self, newUrl):
        if not newUrl or newUrl in self.oldUrlSet:
            return;
        self.newUrlSet.add(newUrl);


    def addUrls(self, newUrls):
        if not newUrls:
            return;
        for url in newUrls:
            self.addUrl(url);


    def getUrl(self):
        url = self.newUrlSet.pop();
        self.oldUrlSet.add(url);
        return url;

    def sizeofNew(self):
        return len(self.newUrlSet);

    def sizeofOld(self):
        return len(self.oldUrlSet);





