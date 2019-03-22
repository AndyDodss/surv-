import cv2
from pyzbar import pyzbar

def func() :
    cap = cv2.VideoCapture(0)
    while True :
        _, frame = cap.read()

        decodedobjects = pyzbar.decode(frame)

        if decodedobjects != []:
            data = ''
            for obj in decodedobjects:
                   data = obj.data
                   break
            cap.release()
            cv2.destroyAllWindows()
            return data

        cv2.imshow("Frame",frame)

        key = cv2.waitKey(1)
        if key == 27 :
            break;
