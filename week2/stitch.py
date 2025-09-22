import cv2 as cv
import numpy as np

vid_path = "Minecraft_stitch_test.mp4"

vcap = cv.VideoCapture(vid_path)

def sift_all():
    stitcher = cv.Stitcher.create(cv.Stitcher_SCANS)
    frames = []
    s, f = vcap.read()
    i = 0
    while s:
        if not i%20: frames.append(f); #cv.imwrite(f"img{i}.png",f)
        s, f = vcap.read()
        #print(i := i+1)
    print(f"stitching {len(frames)} frames")
    status,out = stitcher.stitch(frames)
    print("done")
    if status == cv.Stitcher_OK:
        cv.imshow("out",out)
        cv.imwrite("stitch.png",out)
        cv.waitKey(0)
    else:
        print("error")
        sys.exit(-1)

sift_all()
