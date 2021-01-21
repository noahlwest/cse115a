import calibration


def gui_get_calibration_info():
    print("[+] getting calibration info")
    height = calibration.get_height()
    angle = calibration.get_angle()
    fov = calibration.get_fov()
    print("[+] returning calibration info")

    return height, angle, fov


def display_gui_calibration():
    print("[+] GUI showing")
    print("[+] GUI closed")
    return gui_get_calibration_info()

