import csv

class DataOutput(object):
    def __init__(self):
        self.dataSet = [];

    def addData(self, data):
        if not data:
            return;
        self.dataSet.append(data);

    def outputData(self):
        headers = ['title', 'url', 'summary'];
        with open('baike.csv', 'w', encoding = 'utf-8') as fw:
            f_csv = csv.DictWriter(fw, headers);
            f_csv.writeheader();
            f_csv.writerows(self.dataSet);
        print('Results is saved.');


if __name__ == '__main__':
    output = DataOutput();
    output.addData({'title': '你好', 'url': 'https', 'summary': 'Nihao'});
    output.outputData();