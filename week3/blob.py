import cv2 as cv
import numpy as np

def disp(imgs,x,y):
    h = max([img.shape[0] for img in imgs])
    w = max([img.shape[1] for img in imgs])
    comb = np.zeros((h*y,w*x,3))
    for i in range(min(len(imgs),x*y)):
        x1, y1 = w*(i//x), h*(i%y)
        x2, y2 = x1 + imgs[i].shape[0], y1 + imgs[i].shape[1]
        comb[x1:x2, y1:y2, 0:3] = imgs[i]
    comb = cv.resize(comb,dsize=None,fx=1/max(x,y),fy=1/max(x,y))
    cv.imshow('disp',comb)
    cv.waitKey(0)

filepath1 = "./images/polka_dots_1.png"
filepath2 = "./images/polka_dots_2.jpg"

img = cv.imread(filepath2)

b,g,r = cv.split(img)
def process(img):
    cv.imshow('img',img)
    blur = cv.GaussianBlur(img,(5,5),0)
    dst = cv.convertScaleAbs(cv.Laplacian(blur, cv.CV_16S, ksize=3))
    blur2 = cv.GaussianBlur(dst,(17,17),0)
    eq = cv.equalizeHist(blur2)
    cv.imshow('eq',eq)
    cv.waitKey(0)
    return eq

merged = cv.merge((process(b),process(g),process(r)))
cv.imshow('merge', merged)
cv.waitKey(0)
