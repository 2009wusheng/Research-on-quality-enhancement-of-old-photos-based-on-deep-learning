# 这是一个示例 Python 脚本。

# 按 Shift+F10 执行或将其替换为您的代码。
# 按 双击 Shift 在所有地方搜索类、文件、工具窗口、操作和设置。


import cv2
from matplotlib import pyplot as plt
import numpy as np


img_path = "C:/Users/60432\Desktop/biyesheji/tuihua/img/1.jpg"
image = cv2.imread(img_path)
print(image.shape)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
alpha = np.ones((*image.shape[:2], 1), dtype=np.uint8) * 255
image_alpha = np.concatenate((image, alpha), axis=2)
 # the following image can be changed to image_gray or image_alpha
blur_image = cv2.GaussianBlur(image, ksize=(5, 5), sigmaX=1, sigmaY=1)
cv2.imshow('original_image', image)
cv2.imshow('gaussian_blur_image', blur_image)

cv2.imwrite('C:/Users/60432\Desktop/biyesheji/tuihua/img/1-result.jpg', blur_image)
cv2.waitKey(0)
cv2.destroyAllWindows()