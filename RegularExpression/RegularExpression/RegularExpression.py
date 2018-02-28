import re

if __name__ == '__main__':
    # pattern
    pa = re.compile(r'((\d+)([a-z]+)(?P<digit>\d+))');

    # match 仅从第一个字符匹配一次
    match = pa.match('11dfdf22dfafd33');
    print('\nmatch: ', match);          
    print('group: ', match.group());    # 通过括号的分组，
    print('group1: ', match.group(1));
    print('group2: ', match.group(2));
    print('groupdict: ', match.groupdict());
    print('groups: ', match.groups());

    # search 匹配一次
    search = pa.search('11dfdf22dfafd33');
    print('\nsearch',search);

    # split 按pattern分割，返回列表
    # findall 找到所有，返回列表
    # finditer 返回迭代
    # sub 替换，返回替换后字符串
    # subn 替换，返回替换后字符串及替换次数