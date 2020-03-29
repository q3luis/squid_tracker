'''
Utils for load video, use OpenCV
Transform image use numpy for better track squid
'''

import cv2
import numpy as np


def get_video(path):
    '''

    :param path: path video
    :return: cap,fps : cap(stream video) ,fps(frame por seconds)
    '''

    cap = cv2.VideoCapture(path)
    if (cap.isOpened()== False):
        raise("  error vide no abierto")

    fps = cap.get(cv2.CAP_PROP_FPS)


    return cap, fps





