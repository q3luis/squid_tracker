'''
Main class for tracker squid

'''

from tracker import *
from load_video import *
from output_utils import *
from input_utils import *
from metrics import Metrics

import cv2

'''
Dividimos el proceso en varias fases una de navegación donde podemos seleccionar el trozo del video
que queremos trackear y otra la de trackeo.
En la primera fase solo visualizamos el video y damos la opción de movernos en el video
Lo hacemos de una forma facil, simplemente un bucle que se dedique a recorrer y visualizar el video

'''

def squid_tracker(path):

    cap, fps = get_video(path)
    ret, frame = cap.read()
    time_exp = -1
    count_track = 0
    array_metrics = []

    print(f" fps {fps}")

    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret:
            if len(array_metrics)>0 and array_metrics[-1].calculate_time()<time_exp:
                succes, box = tracker_image(tracker, frame)
                metric.update(box)
                show_image_box(frame, bbox, box)

            else:
                show_image(frame,cap)

        k = cv2.waitKey(25)
        if k == ord('q'):
            break
        if k == ord('g'):
            print("input frame number")
            n_number = int(input())
            cap.set(cv2.CAP_PROP_POS_FRAMES, n_number)

        if k == ord('t'):
            print("input frame number")
            n_number = int(input())
            print("input time exp in seg ")
            time_exp = int(input())
            cap.set(cv2.CAP_PROP_POS_FRAMES, n_number)
            ret, frame = cap.read()
            if ret:
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



def squid_tracker_old(path):
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
