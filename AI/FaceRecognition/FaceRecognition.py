# !/usr/bin/python
# coding: utf8
# Time: 2020/4/27 18:26
# Author: Liam
# E-mail: luyu.real@qq.com
# Software: PyCharm
import cv2 as cv
image = cv.imread("cover.jpg")
cv.imshow("input image", image)
cv.waitKey(0)
cv.destroyAllWindows()

