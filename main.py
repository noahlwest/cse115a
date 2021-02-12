from Social_GUI import start_gui
from os import system, environ


def suppress_qt_warnings():
    environ["QT_DEVICE_PIXEL_RATIO"]       = "0"
    environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"
    environ["QT_SCREEN_SCALE_FACTORS"]     = "1"
    environ["QT_SCALE_FACTOR"]             = "1"


if __name__ == "__main__":
    # clears the console
    system("cls")
    
    # suppress warnings on Rory's computer
    suppress_qt_warnings()

    # starts the gui
    start_gui()
