import cv2 as cv
import os

path = "./screenshoot/10.16-10.25"
for path, directory, file in os.walk(path):
    # print(path)
    # print(directory)
    # print(file)
    break
# filelist = next(os.walk(path))[2]
# pic = []
# for i in file:
# if (".png" in i):
#     pic.append(i)
# pic.append(i)
# for j in pic:
#   read_image(path,j)


# 加载图片
for i in file:
    # image = cv.imread('pic/test.PNG')
    filename = path + '/' + i
    image = cv.imread(filename)

    # 获取图像尺寸
    height, width, channels = image.shape

    fixed_width = 277
    fixed_height = int(277 / width * height)

    # new_image = cv.resize(image, (0,0), fx=0.25, fy=0.25, interpolation=cv.INTER_AREA)
    new_image = cv.resize(image, dsize=(fixed_width, fixed_height), interpolation=cv.INTER_AREA)
    # cv.imwrite("resizedImage_pmm.jpg", new_image)
    cv.imwrite('./croppedPic' + '/' + i, new_image)
    # 裁剪图像
    # cropped_image = new_image[75:365, 23:300]
    # 显示裁剪图像
    # cv.imshow("cropped", cropped_image)
    # 保存裁剪图像
    # cv.imwrite('./croppedPic' + '/' + i, cropped_image)
