import gui_functions
import image_functions


def main():
    height, angle, fov = gui_functions.display_gui_calibration()
    image_functions.start_human_detection(height, angle, fov)


main()
