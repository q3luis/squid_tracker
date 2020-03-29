'''
Main class for tracker squid

'''

from tracker import *
from load_video import *
from output_utils import *
from input_utils import *
from metrics import Metrics


def squid_tracker(path):
    # Load video
    array_metrics = []
    cap, fps = get_video(path)

    print(f" fps {fps}")

    ret, frame = cap.read()

    tracker, bbox = get_tracker(frame)

    exp_name,weight_size,height_size= get_we_he_name()

    metric = Metrics(bbox, fps, exp_name,weight_size, height_size)

    array_metrics.append(metric)

    while (cap.isOpened()):

        ret, frame = cap.read()

        if ret:
            succes, box = tracker_image(tracker, frame)

            metric.update(box)

            show_image_box(frame, bbox, box)

        k = cv2.waitKey(25)
        if k == ord('q'):
            break
        if k == ord('r'):
            print(f" capture {k}  ")
            cv2.destroyAllWindows()
            tracker, bbox = get_tracker(frame)
            exp_name,weight_size,height_size= get_we_he_name()
            metric = Metrics(bbox, fps,exp_name,weight_size, height_size)

            array_metrics.append(metric)

    for i,metric_aux in enumerate(array_metrics):
        print(f" resumen metric {i} ")
        metric_aux.show()

    cap.release()


cv2.destroyAllWindows()
