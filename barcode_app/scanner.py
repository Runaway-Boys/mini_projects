import cv2
from pyzbar.pyzbar import decode
import time

cam = cv2.VideoCapture(0)
cam.set(3,640) 
cam.set(4,480)
used_codes=[]
webcam = True
while webcam == True:
    success, frame = cam.read()

    for bar_code in decode(frame):

        if bar_code.data.decode('utf-8') not in used_codes:
            print('approved')
            print(bar_code.data.decode('utf-8'))
            used_codes.append(bar_code.data.decode('utf-8'))
            time.sleep(5)
                #stops too many readings of the same barcode
        elif bar_code.data.decode('utf-8')  in used_codes:
            print('already in ')
            time.sleep(5)  
        else:
            pass
    cv2.imshow("code_scanner",frame)
    cv2.waitKey(1)

    
