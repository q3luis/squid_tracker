'''

File for control key imput

'''

import cv2
import numpy as np


def get_we_he_name():

    print("input weight in cm ")
    weight_size = float(input())
    print("input height in cm ")
    height_size = float(input())
    print("introduce el nombre del experimento ")
    exp_name = str(input())

    print(f" exp_name {exp_name} ,  weight {weight_size} , heigth  {height_size} ")

    return exp_name,weight_size,height_size

