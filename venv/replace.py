#!/usr/bin/python
# -*- coding: UTF-8 -*-

import re
import sys
print(sys.getdefaultencoding())

# 自定义正则
rex = "\'2018-"
new_str = "\'2019-"
# old_file_path = r'E:\database\database\t_acq_data_2018_whole.sql'
# new_file_path = r'E:\database\database\t_acq_data_2019_whole.sql'
# rex = "PRIMARY KEY \(\`ACQ_DATA_ID\`\)\r\n"
# new_str = "PRIMARY KEY \(\`ACQ_DATA_ID\`\)\,\r\n"
old_file_path = r'E:\database\database\t_acq_data_2018.sql'
new_file_path = r'E:\database\database\t_acq_data_2019.sql'


def match_timestamp(repex, eachline):
    p = re.compile(repex)
    return p.findall(eachline.decode('utf-8'))


# 打开旧文件，将每一行yield后作为迭代器返回。
def old_file_yield(old_file_path):
    with open(old_file_path, 'rb') as  oldf:
        while True:
            line = oldf.readline()
            yield line
            if not line:
                oldf.close()
                break


# 打开新文件开始逐行读取替换。
def replace_match(old_file_path, new_file_path):
    count = 0
    with open(new_file_path, "w", encoding='utf-8') as newf:
        for line in old_file_yield(old_file_path):
            ifmatch = match_timestamp(rex, line)
            if not line:
                newf.close()
                return count
                break
            elif ifmatch != []:
                count += 1
                print("替换前：%s" % line)
                line = line.replace(rex.encode("utf-8"),new_str.encode("utf-8"))
                print("替换后：%s" % line)
                newf.write(line.decode('utf-8'))
            else:
                newf.write(line.decode('utf-8'))


print('一共替换了%s行' % replace_match(old_file_path, new_file_path))