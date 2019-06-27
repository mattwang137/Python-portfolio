#!/usr/bin/python3
#encoding:utf-8

import numpy as np
import cv2,os,dlib

"""
Develop Subject: python-opencv-face-detection
Developer: Matt Wang
Python environment: version 3.6
"""

def faceDetection():

    cap=cv2.VideoCapture(0)
    detector=dlib.get_frontal_face_detector()

    p=1

    if not os.path.exists("faceDetection"):
        os.mkdir("faceDetection")
    mypath = "./faceDetection/"
    files = os.listdir(mypath)
    fn=len(files)

    while(cap.isOpened()):
        try:
            ret , frame = cap.read()
            # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            face_rects=detector(frame,0)
            for i, d in enumerate(face_rects):
                x1=d.left()
                y1=d.top()
                x2=d.right()
                y2=d.bottom()

                cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),4)
            if ret==True:
                cv2.imshow("Press 'z' to take a picture of face or press 'q' to exit",frame)
                k=cv2.waitKey(1)
                if k==ord("q"):
                    cap.release()
                    cv2.destroyAllWindows()
                    break
                if k==ord("z") or k==ord("Z"): # press z to take a picture
                    if fn==0:
                        crop_frame = frame[y1:y2, x1:x2]
                        cv2.imwrite("faceDetection\\face"+str(p)+".jpg",crop_frame)
                        p=p+1
                    else:
                        fn+=1
                        crop_frame = frame[y1:y2, x1:x2]
                        cv2.imwrite("faceDetection\\face"+str(fn)+".jpg",crop_frame)
            else:
                cap.release()
                cv2.destroyAllWindows()
                break

        except:
            cap.release()
            cv2.destroyAllWindows()
            break
    cap.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    faceDetection()