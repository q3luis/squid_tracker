'''

Calculate distinct metrics for squid movements

'''
import numpy as np


class Metrics:

    def __init__(self, bbox, fps,exp_name,width_size,heigh_size):
        # prev bbox
        self.bbox = bbox
        print(f" bbox {bbox} ")
        self.dist_move = 0
        # frames por seconds utils for calculate dist/seconds
        self.fps = fps
        self.exp_name=exp_name
        # acumulator for frames utils for calculate dist/seconds
        self.num_frames = 0
        self.width_size = width_size
        self.heigh_size = heigh_size

        #real size in cm's
        self.pixel_w_s = self.width_size/self.bbox[2]
        self.pixel_h_s = self.heigh_size/self.bbox[3]


    def _calculate(self, box):

        x_p, y_p = self.bbox[:2]
        x, y, = box[:2]

        dist_x = np.abs(x_p - x)*self.pixel_w_s
        dist_y = np.abs(y_p - y)*self.pixel_h_s

        if dist_x != 0 and dist_y != 0:
            self.dist_move += np.sqrt((dist_x ** 2 + dist_y * 2))

        else:
            self.dist_move += dist_x
            self.dist_move += dist_y

    def _caculate_speed(self):
        t = self.num_frames/float(self.fps)

        return self.dist_move/t
    def calculate_time(self):

        return self.num_frames/float(self.fps)

    def update(self, box):
        '''
        Update box and metrics
        :param box:
        :return:
        '''

        self._calculate(box)
        self.bbox = box
        self.num_frames += 1

    def show(self):
        print("------------------------------------------")
        print(f"EXP NAME :  {self.exp_name}")
        print(f" num frames : {self.num_frames} ")
        print(f" distance : {self.dist_move} cm ")
        print(f" speed : {self._caculate_speed()}  cm/s ")
        print("------------------------------------------")
