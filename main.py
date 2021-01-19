import numpy as np
import cv2
import math
import image_functions as img
import calibration as cal
import distance_functions as dist
import gui_functions as gui

if __name__ == "__main__":

    img.hello_world()
    cal.hello_world()
    dist.hello_world()
    gui.hello_world()
    print("Starting program...")

    cv2.startWindowThread()
    cap = cv2.VideoCapture(img.get_videocapture_arg())
    img.set_cap_height_and_width(cap, 1280, 720)

    while(True):

        ret, frame = cap.read()

        cv2.imshow('press q to exit', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cv2.waitKey(1)
