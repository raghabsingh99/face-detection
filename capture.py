from datetime import datetime
import cv2 , time

from cv2 import threshold

first_frame=None

status_list=[None,None]
times=[]

vide0= cv2.VideoCapture(0)


while True:
    check, frame = vide0.read()
    status=0

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray=cv2.GaussianBlur(gray,(21,21),0)
    
    if first_frame is None:
        first_frame=gray
        continue
    status=1

    delta_frame=cv2.absdiff(first_frame,gray)
    thres_delta=cv2.threshold(delta_frame,30,255,cv2.THRESH_BINARY)[1]

    thres_frame=cv2.dilate(thres_delta, None,iterations=2)

    (cont,_)= cv2.findContours(thres_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    

    for contour in cont:
        if cv2.contourArea(contour)<1000:
            continue
        status=1

        (x,y,w,h)= cv2.boundingRect(contour)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),3)

    status_list.append(status)
    if status_list[-1]==1 and status_list[-2]==0:
       times.append(datetime.now()) 

    if status_list[-1]==0 and status_list[-2]==1:
       times.append(datetime.now()) 



    cv2.imshow("gray frame",gray)
    cv2.imshow("delta_frame", delta_frame)
    cv2.imshow("threshold frame",thres_frame)
    cv2.imshow("color frame", frame)

    

    key=cv2.waitKey(1)
    print(gray)
    print(delta_frame)

    if key==ord('q'):
        if status==1:
            times.append(datetime.now())
        break

print(status_list)


vide0.release()
cv2.destroyAllWindows


