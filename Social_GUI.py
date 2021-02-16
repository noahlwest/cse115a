import os
import sys
import image_functions as img

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QImage, QPalette, QBrush


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(380, 470)
        MainWindow.setStatusTip("")

        #Background
        background = ""

        try:
            background = os.getcwd()
            background += "\\back2.png"
            if not os.path.exists(background):
                print(f"file path to {background} not found")
        except Exception as e:
            print(e)

        Image = QImage(background)
        #BackImage = Image.scaled(QSize(380,470))
        palette = QPalette()
        palette.setBrush(QPalette.Window, QBrush(Image))
        MainWindow.setPalette(palette)



        # Choose One Title
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.ChooseTitle = QtWidgets.QLabel(self.centralwidget)
        self.ChooseTitle.setGeometry(QtCore.QRect(240, 95, 111, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.ChooseTitle.setFont(font)
        self.ChooseTitle.setObjectName("ChooseTitle")
        self.ChooseTitle.setStyleSheet("color: #E7E7E7;")


        #Webcam Option
        self.WebCam = QtWidgets.QRadioButton(self.centralwidget)
        self.WebCam.setGeometry(QtCore.QRect(240, 140, 121, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.WebCam.setFont(font)
        self.WebCam.setObjectName("WebCam")
        self.WebCam.setChecked(True)
        self.WebCam.setStyleSheet("color: #E7E7E7;")


        #Video Option
        self.Video = QtWidgets.QRadioButton(self.centralwidget)
        self.Video.setGeometry(QtCore.QRect(240, 160, 82, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.Video.setFont(font)
        self.Video.setObjectName("Video")
        self.Video.setStyleSheet("color: #E7E7E7;")


        #Social Distance Detector Title
        self.Title = QtWidgets.QLabel(self.centralwidget)
        self.Title.setGeometry(QtCore.QRect(10, 0, 271, 81))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(20)
        self.Title.setFont(font)
        self.Title.setObjectName("Title")
        self.Title.setStyleSheet("color: #E7E7E7;")


        #Height input box
        self.HeightIn = QtWidgets.QLineEdit(self.centralwidget)
        self.HeightIn.setGeometry(QtCore.QRect(10, 140, 113, 20))
        self.HeightIn.setObjectName("HeightIn")
        self.HeightIn.setPlaceholderText("9 (DEFAULT)")

        self.HeightIn.setStyleSheet(
                                    "border :2px solid #555;"
                                    "border-top-left-radius :35px;"
                                    "border-top-right-radius : 35px; "
                                    "border-bottom-left-radius : 35px; "
                                    "border-bottom-right-radius : 35px;"
                                    "border-style: outset")

        #Angle Input Box
        self.AngleIn = QtWidgets.QLineEdit(self.centralwidget)
        self.AngleIn.setGeometry(QtCore.QRect(10, 190, 113, 20))
        self.AngleIn.setObjectName("AngleIn")
        self.AngleIn.setPlaceholderText("90 (DEFAULT)")
        self.AngleIn.setStyleSheet(
                                    "border :2px solid #555;"
                                    "border-top-left-radius :35px;"
                                    "border-top-right-radius : 35px; "
                                    "border-bottom-left-radius : 35px; "
                                    "border-bottom-right-radius : 35px;"
                                    "border-style: outset")

        #Field of View Hor Input Box
        self.FOV_H_In = QtWidgets.QLineEdit(self.centralwidget)
        self.FOV_H_In.setGeometry(QtCore.QRect(10, 260, 113, 20))
        self.FOV_H_In.setObjectName("FOV_H_In")
        self.FOV_H_In.setPlaceholderText("90 (DEFAULT)")
        self.FOV_H_In.setStyleSheet(
                                    "border :2px solid #555;"
                                    "border-top-left-radius :35px;"
                                    "border-top-right-radius : 35px; "
                                    "border-bottom-left-radius : 35px; "
                                    "border-bottom-right-radius : 35px;"
                                    "border-style: outset")

        #Field of View Ver Input Box
        self.FOV_V_In = QtWidgets.QLineEdit(self.centralwidget)
        self.FOV_V_In.setGeometry(QtCore.QRect(10, 330 , 113, 20))
        self.FOV_V_In.setObjectName("FOV_V_In")
        self.FOV_V_In.setPlaceholderText("110 (DEFAULT)")
        self.FOV_V_In.setStyleSheet(
                            "border :2px solid #555;"
                            "border-top-left-radius :35px;"
                            "border-top-right-radius : 35px; "
                            "border-bottom-left-radius : 35px; "
                            "border-bottom-right-radius : 35px;"
                            "border-style: outset")

        #Required Input Title
        #self.ReqiuredIn = QtWidgets.QLabel(self.centralwidget)
        #self.ReqiuredIn.setGeometry(QtCore.QRect(10, 80, 151, 31))
        #font = QtGui.QFont()
        #font.setFamily("Times New Roman")
        #font.setPointSize(18)
        #self.ReqiuredIn.setFont(font)
        #self.ReqiuredIn.setObjectName("ReqiuredIn")

        #Height Title
        self.HeightTitle = QtWidgets.QLabel(self.centralwidget)
        self.HeightTitle.setGeometry(QtCore.QRect(10, 120, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.HeightTitle.setFont(font)
        self.HeightTitle.setObjectName("HeightTitle")
        self.HeightTitle.setStyleSheet("color: #E7E7E7;")
       

        #Angle Title
        self.AngleTitle = QtWidgets.QLabel(self.centralwidget)
        self.AngleTitle.setGeometry(QtCore.QRect(10, 170, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.AngleTitle.setFont(font)
        self.AngleTitle.setObjectName("AngleTitle")
        self.AngleTitle.setStyleSheet("color: #E7E7E7;")

        #Field of View Hor Title
        self.FOV_H_Title = QtWidgets.QLabel(self.centralwidget)
        self.FOV_H_Title.setGeometry(QtCore.QRect(10, 220, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.FOV_H_Title.setFont(font)
        self.FOV_H_Title.setObjectName("FOV_H_Title")
        self.FOV_H_Title.setStyleSheet("color: #E7E7E7;")


        #Field of View Ver Title
        self.FOV_V_Title = QtWidgets.QLabel(self.centralwidget)
        self.FOV_V_Title.setGeometry(QtCore.QRect(10, 290, 131, 40))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.FOV_V_Title.setFont(font)
        self.FOV_V_Title.setObjectName("FOV_V_Title")
        self.FOV_V_Title.setStyleSheet("color: #E7E7E7;")


        #Distance Options title
        self.DistanceTitle = QtWidgets.QLabel(self.centralwidget)
        self.DistanceTitle.setGeometry(QtCore.QRect(240, 220, 131, 26))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        self.DistanceTitle.setFont(font)
        self.DistanceTitle.setObjectName("DistanceTitle")
        self.DistanceTitle.setStyleSheet("color: #E7E7E7;")


        #Audio Alert Check Box
        self.AudioCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.AudioCheck.setGeometry(QtCore.QRect(240, 250, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.AudioCheck.setFont(font)
        self.AudioCheck.setObjectName("AudioCheck")
        self.AudioCheck.setStyleSheet("color: #E7E7E7;")


        #Screen Shot Check Box
        self.ScreenCheck = QtWidgets.QCheckBox(self.centralwidget)
        self.ScreenCheck.setGeometry(QtCore.QRect(240, 280, 101, 17))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        self.ScreenCheck.setFont(font)
        self.ScreenCheck.setObjectName("ScreenCheck")
        self.ScreenCheck.setStyleSheet("color: #E7E7E7;")


        #Start Button
        self.StartButton = QtWidgets.QPushButton(self.centralwidget)
        self.StartButton.setGeometry(QtCore.QRect(140, 370, 101, 41))
        # self.StartButton.setGeometry(140, 370, 101, 41)
        self.StartButton.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        self.StartButton.setFont(font)
        self.StartButton.setObjectName("StartButton")
        self.StartButton.setStyleSheet(
                                        "color: white;"
                                        "background-color: #343434; "
                                        "border : 4px solid #555;"
                                        "border-top-left-radius : 35px;"
                                        "border-top-right-radius : 35px; "
                                        "border-bottom-left-radius : 35px; "
                                        "border-bottom-right-radius : 35px;"
                                        "border-style: outset")
                                        
        
        self.StartButton.clicked.connect(self.show_popup)
        #MenuBar and Menu functions - might delete
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 392, 21))
        self.menubar.setObjectName("menubar")
        self.menuFIle = QtWidgets.QMenu(self.menubar)
        self.menuFIle.setObjectName("menuFIle")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        self.actionExit.setFont(font)
        self.actionExit.setObjectName("actionExit")
        self.menuFIle.addAction(self.actionExit)
        self.menubar.addAction(self.menuFIle.menuAction())

        # Main Window call connection. See retranslateUi function below
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ChooseTitle.setText(_translate("MainWindow", "Choose One"))
        self.WebCam.setText(_translate("MainWindow", "Webcam (Default)"))
        self.Video.setText(_translate("MainWindow", "Video"))
        self.Title.setText(_translate("MainWindow", "Social Distance Detector"))
        #self.ReqiuredIn.setText(_translate("MainWindow", "Required Input"))
        self.HeightTitle.setText(_translate("MainWindow", "Height (Feet)"))
        self.AngleTitle.setText(_translate("MainWindow", "Angle (Degree)"))
        self.FOV_H_Title.setText(_translate("MainWindow", "Field Of View\nHorizontal (Degree)"))
        self.FOV_V_Title.setText(_translate("MainWindow", "Field Of View\nVertical (Degree)"))
        self.DistanceTitle.setText(_translate("MainWindow", "Distance Options"))
        self.AudioCheck.setText(_translate("MainWindow", " Audio Alert"))
        self.ScreenCheck.setText(_translate("MainWindow", "Screen Shots"))
        self.StartButton.setText(_translate("MainWindow", "Start"))

        # self.StartButton.setStyleSheet('QPushButton {background-color: #343434; color: white;}')

        self.menuFIle.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit The Program"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+E"))

    def show_popup(self):
        height = 9
        angle = 90
        fov_h = 90
        fov_v = 110
        
        # Dummy variables for the otherboxes on GUI --
        webCheck = self.WebCam.isChecked()
        audioAlert = self.AudioCheck.isChecked()
        screenShots = self.ScreenCheck.isChecked()

        #If a value is entered, put it into correspounding value
        #If no value entered keep the default

        # we can now accept float values instead of int only
        if  ( not isinstance(int(float(self.HeightIn.text())), int) or not isinstance(float(self.HeightIn.text()), float)) and bool(self.HeightIn.text()):
            height = -1
        elif bool( self.HeightIn.text() ):
            height = float(self.HeightIn.text())
        
        if ( not isinstance(int(float(self.AngleIn.text())), int) or not isinstance(float(self.AngleIn.text()), float )) and bool(self.AngleIn.text()):
            angle = -1
        elif bool(self.AngleIn.text()):
            angle = float(self.AngleIn.text())
        
        if ( not isinstance(int(float(self.FOV_H_In.text())), int) or not isinstance(float(self.FOV_H_In.text()), float) ) and bool(self.FOV_H_In.text()):
            fov_h = -1
        elif bool(self.FOV_H_In.text()):
            fov_h = float(self.FOV_H_In.text())

        if ( not isinstance(int(float(self.FOV_V_In.text())), int) or not isinstance(float(self.FOV_V_In.text()), float) ) and bool(self.FOV_V_In.text()):
            fov_v = -1
        elif bool(self.FOV_V_In.text()):
            fov_v = float(self.FOV_V_In.text())

        #Test valuess
        #print ("%d, %d, %d, %d\n", height, angle, fov_v, fov_h)

        #If a INVLAID value, throw a pop up error message
        #Else link code below
        if(height < 0.0 or height > 200.0 or angle < 0.0 or angle > 90.0  or \
           fov_h  < 0.0 or fov_h  > 359.0 or fov_v < 0.0 or fov_v > 359.0 ):
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Invalid value(s) entered")
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText("All values must be numbers and cannot be empty\n\nHeight must be in the range 0 to 200 feet\n\nAngle must be in the range 0 to 90 degrees\n\nField of Views must be in the range 0 to 360 degrees ")
            x = msg.exec_()
        else:
            # MainWindow.showMinimized()
            img.init_opencv()
            img.start_human_detection_loop(height, angle, fov_h, fov_v, webCheck, audioAlert, screenShots)
            img.stop_opencv()



def start_gui():
    print("Starting program...")
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


