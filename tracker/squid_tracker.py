'''
Main class for tracker squid

'''

from tracker import *
from load_video import *
from output_utils import *


def squid_tracker(path):
    # Load video
    cap, fps = get_video(path)

    print(f" fps {fps}")

    ret, frame = cap.read()

    tracker, bbox = get_tracker(frame)

    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret:
            succes, box = tracker_image(tracker, frame)

            show_image_box(frame, bbox, box)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()

cv2.destroyAllWindows()