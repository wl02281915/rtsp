import cv2, time

cap3 = cv2.VideoCapture('')
count_ = 0
start_time = fps_time = time.time()

while cap3.isOpened():
    count_ += 1
    ret3, frame3 = cap3.read()
    frame_time = int(start_time*1000+cap3.get(cv2.CAP_PROP_POS_MSEC))
    delay_time = int((time.time()*1000) - frame_time)
    frame3 = cv2.resize(frame3,(1080,720))
    cv2.imshow('test3', frame3)
    if count_ % 50 == 0 :
        print(f'fps = {int(50/(time.time()-fps_time))} '+ f'delay = {delay_time} ms')
        count_ = 0
        fps_time = time.time()
    if cv2.waitKey(1) == ord('q'):
        break
cap3.release()
cv2.destroyAllWindows()
