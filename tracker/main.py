import cv2
import numpy as np

from squid_tracker import *

DEFAULT_SIZE = (854, 480)

# GOPR0792


path = '/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/GOPR0807.LRV.mp4'
# path = "/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/vlc-record-2020-03-21-18h10m29s-GOPR0823.MP4-.mp4"

# path  =  '/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/GOPR0792.mp4'

# path  =  '/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/GOPR0830.mp4'

import argparse


def get_parser():

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-path",required=True,type=str)
    return parser

def main():
    parse =get_parser().parse_args()

    print(f" video path {parse.path}")
    squid_tracker(parse.path)


if __name__ == '__main__':
    main()
