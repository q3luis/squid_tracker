

import cv2
import numpy as np

DEFAULT_SIZE = (854,480 )

# GOPR0792



path  =  '/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/GOPR0807.LRV.mp4'
#path = "/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/vlc-record-2020-03-21-18h10m29s-GOPR0823.MP4-.mp4"

#path  =  '/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/GOPR0792.mp4'

#path  =  '/Users/luispeinado/workspaces/workspace_python/squid_tracker/data/GOPR0830.mp4'


cap = cv2.VideoCapture(path)

if (cap.isOpened()== False):
    print("  error vide no abiert")

tracker = cv2.Tracker_create('MIL')

ret, frame = cap.read()

frame = cv2.resize(frame,DEFAULT_SIZE)

grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



def inverse_color_img(image,th=20):
    print(image.shape)
    #image = image.copy()
    idx1= np.where(image > th)
    image[:,:] = 0
    image[idx1] = 255.0

    return image


def capture_box_size():

    txt =  cv2.waitKey(10)

    while(txt!=ord('q')):
        print(txt)
        txt = cv2.waitKey(10)






blackAndWhiteImage = inverse_color_img(grayImage)

#hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

bbox = cv2.selectROI(frame, False)

print(" bbox {} ".format(bbox))
print(" ret {} ".format(ret))

ok = tracker.init(blackAndWhiteImage, bbox)


capture_box_size()

while(cap.isOpened()):

    ret, frame = cap.read()

    #frame = cv2.resize(frame,DEFAULT_SIZE)




    if ret == True:
        ### track erf box
        frame = cv2.resize(frame,DEFAULT_SIZE)

        grayImage = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blackAndWhiteImage = inverse_color_img(grayImage)

        (success, box) = tracker.update(blackAndWhiteImage)
        print("box : {}".format(box))

        #if success:
            # Tracking success
        p1 = (int(box[0]), int(box[1]))
        p2 = (int(box[0] + bbox[2]), int(box[1] + bbox[3]))
        cv2.rectangle(frame, p1, p2, (0,255,0), 2, 1)

        cv2.imshow('Frame',frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):

            break

    else:
        print(" ret {} ".format(ret))




print("cap rel  {} ".format(cap.isOpened()))

cap.release()



cv2.destroyAllWindows()


