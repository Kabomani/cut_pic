# -*- coding = utf-8 -*-
# @Time:2023-11-08 20:39
# @Author:Mark
# @File:getnumber.py
# @Software:PyCharm

# 导入相关包
import cv2
import os
from PIL import Image
import pytesseract
import re


# def get_path(path):
#     # path = "water"
#     file_paths = []
#     folder_paths = []
#     path_list=get_file_path(path,file_paths)
#     # for path, dir, file in os.walk(path):
#     #     for folder in dir:
#     #         folder_path = os.path.join(path, folder)
#     #         bottom_path = get_file_path(folder_path)
#     #     # 遍历 rootdir 目录下的文件
#     #     path = os.path.join(rootdir, f)  # 文件路径
#     #     if os.path.isdir(path):
#     #         # 如果是目录，则继续递归
#     #         rename_files(path)
#     #     else:
#     #         # remove_chinese(f)
#     #         new_name = remove_chinese(f)
#     #         # 如果不是目录，则重命名该文件
#     #         # new_name = 'myprefix_' + f   # 新名称
#     #         os.rename(path, os.path.join(rootdir, new_name))
#     #
#     # for path, dir, file in os.walk(path):
#     #     for folder in dir:
#     #         folder_path = os.path.join(path, folder)
#     #
#     #         for dirpath, dirnames, filenames in os.walk(folder_path):
#     #             for
#     #             file_dir = os.path.join(folder_path, dirnames)
#     #
#     #             # file_path=folder_path+'/'+filenames
#     #             for pic in filenames:
#     #                 # 拼接文件的完整路径
#     #                 file_path = os.path.join(file_dir, pic)
#     #                 # 将文件路径添加到列表中
#     #                 file_paths.append(file_path)
#     # # print(file_paths)
#     return path_list
#     # break
#     # pic = []
#     # for i in file:
#     #     if (".png" in i):
#     #         pic.append(i)


def get_file_path(root_path):
    path_list = []
    for path, dirs, files in os.walk(root_path):
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


def cut_pic(file_paths):

    for file_path in file_paths:
        print(file_path)
        route, filename = os.path.split(file_path)
        img = cv2.imread(file_path)
        print(img.shape)  # Print image shape
        # cv2.imshow("original", img)
        # 裁剪图像
        # cropped_image = img[80:280, 150:330]
        cropped_image = img[610:930, ]
        saveRoute = 'screenshoot\\temp\\' + filename
        # 显示裁剪图像
        # cv2.imshow("cropped", cropped_image)
        cv2.imwrite(saveRoute, cropped_image)

        file_text = read_image(saveRoute)

        # 保存裁剪图像
        cv2.imwrite('screenshoot\\number\\' + file_text, cropped_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


def read_image(route):
    img = Image.open(route)
    text = pytesseract.image_to_string(img, lang='chi_sim', config='digits')

    print(text)
    name_text = text.replace("-", "").rstrip('\n') + '.png'

    if name_text == '0.00.png':
        name_text='6.00.png'
    return name_text


def clean_folder():
    # 指定要删除的文件夹路径
    folder_path = 'screenshoot\\temp'

    # 获取文件夹中的所有文件列表
    file_list = os.listdir(folder_path)

    # 循环遍历文件列表
    for file_name in file_list:
        file_path = os.path.join(folder_path, file_name)
        # 使用os.remove()函数删除每个文件
        os.remove(file_path)


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
    rootdir = 'payment'

    # 修改截图文件名
    rename_files(rootdir)  # 可以把改名和获取路径合并为一个方法，要不然有重复部分

    # path = "water"
    # 获取文件路径
    file_paths = get_file_path(rootdir)
    print(file_paths)

    # 清理临时文件夹
    clean_folder()

    # 进行图片裁切
    cut_pic(file_paths)
