# -*- coding = utf-8 -*-
# @Time:2023-11-09 22:13
# @Author:Mark
# @File:ocrDate.py
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


def file_classify(file_paths,save_root):
    for file_path in file_paths:
        print(file_path)
        route, filename = os.path.split(file_path)

        #生成保存路径
        root_dir, sub_path = route.split('\\', 1)

        img = cv2.imread(file_path)
        print(img.shape)  # Print image shape
        # cv2.imshow("original", img)

        # 裁剪日期部分
        # 裁剪图像
        # cropped_image = img[80:280, 150:330]
        cropped_image = img[705:1288, ]
        temp_route = 'screenshoot\\temp\\' + filename

        # 显示裁剪图像
        # cv2.imshow("cropped", cropped_image)
        cv2.imwrite(temp_route, cropped_image)

        # file_date,payamount = read_image(temp_route)
        # file_date,pre_filename = read_image(temp_route)
        # pre_filename = read_image(temp_route)
        text = read_image(temp_route)

        #将识别内容保存
        # exclude_char_list = ':\\|\'?!"[]()@#$%^&*<>/- ”“"'
        # text = ''.join([x for x in text if x not in exclude_char_list])
        content = text
        print(content)
        fp2 = open('screenshoot\\temp\\'+filename+'.txt', 'a')

        fp2.write(content.encode('utf-8').decode('utf-8'))
        fp2.close()

        # #创建裁剪文件目录
        # save_path= save_root+sub_path+'\\'+file_date
        # # 创建保存路径
        # if os.path.exists(save_path):  # 当文件夹存在时清空文件夹
        #     # shutil.rmtree(save_path, True)
        #     print('dir exist')
        # else:  # 当文件夹不存在时在当前路径下创建用于存放数据的文件夹
        #     os.makedirs(save_path)
        # # save_path =
        # # 保存裁剪图像
        # cv2.imwrite(save_path+'\\'+pre_filename+'.png', cropped_image)


        # cv2.imwrite('screenshoot\\number\\' + file_text, cropped_image)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()


def read_image(route):
    img = Image.open(route)
    # text = pytesseract.image_to_string(img, lang='chi_sim', config='digits')
    text = pytesseract.image_to_string(img, lang='chi_sim')

    print(text)
    # text = text.rstrip('\n')
    # file_date, pre_filename = generate_date(text)

    # name_text = text.replace("-", "").rstrip('\n') + '.png'

    # if name_text == '0.00.png':
    #     name_text = '6.00.png'
    return text
    # return file_date,pre_filename


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


def generate_date(text):
    import datetime
    date_str = text
    # date_str = text[:-6]
    date_format = "%Y%m%d%H%M%S"
    datetime_object = datetime.datetime.strptime(date_str, date_format)
    year = datetime_object.year
    month = datetime_object.month
    day = datetime_object.day
    hour = datetime_object.hour
    minute = datetime_object.minute
    second = datetime_object.second

    date_dir_name = str(year) + '-' + str(month) + '-' + str(day)
    payment_time = str(hour) + '-' + str(minute)
    print(date_dir_name)
    print(payment_time)
    # year = text[0:4]
    # month = text[4:6]
    # day = text[6:8]
    # hour = text[8:10]
    # minute = text[10:12]
    # second = text[12:14]
    from dateutil.parser import parse

    # a = 20170825
    # b = str(a)
    # pic_date = parse(text)

    # print(date)
    return date_dir_name, payment_time


if __name__ == '__main__':
    rootdir = 'readyToCut'
    save_root = 'screenshoot'

    # 修改截图文件名
    # rename_files(rootdir)  # 可以把改名和获取路径合并为一个方法，要不然有重复部分

    # path = "water"
    # 获取文件路径
    file_paths = get_file_path(rootdir)
    print(file_paths)

    # 清理临时文件夹
    clean_folder()

    # 进行图片日期识别并修改文件名为日期
    # 将图片日期部分裁切出来进行识别
    file_classify(file_paths,save_root)
    # cut_date(file_paths)
