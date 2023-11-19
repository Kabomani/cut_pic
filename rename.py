# -*- coding = utf-8 -*-
# @Time:2023-11-09 18:07
# @Author:Mark
# @File:rename.py
# @Software:PyCharm

import os
import re


def remove_chinese(filename):
    pattern = re.compile(r'[^\x00-\x7f]+')
    return re.sub(pattern, '', filename)

# 测试代码
# filename = "文件名中的汉字.txt"
# new_filename = remove_chinese(filename)
# print(new_filename)  # 输出：文件名中的.txt


def rename_files(rootdir):
    for f in os.listdir(rootdir):
        # 遍历 rootdir 目录下的文件
        path = os.path.join(rootdir, f)   # 文件路径
        if os.path.isdir(path):
            # 如果是目录，则继续递归
            rename_files(path)
        else:
            # remove_chinese(f)
            new_name = remove_chinese(f)
            # 如果不是目录，则重命名该文件
            # new_name = 'myprefix_' + f   # 新名称
            os.rename(path, os.path.join(rootdir, new_name))

if __name__ == '__main__':
    rootdir = 'water'
    rename_files(rootdir)