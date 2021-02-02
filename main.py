import Social_GUI
import sys

def start_gui():
    print("Starting program...")
    app = Social_GUI.QtWidgets.QApplication(sys.argv)
    MainWindow = Social_GUI.QtWidgets.QMainWindow()
    ui = Social_GUI.Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())



if __name__ == "__main__":
    start_gui()

