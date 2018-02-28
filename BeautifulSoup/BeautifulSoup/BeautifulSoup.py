from bs4 import BeautifulSoup as bs
import requests
import lxml
import chardet
import re

if __name__ == '__main__':
    req = requests.get('http://www.ip138.com/');
    req.encoding = chardet.detect(req.content)['encoding'];

    # BeautifulSoup
    soup = bs(req.text, 'lxml');

    
    # Tag, name, attr, string
    print('\n\n# Tag, name, attr, string');
    print('Tag: ', soup.title);
    print('Name of Tag: ', soup.title.name);    # 显示标签名称
    print('String(content) of Tag: ', soup.title.string);   # 显示文本，若标签中有唯一子标签或无子标签
    print('Attr Test of Tag: ', soup.title.get('test'));      # 查询单个属性，同字典操作， soup.title['test']关键字不存在会报错
    print('Attrs of Tag: ', soup.title.attrs);      # 查询所有属性


    # select 可用以css定
    guide = soup.select('.module.mod-guide')[0]    # 本条语句功能同下
    # find_all 默认查找所有符合条件的后代
    guide = soup.find_all(class_ = 'module mod-guide')[0];  # 由于class为python关键字，所以用class_
    guideList = guide.select('a');
    print('\n\n# Function "select" & "find_all"')
    print("Guide: ", guideList[0]);
    print("Href of Guide: %s: %s" % (guideList[0].string, guideList[0]['href'])) # 查询单个属性
    guideRe = guide.find_all(href = re.compile('train'))[0];  # 结合正则re
    print("with re: ", guideRe);


    # 树结构
    print('\n\n# Tree structure');
    # 父
    print(guideList[0].parent.name)
    
    # 子 
    # contents & children
    print(guideList[0].parent.contents) # contents
    print(list(guideList[0].parent.children)); # children 为迭代器
    # string # 显示文本内容
    print(guideList[0].parent.string);  # 多子节点，显示为None；唯一子节点或无子节点可正常显示
    print(list(guideList[0].parent.strings));   # 迭代器
    print(list(guideList[0].parent.stripped_strings)); # 迭代器

    # 兄弟 
    # previous_sibling, next_sibling, previous_siblings, next_siblings(迭代)

    # 前后，不分层次
    # previous_element, next_element
