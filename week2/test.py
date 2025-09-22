import cv2 as cv
import numpy as np

print(cv.__version__)
img = cv.imread("Figure2Submission.png")
cv.imshow("test",img)
k = cv.waitKey(0)
if k:
    print("winclose")
