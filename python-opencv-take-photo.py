#!/usr/bin/python3
#encoding:utf-8

import numpy as np
import cv2,os
"""
Develop Subject: python-opencv-take-photo
Developer: Matt Wang
Python environment: version 3.6
"""

def takePicture():

    cap = cv2.VideoCapture(0)

    if not os.path.exists("myPicture"):
        os.mkdir("myPicture")
    mypath = "./myPicture/"
    files = os.listdir(mypath)
    fn=len(files)

    p=1

    while(cap.isOpened()):
        ret , frame = cap.read()
        # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        cv2.imshow("Press 'z' to take a picture or press 'q' to exit",frame)
        k=cv2.waitKey(1)
        if k==ord("z") or k==ord("Z"): # take a picture
            if fn==0:
                cv2.imwrite("myPicture\\pic"+str(p)+".jpg",frame)
                p+=1
            else:
                fn+=1
                cv2.imwrite("myPicture\\pic"+str(fn)+".jpg",frame)
        if k==ord("q"):
            cap.release()
            cv2.destroyAllWindows()
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    takePicture()