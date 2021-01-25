from cv2 import cv2
import sys, imutils
from skimage.filters import threshold_local
import numpy as np
import argparse
import imutils

import random as r


def doWork(filename, outputfolder):
    image1 = cv2.imread(filename)
    h, w = image1.shape[0:2]

    # Make border for easier crop
    image = cv2.copyMakeBorder(
        image1,
        30,
        30,
        30,
        30,
        cv2.BORDER_CONSTANT,
        value=(255,255,255)
    )
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (5, 5), 0)

    ret, th = cv2.threshold(gray, 210, 235, 1)

    cnts, hierarchy = cv2.findContours(th.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key=cv2.contourArea, reverse=True)

    best_contours = list()

    for c in cnts:
        box = cv2.minAreaRect(c)
        box = cv2.cv.BoxPoints(box) if imutils.is_cv2() else cv2.boxPoints(box)
        box = np.array(box, dtype="int")
        Area = image.shape[0] * image.shape[1]
        if Area / 10 < cv2.contourArea(box) < Area * 2 / 3:
            #print(box)
            best_contours.append(box)
            #cv2.drawContours(image, [box], -1, (0, 255, 0), 2)

    # image = cv2.resize(image, (960, 540))                    # Resize image

    i = 0
    fname = str(filename)
    p = fname.split("/")
    imgname = p[len(p)-1]
    imgname = imgname[:-4]
    for c in best_contours:
        # get the bounding rect
        x, y, w, h = cv2.boundingRect(c)

        path= outputfolder

        # Get individual file name
        imgname_i = str(imgname) + '_' + str(i)
        new_file_name = 'cropped{}.png'.format(imgname_i)

        # File name + directory
        new_file_name_path = path + new_file_name
        print(new_file_name_path)

        cv2.imwrite(new_file_name_path, image[y:y + h, x:x + w])
        i+=1


    #cv2.imshow("Image2", image2)
    #cv2.waitKey(0)
