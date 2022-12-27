# MOST ACCURACY OVERALL WITH DETECTION AND COUNTER:--
from datetime import date, datetime
import cv2
import numpy as np
from time import sleep
import pymongo
import os
import time
# import random


new_client = pymongo.MongoClient('mongodb://localhost:27017')
new_db = new_client['DATA_TRY']
new_col = new_db['detection001']

length_min= 90 #Min length of a rectangle.
height_min=90 #Min heught of a rectangle.

offset=6#Contact line position.  
post_line = 550#Contact line position. 
# post_line2 = 550

delay= 60 #FPS of video

detect = []
counter= 0

	
def paste_centroid(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx,cy

cap = cv2.VideoCapture('video.mp4')
sub = cv2.createBackgroundSubtractorKNN()
while True:
    ret , frame1 = cap.read()
    tempo = float(1/delay)
    sleep(tempo) 
    grey = cv2.cvtColor(frame1,cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grey,(3,3),5)
    img_sub = sub.apply(blur)
    dilat = cv2.dilate(img_sub,np.ones((5,5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx (dilat, cv2. MORPH_CLOSE , kernel)
    dilatada = cv2.morphologyEx (dilatada, cv2. MORPH_CLOSE , kernel)
    contorno,h=cv2.findContours(dilatada,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    
    cv2.line(frame1, (25, post_line), (1200, post_line), (255,127,0), 3) 
    # cv2.line(frame1, (1100, post_line2), (700, post_line2), (255,127,0), 2) 

    for(i,c) in enumerate(contorno):
        (x,y,w,h) = cv2.boundingRect(c)
        validate_counter = (w >= length_min) and (h >= height_min)
        if not validate_counter:
            continue

        cv2.rectangle(frame1,(x,y),(x+w,y+h),(0,255,0),2)        
        centro = paste_centroid(x, y, w, h)
        detect.append(centro)
        cv2.circle(frame1, centro, 4, (0, 100,300), -1)
        
        
        for (x,y) in detect:
            if y<(post_line+offset) and y>(post_line-offset) :
                counter+=1
                cv2.line(frame1, (25, post_line), (1200, post_line), (0,127,255), 3)
                # cv2.line(frame1, (1100, post_line2), (700, post_line2), (0,127,255), 3)
                                
                detect.remove((x,y))
                   
                
                # print("Passed car out : "+str(counter2))
                print("PASSED CAR IN: "+str(counter))
                sec = datetime.utcnow().replace()
                print(sec)
                second = str(sec)
                print(second[11:19])
                new_dict = {"TOTAL NO OF CARS DETECTED:" : counter , "TIME": second[14:19]}
                adding = new_col.insert_one(new_dict)
                               
    cv2.putText(frame1, "VEHICLE COUNT IN : "+str(counter), (500, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),3)
    # cv2.putText(frame1, "VEHICLE COUNT OUT : "+str(counter2), (700, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 0),3)
    cv2.imshow("Video Original" , frame1)
    #cv2.imshow("Detectar",dilatada)
    # print(adding)
                          
                
    if cv2.waitKey(1) == 13:
        break
cv2.destroyAllWindows()
cap.release()
       