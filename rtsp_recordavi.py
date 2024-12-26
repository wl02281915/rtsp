import threading, json, base64
from queue import Queue
import numpy as np
import time, cv2
cap = cv2.VideoCapture('')
cap.set(cv2.CAP_PROP_BUFFERSIZE,0)
frame_ = 0
q = Queue()


origin_fps = 15
inference_sleep_time = 1/origin_fps
delay_time = 0
rtsp_sleep_time = 0
buffer_frame = 200
wanted_delay = 5*1000


fourcc = cv2.VideoWriter_fourcc(*'XVID')
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
out = cv2.VideoWriter('output.avi', fourcc, fps, (frame_width, frame_height))
save_frame=0
while cap.isOpened():
    try :
        ret, frame = cap.read()
        out.write(frame)
        save_frame+=1
        print('save rtsp ! '+str(save_frame))
    except Exception as e:
        print('save_rtsp error : ' + str(e))
        continue

cap.release()
out.release()

