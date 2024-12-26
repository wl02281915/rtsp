import threading, cv2, time, sys
from queue import Queue
from ultralytics import YOLO
cap3 = cv2.VideoCapture('')


#cv2.namedWindow('test3', cv2.WINDOW_AUTOSIZE)
#cv2.resizeWindow('test3',640,640)
frame_ = 0
start_time = fps_time = time.time()
fps_ = 0
model = YOLO("yolo11n.pt")
q = Queue()

def get_rtsp() :
    global frame3
    global frame_
    print('rtsp start')
    while cap3.isOpened():
        frame_+=1
        ret3, frame3 = cap3.read()
        #frame3 = cv2.resize(frame3,(640,640))

def inference() :
    global annotated_frame
    while cap3.isOpened():
        print(frame_)
        results = model.predict(source=frame3,save=False,save_txt=False,imgsz=(640,640),conf=0.5)
        annotated_frame = results[0].plot()
        q.put(annotated_frame)

if __name__ == '__main__':
    t1 = threading.Thread(target = get_rtsp)
    t1.start()
    time.sleep(5)
    t2 = threading.Thread(target = inference)
    t2.start()
    while True:
        try:
            item = q.get(block=False)
        except Exception as e:
            keycode = cv2.waitKey(20)
            if keycode & 0xFF == ord('q'):
                break
            continue

        if type(item) == int:
            break

        if type(item) == type(0):
            break
        item = cv2.resize(item,(1080,920))
        cv2.imshow('test', item)



    #time.sleep(5)
    #t2 = threading.Thread(target = inference)
    #t2.start()
    #time.sleep(3)

    item = q.get(block=False)
    cv2.imshow('test3', item)
    #print(item)

    t1.join()
    t2.join()
