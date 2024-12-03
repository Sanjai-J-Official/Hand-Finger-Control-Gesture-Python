import time
import cv2
 


class fpscls:
    def __inti__(self):
        pass
         

    
    def fpsFun(self,img,fps):

        cv2.putText(img,str(f"Fps:{int(fps)}"),(400,40),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),3)
        
        return img
    


cls=fpscls()      
def main():
    ptime=0
    cap=cv2.VideoCapture(0)
    
    
    while True:
        istrue ,img=cap.read()

        ctime=time.time()
        fps=1/(ctime-ptime)
        ptime=ctime
        img=cls.fpsFun(img,fps)

     
        
  

        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            cv2.destroyAllWindows()
            break
        


if __name__=="__main__":
    main()

