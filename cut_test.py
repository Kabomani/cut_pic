# 导入相关包
import cv2

# import numpy as np
img = cv2.imread('originPic/test.PNG')
print(img.shape) # Print image shape
# cv2.imshow("original", img)
# 裁剪图像
# cropped_image = img[80:280, 150:330]
cropped_image = img[300:1525, 80:1230]
# 显示裁剪图像
cv2.imshow("cropped", cropped_image)
# 保存裁剪图像
cv2.imwrite('screenshoot/Cropped Image.jpg', cropped_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
