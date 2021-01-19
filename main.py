import numpy as np
import cv2
import math
import functions as fn

if __name__ == "__main__":

    cv2.startWindowThread()
    cap = cv2.VideoCapture(fn.get_videocapture_arg())
    fn.set_cap_height_and_width(cap, 1280, 720)

    while(True):

        ret, frame = cap.read()

        cv2.imshow('press q to exit', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
