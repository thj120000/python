#!@Author : Sanwat
#!@File : .py
import numpy as np
import cv2

img = cv2.imread("C:/picture/1.jpg")
cv2.namedWindow("wa",2)
cv2.imshow("wa",img)
cv2.waitKey(0)