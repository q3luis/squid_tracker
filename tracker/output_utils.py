'''

utils for show images

'''

import cv2
import numpy


def plot_box(frame, bbox, box):
    '''
    :param frame: image
    :param bbox: original box, for calculate box size
    :param box: tracker box

    '''

    p1 = (int(box[0]), int(box[1]))
    p2 = (int(box[0] + bbox[2]), int(box[1] + bbox[3]))
    cv2.rectangle(frame, p1, p2, (0, 255, 0), 2, 1)


def show_image_box(frame, bbox, box):
    '''
    :param frame: image
    :param bbox: original box, for calculate box size
    :param box: tracker box

    '''
    plot_box(frame, bbox, box)

    cv2.imshow('Frame',frame)
