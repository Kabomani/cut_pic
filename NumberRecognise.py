# 引入库
import easyocr
#设置要识别繁体中文和英文两种语言
reader = easyocr.Reader(['ch_sim']) #如果不用gpu可以设gpu=False
#设置要识别的图片
result = reader.readtext('croppedPic/图片1.jpg')
#打印识别结果
print(result)