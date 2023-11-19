# -*- coding = utf-8 -*-
# @Time:2023-11-10 17:31
# @Author:Mark
# @File:resize_n_cut.py
# @Software:PyCharm

import re
import cv2 as cv
import os


def get_file_path(root_dir):
    path_list = []
    for path, dirs, files in os.walk(root_dir):
        if len(files) > 0:
            for file in files:
                file_path = os.path.join(path, file)
                path_list.append(file_path)
        if len(dirs) > 0:
            for sub_dir in dirs:
                folder_path = os.path.join(path, sub_dir)
                sub_path = get_file_path(folder_path)
                path_list += sub_path

        return path_list


def resize_n_cut(path_lists, save_dir):
    # 加载图片
    for file_path in path_lists:
        # image = cv.imread('pic/test.PNG')
        # filename = file_path
        # 进行路径拆分
        root_path, filename = os.path.split(file_path)
        print(root_path)
        print(filename)
        root_dir, sub_path = root_path.split('\\', 1)
        print(root_dir)
        save_path = save_dir + '\\' + sub_path

        # 创建保存路径
        if os.path.exists(save_path):  # 当文件夹存在时清空文件夹
            # shutil.rmtree(save_path, True)
            print('dir exist')
        else:  # 当文件夹不存在时在当前路径下创建用于存放数据的文件夹
            os.makedirs(save_path)

        # 进行图片操作
        image = cv.imread(file_path)

        # 获取图像尺寸
        height, width, channels = image.shape

        fixed_width = 300
        fixed_height = int(300 / width * height)

        # new_image = cv.resize(image, (0,0), fx=0.25, fy=0.25, interpolation=cv.INTER_AREA)
        resized_image = cv.resize(image, dsize=(fixed_width, fixed_height), interpolation=cv.INTER_AREA)
        # cv.imwrite("resizedImage_pmm.jpg", new_image)
        # 保存压缩有文件
        cv.imwrite(save_dir + '\\' + sub_path + '\\' +'temp'+'\\'+ filename, resized_image)

        # 裁剪图像
        cropped_image = resized_image[75:350, 23:273]
        # 显示裁剪图像
        # cv.imshow("cropped", cropped_image)
        # 保存裁剪图像
        cv.imwrite(save_dir + '\\' + sub_path + '\\' + filename, cropped_image)


def remove_chinese(filename):
    pattern = re.compile(r'[^\x00-\x7f]+')
    return re.sub(pattern, '', filename)


def rename_files(rootdir):
    for f in os.listdir(rootdir):
        # 遍历 rootdir 目录下的文件
        path = os.path.join(rootdir, f)  # 文件路径
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
    root_dir = "readyToCut"
    # root_path = "screenshoot"
    save_dir = 'cutFinished'

    # 修改截图文件名
    rename_files(root_dir)  # 可以把改名和获取路径合并为一个方法，要不然有重复部分

    path_lists = get_file_path(root_dir)
    resize_n_cut(path_lists, save_dir)
