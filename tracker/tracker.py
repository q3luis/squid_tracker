'''
File for crate and control tracker
'''

import cv2
import numpy as np


def inverse_color_img(frame, th=20):
    # image = image.copy()
    grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    idx1 = np.where(grayImage > th)
    grayImage[:, :] = 0
    grayImage[idx1] = 255.0

    return grayImage

def get_tracker(frame):
    bbox = cv2.selectROI(frame, False)

    blackAndWhiteImage = inverse_color_img(frame)

    tracker = cv2.TrackerMIL_create()

    ok = tracker.init(blackAndWhiteImage, bbox)

    return tracker,bbox


def tracker_image(tracker, frame):
    blackAndWhiteImage = inverse_color_img(frame)
    (success, box) = tracker.update(blackAndWhiteImage)

    return success, box
