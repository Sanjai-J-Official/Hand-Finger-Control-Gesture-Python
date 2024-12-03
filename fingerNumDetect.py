import cv2
import os
import fps 
import time
import sys
s=sys.path.append(os.path.abspath("../"))
 
from handTrack.handtrackingmodule import handDetetor
cap=cv2.VideoCapture(0)

folderpath="images"
dir=os.listdir(folderpath)
overlayList=[]
for imgdir in dir:
    image=cv2.imread(f"{folderpath}/{imgdir}")
    overlayList.append(image)
img_overlay=[]
for i in overlayList:
    resize_overlay=cv2.resize(i,(100,200))
    img_overlay.append(resize_overlay)


detetor=handDetetor()
cls=fps.fpscls()
ptime=0
count=0

tipfinger=[4,8,12,16,20]
while True:

    success ,img= cap.read()
  
    
    
    img=detetor.findHands(img)
    posis=detetor.findposition(img,draw=True)
    

    
    

    
    ctime=time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    img=cls.fpsFun(img,fps)
    

    if len(posis) != 0:
        fingers=[]

        if posis[tipfinger[0]][1] < posis[tipfinger[0]-1][1]:
                fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):

            if posis[tipfinger[id]][2] < posis[tipfinger[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)
        
        totalfinger=fingers.count(1)
        print(totalfinger)
        img[0:200,0:100]=img_overlay[totalfinger-1]
    cv2.imshow("hand img",img)

        
    
    if cv2.waitKey(1) & 0xFF==ord("q"):
        cv2.destroyAllWindows()
        break
cap.release()
cv2.destroyAllWindows()
