import numpy as np
import cv2
import math
import image_functions as img
import calibration as cal
import distance_functions as dist
import gui_functions as gui

if __name__ == "__main__":

    print("Starting program...")
    
    webcam = True
    img.init_opencv()

    height, angle, fov = gui.display_gui_calibration()
    
    img.start_human_detection_loop(height, angle, fov)

    img.stop_opencv()
