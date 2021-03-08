import platform
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
import image_functions as img
import files_rc
import os

class Ui_MainWindow(object):
    # Input:       a MainWindow created by PyQt5/PySide
    # Output:      none
    # Description: Sets up the UI for the first time on load up
    def setupUi(self, MainWindow) -> None:

        #MAIN WINDOW FUNCTIONS
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(953, 836)

        #FONT FOR MAIN WINDOW
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet("QMainWindow {background: transparent; }\n"
"QToolTip {\n"
"    color: #ffffff;\n"
"    background-color: rgba(27, 29, 35, 160);\n"
"    border: 1px solid rgb(40, 40, 40);\n"
"    border-radius: 2px;\n"
"}")
        #CENTRAL WIDGET
        self.central_widget = QtWidgets.QWidget(MainWindow)
        self.central_widget.setStyleSheet("background: transparent;\n"
"color: rgb(210, 210, 210);")
        self.central_widget.setObjectName("central_widget")
        self.grid_layout_2 = QtWidgets.QGridLayout(self.central_widget)
        self.grid_layout_2.setContentsMargins(10, 10, 10, 10)
        self.grid_layout_2.setObjectName("grid_layout_2")
        self.frame_main = QtWidgets.QFrame(self.central_widget)
        self.frame_main.setStyleSheet("/* LINE EDIT */\n"
"QLineEdit {\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding-left: 10px;\n"
"}\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QLineEdit:focus {\n"
"    border: 2px solid rgb(91, 101, 124);\n"
"}\n"
"\n"
"/* SCROLL BARS */\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"    border-radius: 0px;\n"
"}\n"
"QScrollBar::handle:horizontal {\n"
"    background: rgb(85, 170, 255);\n"
"    min-width: 25px;\n"
"    border-radius: 7px\n"
"}\n"
"QScrollBar::add-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-right-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"    subcontrol-position: right;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::sub-line:horizontal {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"    width: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-bottom-left-radius: 7px;\n"
"    subcontrol-position: left;\n"
"    subcontrol-origin: margin;\n"
"}\n"
"QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
"QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal\n"
"{\n"
"     background: none;\n"
"}\n"
" QScrollBar:vertical {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"    border-radius: 0px;\n"
" }\n"
" QScrollBar::handle:vertical {    \n"
"    background: rgb(85, 170, 255);\n"
"    min-height: 25px;\n"
"    border-radius: 7px\n"
" }\n"
" QScrollBar::add-line:vertical {\n"
"     border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-bottom-left-radius: 7px;\n"
"    border-bottom-right-radius: 7px;\n"
"     subcontrol-position: bottom;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::sub-line:vertical {\n"
"    border: none;\n"
"    background: rgb(55, 63, 77);\n"
"     height: 20px;\n"
"    border-top-left-radius: 7px;\n"
"    border-top-right-radius: 7px;\n"
"     subcontrol-position: top;\n"
"     subcontrol-origin: margin;\n"
" }\n"
" QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
" QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
"     background: none;\n"
" }\n"
"\n"
"/* CHECKBOX */\n"
"QCheckBox::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QCheckBox::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"    background: 3px solid rgb(52, 59, 72);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"    background-image: url(:/16x16/icons/16x16/cil-check-alt.png);\n"
"}\n"
"\n"
"/* RADIO BUTTON */\n"
"QRadioButton::indicator {\n"
"    border: 3px solid rgb(52, 59, 72);\n"
"    width: 15px;\n"
"    height: 15px;\n"
"    border-radius: 10px;\n"
"    background: rgb(44, 49, 60);\n"
"}\n"
"QRadioButton::indicator:hover {\n"
"    border: 3px solid rgb(58, 66, 81);\n"
"}\n"
"QRadioButton::indicator:checked {\n"
"    background: 3px solid rgb(94, 106, 130);\n"
"    border: 3px solid rgb(52, 59, 72);    \n"
"}\n"
"\n"
"/* COMBOBOX */\n"
"QComboBox{\n"
"    background-color: rgb(27, 29, 35);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(27, 29, 35);\n"
"    padding: 5px;\n"
"    padding-left: 10px;\n"
"}\n"
"QComboBox:hover{\n"
"    border: 2px solid rgb(64, 71, 88);\n"
"}\n"
"QComboBox::drop-down {\n"
"    subcontrol-origin: padding;\n"
"    subcontrol-position: top right;\n"
"    width: 25px; \n"
"    border-left-width: 3px;\n"
"    border-left-color: rgba(39, 44, 54, 150);\n"
"    border-left-style: solid;\n"
"    border-top-right-radius: 3px;\n"
"    border-bottom-right-radius: 3px;    \n"
"    background-image: url(:/16x16/icons/16x16/cil-arrow-bottom.png);\n"
"    background-position: center;\n"
"    background-repeat: no-reperat;\n"
" }\n"
"QComboBox QAbstractItemView {\n"
"    color: rgb(85, 170, 255);    \n"
"    background-color: rgb(27, 29, 35);\n"
"    padding: 10px;\n"
"    selection-background-color: rgb(39, 44, 54);\n"
"}\n"
"\n"
"/* SLIDERS */\n"
"QSlider::groove:horizontal {\n"
"    border-radius: 9px;\n"
"    height: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:horizontal:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:horizontal {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:horizontal:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:horizontal:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"QSlider::groove:vertical {\n"
"    border-radius: 9px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    background-color: rgb(52, 59, 72);\n"
"}\n"
"QSlider::groove:vertical:hover {\n"
"    background-color: rgb(55, 62, 76);\n"
"}\n"
"QSlider::handle:vertical {\n"
"    background-color: rgb(85, 170, 255);\n"
"    border: none;\n"
"    height: 18px;\n"
"    width: 18px;\n"
"    margin: 0px;\n"
"    border-radius: 9px;\n"
"}\n"
"QSlider::handle:vertical:hover {\n"
"    background-color: rgb(105, 180, 255);\n"
"}\n"
"QSlider::handle:vertical:pressed {\n"
"    background-color: rgb(65, 130, 195);\n"
"}\n"
"\n"
"")
        #FRAME DECLARATION
        self.frame_main.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.frame_top = QtWidgets.QFrame(self.frame_main)
        self.frame_top.setMinimumSize(QtCore.QSize(0, 65))
        self.frame_top.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top.setStyleSheet("background-color: transparent;")
        self.frame_top.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.frame_top_right = QtWidgets.QFrame(self.frame_top)
        self.frame_top_right.setStyleSheet("background: transparent;")
        self.frame_top_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_right.setObjectName("frame_top_right")
        self.frame_top_btns = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_btns.setMaximumSize(QtCore.QSize(16777215, 42))
        self.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
        self.frame_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_btns.setObjectName("frame_top_btns")
        self.frame_toggle = QtWidgets.QFrame(self.frame_top)
        self.frame_toggle.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_toggle.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_toggle.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_toggle.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_toggle.setObjectName("frame_toggle")
        self.frame_label_top_btns = QtWidgets.QFrame(self.frame_top_btns)
        self.frame_icon_top_bar = QtWidgets.QFrame(self.frame_label_top_btns)
        self.frame_icon_top_bar.setMaximumSize(QtCore.QSize(30, 30))
        self.frame_icon_top_bar.setStyleSheet("background: transparent;\n"
"background-image: url(:/16x16/icons/16x16/cil-terminal.png);\n"
"background-position: center;\n"
"background-repeat: no-repeat;\n"
"")
        self.frame_icon_top_bar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_icon_top_bar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_icon_top_bar.setObjectName("frame_icon_top_bar")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_label_top_btns.sizePolicy().hasHeightForWidth())
        self.frame_label_top_btns.setSizePolicy(sizePolicy)
        self.frame_label_top_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_top_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_top_btns.setObjectName("frame_label_top_btns")
        #LAYOUT DECLARATION
        self.vertical_layout = QtWidgets.QVBoxLayout(self.frame_main)
        self.vertical_layout.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout.setSpacing(0)
        self.vertical_layout.setObjectName("vertical_layout")
        self.vertical_layout_2 = QtWidgets.QVBoxLayout(self.frame_top_right)
        self.vertical_layout_2.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_2.setSpacing(0)
        self.vertical_layout_2.setObjectName("vertical_layout_2")
        self.vertical_layout_3 = QtWidgets.QVBoxLayout(self.frame_toggle)
        self.vertical_layout_3.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_3.setSpacing(0)
        self.vertical_layout_3.setObjectName("vertical_layout_3")
        self.horizontal_layout_3 = QtWidgets.QHBoxLayout(self.frame_top)
        self.horizontal_layout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_3.setSpacing(0)
        self.horizontal_layout_3.setObjectName("horizontal_layout_3")
        self.horizontal_layout_4 = QtWidgets.QHBoxLayout(self.frame_top_btns)
        self.horizontal_layout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_4.setSpacing(0)
        self.horizontal_layout_4.setObjectName("horizontal_layout_4")
        self.horizontal_layout_10 = QtWidgets.QHBoxLayout(self.frame_label_top_btns)
        self.horizontal_layout_10.setContentsMargins(5, 0, 10, 0)
        self.horizontal_layout_10.setSpacing(0)
        self.horizontal_layout_10.setObjectName("horizontal_layout_10")
        self.btn_toggle_menu = QtWidgets.QPushButton(self.frame_toggle)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_toggle_menu.sizePolicy().hasHeightForWidth())
        #BUTTON MENU
        self.btn_toggle_menu.setSizePolicy(sizePolicy)
        self.btn_toggle_menu.setStyleSheet("QPushButton {\n"
                                           "    background-image: url(:/24x24/icons/24x24/cil-menu.png);\n"
                                           "    background-position: center;\n"
                                           "    background-repeat: no-reperat;\n"
                                           "    border: none;\n"
                                           "    background-color: rgb(27, 29, 35);\n"
                                           "}\n"
                                           "QPushButton:hover {\n"
                                           "    background-color: rgb(33, 37, 43);\n"
                                           "}\n"
                                           "QPushButton:pressed {    \n"
                                           "    background-color: rgb(85, 170, 255);\n"
                                           "}")
        self.btn_toggle_menu.setText("")
        self.btn_toggle_menu.setObjectName("btn_toggle_menu")
        #ADD LAYOUTS TO FRAME
        self.vertical_layout_3.addWidget(self.btn_toggle_menu)
        self.horizontal_layout_3.addWidget(self.frame_toggle)
        self.horizontal_layout_10.addWidget(self.frame_icon_top_bar)
        self.label_title_bar_top = QtWidgets.QLabel(self.frame_label_top_btns)
        #FONT FOR TITLE_BAR
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_title_bar_top.setFont(font)
        self.label_title_bar_top.setStyleSheet("background: transparent;\n"
                                               "")
        self.label_title_bar_top.setObjectName("label_title_bar_top")
        #ADD LAYOUTS TO FRAME
        self.horizontal_layout_10.addWidget(self.label_title_bar_top)
        self.horizontal_layout_4.addWidget(self.frame_label_top_btns)
        self.frame_btns_right = QtWidgets.QFrame(self.frame_top_btns)
        #FRAME DECLARATION
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_btns_right.sizePolicy().hasHeightForWidth())
        self.frame_btns_right.setSizePolicy(sizePolicy)
        self.frame_btns_right.setMaximumSize(QtCore.QSize(120, 16777215))
        self.frame_btns_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns_right.setObjectName("frame_btns_right")
        #ADD LAYOUTS TO FRAME
        self.horizontal_layout_5 = QtWidgets.QHBoxLayout(self.frame_btns_right)
        self.horizontal_layout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_5.setSpacing(0)
        self.horizontal_layout_5.setObjectName("horizontal_layout_5")
        #MINIMIZE BUTTON
        self.btn_minimize = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_minimize.sizePolicy().hasHeightForWidth())
        self.btn_minimize.setSizePolicy(sizePolicy)
        self.btn_minimize.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_minimize.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_minimize.setStyleSheet("QPushButton {    \n"
                                        "    border: none;\n"
                                        "    background-color: transparent;\n"
                                        "}\n"
                                        "QPushButton:hover {\n"
                                        "    background-color: rgb(52, 59, 72);\n"
                                        "}\n"
                                        "QPushButton:pressed {    \n"
                                        "    background-color: rgb(85, 170, 255);\n"
                                        "}")
        self.btn_minimize.setText("")
        #MINIMIZE ICON
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon)
        self.btn_minimize.setObjectName("btn_minimize")
        self.horizontal_layout_5.addWidget(self.btn_minimize)
        self.btn_maximize_restore = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_maximize_restore.sizePolicy().hasHeightForWidth())
        #MAZIMIZE BUTTON
        self.btn_maximize_restore.setSizePolicy(sizePolicy)
        self.btn_maximize_restore.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_maximize_restore.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_maximize_restore.setStyleSheet("QPushButton {    \n"
                                                "    border: none;\n"
                                                "    background-color: transparent;\n"
                                                "}\n"
                                                "QPushButton:hover {\n"
                                                "    background-color: rgb(52, 59, 72);\n"
                                                "}\n"
                                                "QPushButton:pressed {    \n"
                                                "    background-color: rgb(85, 170, 255);\n"
                                                "}")
        self.btn_maximize_restore.setText("")
        #MAZIMIZE ICON
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-window-maximize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_maximize_restore.setIcon(icon1)
        self.btn_maximize_restore.setObjectName("btn_maximize_restore")
        self.horizontal_layout_5.addWidget(self.btn_maximize_restore)

        #CLOSE BUTTON
        self.btn_close = QtWidgets.QPushButton(self.frame_btns_right)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_close.sizePolicy().hasHeightForWidth())
        self.btn_close.setSizePolicy(sizePolicy)
        self.btn_close.setMinimumSize(QtCore.QSize(40, 0))
        self.btn_close.setMaximumSize(QtCore.QSize(40, 16777215))
        self.btn_close.setStyleSheet("QPushButton {    \n"
                                     "    border: none;\n"
                                     "    background-color: transparent;\n"
                                     "}\n"
                                     "QPushButton:hover {\n"
                                     "    background-color: rgb(52, 59, 72);\n"
                                     "}\n"
                                     "QPushButton:pressed {    \n"
                                     "    background-color: rgb(85, 170, 255);\n"
                                     "}")
        self.btn_close.setText("")
        #CLOSE ICON
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_close.setIcon(icon2)
        self.btn_close.setObjectName("btn_close")
        self.horizontal_layout_5.addWidget(self.btn_close)
        self.horizontal_layout_4.addWidget(self.frame_btns_right, 0, QtCore.Qt.AlignRight)
        self.vertical_layout_2.addWidget(self.frame_top_btns)

        #FRAME DECLORATION
        self.frame_top_info = QtWidgets.QFrame(self.frame_top_right)
        self.frame_top_info.setMaximumSize(QtCore.QSize(16777215, 65))
        self.frame_top_info.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.frame_top_info.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_top_info.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top_info.setObjectName("frame_top_info")
        self.horizontal_layout_8 = QtWidgets.QHBoxLayout(self.frame_top_info)
        self.horizontal_layout_8.setContentsMargins(10, 0, 10, 0)
        self.horizontal_layout_8.setSpacing(0)
        self.horizontal_layout_8.setObjectName("horizontal_layout_8")
        self.label_top_info_1 = QtWidgets.QLabel(self.frame_top_info)
        self.label_top_info_1.setMaximumSize(QtCore.QSize(16777215, 15))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_top_info_1.setFont(font)
        self.label_top_info_1.setStyleSheet("color: rgb(98, 103, 111); ")
        self.label_top_info_1.setText("")
        self.label_top_info_1.setObjectName("label_top_info_1")
        self.horizontal_layout_8.addWidget(self.label_top_info_1)
        self.label_top_info_2 = QtWidgets.QLabel(self.frame_top_info)
        self.label_top_info_2.setMinimumSize(QtCore.QSize(0, 0))
        self.label_top_info_2.setMaximumSize(QtCore.QSize(250, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setBold(True)
        font.setWeight(75)
        self.label_top_info_2.setFont(font)
        self.label_top_info_2.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_top_info_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_top_info_2.setObjectName("label_top_info_2")
        self.horizontal_layout_8.addWidget(self.label_top_info_2)
        self.vertical_layout_2.addWidget(self.frame_top_info)
        self.horizontal_layout_3.addWidget(self.frame_top_right)
        self.vertical_layout.addWidget(self.frame_top)
        self.frame_center = QtWidgets.QFrame(self.frame_main)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_center.sizePolicy().hasHeightForWidth())
        self.frame_center.setSizePolicy(sizePolicy)
        self.frame_center.setStyleSheet("background-color: rgb(40, 44, 52);")
        self.frame_center.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_center.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_center.setObjectName("frame_center")
        self.horizontal_layout_2 = QtWidgets.QHBoxLayout(self.frame_center)
        self.horizontal_layout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontal_layout_2.setSpacing(0)
        self.horizontal_layout_2.setObjectName("horizontal_layout_2")
        self.frame_left_menu = QtWidgets.QFrame(self.frame_center)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_left_menu.sizePolicy().hasHeightForWidth())
        self.frame_left_menu.setSizePolicy(sizePolicy)
        self.frame_left_menu.setMinimumSize(QtCore.QSize(70, 0))
        self.frame_left_menu.setMaximumSize(QtCore.QSize(70, 16777215))
        self.frame_left_menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_left_menu.setStyleSheet("background-color: rgb(27, 29, 35);")
        self.frame_left_menu.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_left_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left_menu.setObjectName("frame_left_menu")
        self.vertical_layout_5 = QtWidgets.QVBoxLayout(self.frame_left_menu)
        self.vertical_layout_5.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_5.setSpacing(1)
        self.vertical_layout_5.setObjectName("vertical_layout_5")
        self.frame_menus = QtWidgets.QFrame(self.frame_left_menu)
        self.frame_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_menus.setObjectName("frame_menus")
        self.layout_menus = QtWidgets.QVBoxLayout(self.frame_menus)
        self.layout_menus.setContentsMargins(0, 0, 0, 0)
        self.layout_menus.setSpacing(0)
        self.layout_menus.setObjectName("layout_menus")
        self.vertical_layout_5.addWidget(self.frame_menus, 0, QtCore.Qt.AlignTop)
        self.frame_extra_menus = QtWidgets.QFrame(self.frame_left_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_extra_menus.sizePolicy().hasHeightForWidth())
        self.frame_extra_menus.setSizePolicy(sizePolicy)
        self.frame_extra_menus.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_extra_menus.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_extra_menus.setObjectName("frame_extra_menus")
        self.layout_menu_bottom = QtWidgets.QVBoxLayout(self.frame_extra_menus)
        self.layout_menu_bottom.setContentsMargins(0, 0, 0, 25)
        self.layout_menu_bottom.setSpacing(10)
        self.layout_menu_bottom.setObjectName("layout_menu_bottom")
        self.vertical_layout_5.addWidget(self.frame_extra_menus, 0, QtCore.Qt.AlignBottom)
        self.horizontal_layout_2.addWidget(self.frame_left_menu)
        self.frame_content_right = QtWidgets.QFrame(self.frame_center)
        self.frame_content_right.setStyleSheet("background-color: rgb(44, 49, 60);")
        self.frame_content_right.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content_right.setObjectName("frame_content_right")
        self.vertical_layout_4 = QtWidgets.QVBoxLayout(self.frame_content_right)
        self.vertical_layout_4.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_4.setSpacing(0)
        self.vertical_layout_4.setObjectName("vertical_layout_4")
        self.frame_content = QtWidgets.QFrame(self.frame_content_right)
        self.frame_content.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_content.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_content.setObjectName("frame_content")
        self.vertical_layout_9 = QtWidgets.QVBoxLayout(self.frame_content)
        self.vertical_layout_9.setContentsMargins(5, 5, 5, 5)
        self.vertical_layout_9.setSpacing(0)
        self.vertical_layout_9.setObjectName("vertical_layout_9")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_content)
        self.stackedWidget.setStyleSheet("background: transparent;")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_home = QtWidgets.QWidget()
        self.page_home.setObjectName("page_home")
        self.vertical_layout_10 = QtWidgets.QVBoxLayout(self.page_home)
        self.vertical_layout_10.setObjectName("vertical_layout_10")
        self.label_6 = QtWidgets.QLabel(self.page_home)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(40)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("")
        self.label_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.vertical_layout_10.addWidget(self.label_6)
        #SPACING ITEMS
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_10.addItem(spacerItem)
        self.horizontal_layout = QtWidgets.QHBoxLayout()
        self.horizontal_layout.setObjectName("horizontal_layout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem1)

        #START BUTTON
        self.start_button = QtWidgets.QPushButton(self.page_home)
        self.start_button.setStyleSheet("border :4px solid #555;"
                                        "border-top-left-radius :35px;"
                                        "border-top-right-radius : 35px; "
                                        "border-bottom-left-radius : 35px; "
                                        "border-bottom-right-radius : 35px;"
                                        "border-style: outset;"
                                        "padding-left: 10px;"
                                        "padding-right: 10px;"
                                        "padding-top: 10px;"
                                        "padding-bottom: 10px;"
                                        )

        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.start_button.setFont(font)
        self.start_button.setObjectName("start_button")

        self.start_button.clicked.connect(self.show_popup)

        self.horizontal_layout.addWidget(self.start_button)
        #MORE SPACER ITEMS
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontal_layout.addItem(spacerItem2)
        self.vertical_layout_10.addLayout(self.horizontal_layout)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.vertical_layout_10.addItem(spacerItem3)
        #FRAME DECLORATION
        self.stackedWidget.addWidget(self.page_home)
        self.page_widgets = QtWidgets.QWidget()
        self.page_widgets.setObjectName("page_widgets")
        self.vertical_layout_6 = QtWidgets.QVBoxLayout(self.page_widgets)
        self.vertical_layout_6.setObjectName("vertical_layout_6")
        self.frame_Adv = QtWidgets.QFrame(self.page_widgets)
        self.frame_Adv.setStyleSheet("border-radius: 5px;")
        self.frame_Adv.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Adv.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Adv.setObjectName("frame_Adv")
        self.vertical_layout_13 = QtWidgets.QVBoxLayout(self.frame_Adv)
        self.vertical_layout_13.setObjectName("vertical_layout_13")
        self.frame_video = QtWidgets.QFrame(self.frame_Adv)
        self.frame_video.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_video.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_video.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                       "border-radius: 5px;\n"
                                       "")
        self.frame_video.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_video.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_video.setObjectName("frame_video")
        self.vertical_layout_7 = QtWidgets.QVBoxLayout(self.frame_video)
        self.vertical_layout_7.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_7.setSpacing(0)
        self.vertical_layout_7.setObjectName("vertical_layout_7")
        self.Video_Title = QtWidgets.QFrame(self.frame_video)
        self.Video_Title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.Video_Title.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.Video_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Video_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Video_Title.setObjectName("Video_Title")
        self.vertical_layout_8 = QtWidgets.QVBoxLayout(self.Video_Title)
        self.vertical_layout_8.setContentsMargins(-1, -1, -1, 0)
        self.vertical_layout_8.setObjectName("vertical_layout_8")
        self.label_video = QtWidgets.QLabel(self.Video_Title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_video.setFont(font)
        self.label_video.setStyleSheet("")
        self.label_video.setObjectName("label_video")
        self.vertical_layout_8.addWidget(self.label_video)
        self.vertical_layout_7.addWidget(self.Video_Title)
        self.frame_v_path = QtWidgets.QFrame(self.frame_video)
        self.frame_v_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_v_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_v_path.setObjectName("frame_v_path")
        self.horizontal_layout_9 = QtWidgets.QHBoxLayout(self.frame_v_path)
        self.horizontal_layout_9.setObjectName("horizontal_layout_9")
        self.grid_v_path = QtWidgets.QGridLayout()
        self.grid_v_path.setContentsMargins(-1, -1, -1, 0)
        self.grid_v_path.setObjectName("grid_v_path")

        #LINE-EDIT FOR VIDEO PATH
        self.video_lineEdit = QtWidgets.QLineEdit(self.frame_v_path)
        self.video_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.video_lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.video_lineEdit.setStyleSheet("QLineEdit {\n"
                                          "    background-color: rgb(27, 29, 35);\n"
                                          "    border-radius: 5px;\n"
                                          "    border: 2px solid rgb(27, 29, 35);\n"
                                          "    padding-left: 10px;\n"
                                          "}\n"
                                          "QLineEdit:hover {\n"
                                          "    border: 2px solid rgb(64, 71, 88);\n"
                                          "}\n"
                                          "QLineEdit:focus {\n"
                                          "    border: 2px solid rgb(91, 101, 124);\n"
                                          "}")
        self.video_lineEdit.setInputMask("")
        self.video_lineEdit.setText("")
        self.video_lineEdit.setObjectName("lineEdit_video")
        self.grid_v_path.addWidget(self.video_lineEdit, 0, 0, 1, 1)

        #OPEN BUTTON FOR VIDEO PATH
        self.Open_v_button = QtWidgets.QPushButton(self.frame_v_path)
        self.Open_v_button.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.Open_v_button.setFont(font)
        self.Open_v_button.clicked.connect(self.open_video_dialog)
        self.Open_v_button.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/16x16/icons/16x16/cil-folder-open.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.Open_v_button.setIcon(icon3)
        self.Open_v_button.setObjectName("Open_v_button")
        self.grid_v_path.addWidget(self.Open_v_button, 0, 1, 1, 1)
        self.horizontal_layout_9.addLayout(self.grid_v_path)
        self.vertical_layout_7.addWidget(self.frame_v_path)
        self.vertical_layout_13.addWidget(self.frame_video)
        self.frame_video_2 = QtWidgets.QFrame(self.frame_Adv)
        self.frame_video_2.setMinimumSize(QtCore.QSize(0, 110))
        self.frame_video_2.setMaximumSize(QtCore.QSize(16777215, 110))
        self.frame_video_2.setStyleSheet("background-color: rgb(41, 45, 56);\n"
                                         "border-radius: 5px;\n"
                                         "")
        self.frame_video_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_video_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_video_2.setObjectName("frame_video_2")
        self.vertical_layout_14 = QtWidgets.QVBoxLayout(self.frame_video_2)
        self.vertical_layout_14.setContentsMargins(0, 0, 0, 0)
        self.vertical_layout_14.setObjectName("vertical_layout_14")
        #SAVED VIDEO PATH TITLE
        self.Screen_Title = QtWidgets.QFrame(self.frame_video_2)
        self.Screen_Title.setMaximumSize(QtCore.QSize(16777215, 35))
        self.Screen_Title.setStyleSheet("background-color: rgb(39, 44, 54);")
        self.Screen_Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Screen_Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Screen_Title.setObjectName("Screen_Title")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.Screen_Title)
        self.gridLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        #SAVED VIDEO PATH LABEL
        self.label_path = QtWidgets.QLabel(self.Screen_Title)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_path.setFont(font)
        self.label_path.setStyleSheet("")
        self.label_path.setObjectName("label_path")
        self.gridLayout_6.addWidget(self.label_path, 0, 0, 1, 1)
        self.vertical_layout_14.addWidget(self.Screen_Title)
        self.frame_p_path = QtWidgets.QFrame(self.frame_video_2)
        self.frame_p_path.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_p_path.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_p_path.setObjectName("frame_p_path")
        self.horizontal_layout_11 = QtWidgets.QHBoxLayout(self.frame_p_path)
        self.horizontal_layout_11.setObjectName("horizontal_layout_11")
        self.grid_p_path = QtWidgets.QGridLayout()
        self.grid_p_path.setContentsMargins(-1, -1, -1, 0)
        self.grid_p_path.setObjectName("grid_p_path")

        #SAVED VIDEO PATH'S LINE-EDIT
        self.screenpath_lineEdit = QtWidgets.QLineEdit(self.frame_p_path)
        self.screenpath_lineEdit.setMinimumSize(QtCore.QSize(0, 30))
        self.screenpath_lineEdit.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.screenpath_lineEdit.setStyleSheet("QLineEdit {\n"
                                               "    background-color: rgb(27, 29, 35);\n"
                                               "    border-radius: 5px;\n"
                                               "    border: 2px solid rgb(27, 29, 35);\n"
                                               "    padding-left: 10px;\n"
                                               "}\n"
                                               "QLineEdit:hover {\n"
                                               "    border: 2px solid rgb(64, 71, 88);\n"
                                               "}\n"
                                               "QLineEdit:focus {\n"
                                               "    border: 2px solid rgb(91, 101, 124);\n"
                                               "}")
        self.screenpath_lineEdit.setInputMask("")
        self.screenpath_lineEdit.setText("")
        self.screenpath_lineEdit.setObjectName("lineEdit_path")
        self.grid_p_path.addWidget(self.screenpath_lineEdit, 0, 0, 1, 1)
        #OPEN VIDEO PATH BUTTON
        self.Open_p_button = QtWidgets.QPushButton(self.frame_p_path)
        self.Open_p_button.setMinimumSize(QtCore.QSize(150, 30))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(9)
        self.Open_p_button.setFont(font)
        self.Open_p_button.clicked.connect(self.open_screenshot_dialog)
        self.Open_p_button.setStyleSheet("QPushButton {\n"
                                         "    border: 2px solid rgb(52, 59, 72);\n"
                                         "    border-radius: 5px;    \n"
                                         "    background-color: rgb(52, 59, 72);\n"
                                         "}\n"
                                         "QPushButton:hover {\n"
                                         "    background-color: rgb(57, 65, 80);\n"
                                         "    border: 2px solid rgb(61, 70, 86);\n"
                                         "}\n"
                                         "QPushButton:pressed {    \n"
                                         "    background-color: rgb(35, 40, 49);\n"
                                         "    border: 2px solid rgb(43, 50, 61);\n"
                                         "}")
        self.Open_p_button.setIcon(icon3)
        self.Open_p_button.setObjectName("Open_p_button")
        self.grid_p_path.addWidget(self.Open_p_button, 0, 1, 1, 1)
        self.horizontal_layout_11.addLayout(self.grid_p_path)
        self.vertical_layout_14.addWidget(self.frame_p_path)
        self.vertical_layout_13.addWidget(self.frame_video_2)
        # FRAME DECLARATION FOR CHECKS
        self.frame_Checks = QtWidgets.QFrame(self.frame_Adv)
        self.frame_Checks.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_Checks.sizePolicy().hasHeightForWidth())
        self.frame_Checks.setSizePolicy(sizePolicy)
        self.frame_Checks.setMinimumSize(QtCore.QSize(0, 150))
        self.frame_Checks.setStyleSheet("background-color: rgb(39, 44, 54);\n"
                                        "border-radius: 5px;")
        self.frame_Checks.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_Checks.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_Checks.setObjectName("frame_Checks")
        self.gridLayout = QtWidgets.QGridLayout(self.frame_Checks)
        self.gridLayout.setObjectName("gridLayout")

        #LABEL FOR VIDEO OPTIONS
        self.label_vo = QtWidgets.QLabel(self.frame_Checks)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_vo.setFont(font)
        self.label_vo.setObjectName("label_vo")
        self.gridLayout.addWidget(self.label_vo, 0, 0, 1, 1)
        #LABEL FOR DISTANCING OPTIONS
        self.label_do = QtWidgets.QLabel(self.frame_Checks)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_do.setFont(font)
        self.label_do.setObjectName("label_do")
        self.gridLayout.addWidget(self.label_do, 0, 1, 1, 1)
        # WEBCAM RADIO BUTTON
        self.webcam_Radio = QtWidgets.QRadioButton(self.frame_Checks)
        self.webcam_Radio.setStyleSheet("")
        self.webcam_Radio.setObjectName("webcam_Radio")
        self.webcam_Radio.setChecked(True)
        self.gridLayout.addWidget(self.webcam_Radio, 1, 0, 1, 1)
        #AUDIO CHECK BUTTON
        self.audio_Check = QtWidgets.QCheckBox(self.frame_Checks)
        self.audio_Check.setAutoFillBackground(False)
        self.audio_Check.setStyleSheet("")
        self.audio_Check.setObjectName("audio_Check")
        self.gridLayout.addWidget(self.audio_Check, 1, 1, 1, 1)
        # VIDEO RADIO bUTTON
        self.video_Radio = QtWidgets.QRadioButton(self.frame_Checks)
        self.video_Radio.setObjectName("video_Radio")
        self.gridLayout.addWidget(self.video_Radio, 2, 0, 1, 1)
        #SAVED VIDEO CHECK BUTTON
        self.screen_Check = QtWidgets.QCheckBox(self.frame_Checks)
        self.screen_Check.setObjectName("screen_Check")
        self.gridLayout.addWidget(self.screen_Check, 2, 1, 1, 1)
        self.vertical_layout_13.addWidget(self.frame_Checks)
        #FRAME FOR CAMREA SPECIFICATION
        self.frame_camera = QtWidgets.QFrame(self.frame_Adv)
        self.frame_camera.setStyleSheet("background-color: rgb(39, 44, 54);\n"
                                        "border-radius: 5px;")
        self.frame_camera.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_camera.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_camera.setObjectName("frame_camera")
        self.vertical_layout_15 = QtWidgets.QVBoxLayout(self.frame_camera)
        self.vertical_layout_15.setObjectName("vertical_layout_15")
        #CAMERA SPECIFICATION TITLE
        self.camera_title = QtWidgets.QLabel(self.frame_camera)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.camera_title.setFont(font)
        self.camera_title.setObjectName("camera_title")
        self.vertical_layout_15.addWidget(self.camera_title)
        #TITLE FOR HEIGHT
        self.height_title = QtWidgets.QLabel(self.frame_camera)
        self.height_title.setObjectName("height_title")
        self.vertical_layout_15.addWidget(self.height_title)
        #LINE-EDIT FOR HEIGHT
        self.height_lineEdit = QtWidgets.QLineEdit(self.frame_camera)
        self.height_lineEdit.setObjectName("height_lineEdit")
        self.vertical_layout_15.addWidget(self.height_lineEdit)
        #TITLE FOR ANGLE
        self.angle_title = QtWidgets.QLabel(self.frame_camera)
        self.angle_title.setObjectName("angle_title")
        self.vertical_layout_15.addWidget(self.angle_title)
        #LINE-EDIT FOR ANGLE
        self.angle_lineEdit = QtWidgets.QLineEdit(self.frame_camera)
        self.angle_lineEdit.setObjectName("angle_lineEdit")
        self.vertical_layout_15.addWidget(self.angle_lineEdit)
        #TITLE FOR FOV VERTICAL
        self.fov_v_title = QtWidgets.QLabel(self.frame_camera)
        self.fov_v_title.setObjectName("fov_v_title")
        self.vertical_layout_15.addWidget(self.fov_v_title)
        #LINE-EDIT FOR FOV VERTICAL
        self.fov_v_lineEdit = QtWidgets.QLineEdit(self.frame_camera)
        self.fov_v_lineEdit.setObjectName("fov_v_lineEdit")
        self.vertical_layout_15.addWidget(self.fov_v_lineEdit)
        #TITLE FOR FOV HORIZONTAL
        self.fov_h_title = QtWidgets.QLabel(self.frame_camera)
        self.fov_h_title.setObjectName("fov_h_title")
        self.vertical_layout_15.addWidget(self.fov_h_title)
        #LINE-EDIT FOR FAV HORIZONTAL
        self.fov_h_lineEdit = QtWidgets.QLineEdit(self.frame_camera)
        self.fov_h_lineEdit.setObjectName("fov_h_lineEdit")
        self.vertical_layout_15.addWidget(self.fov_h_lineEdit)
        self.vertical_layout_13.addWidget(self.frame_camera)
        self.vertical_layout_6.addWidget(self.frame_Adv)
        self.stackedWidget.addWidget(self.page_widgets)
        self.vertical_layout_9.addWidget(self.stackedWidget)
        self.vertical_layout_4.addWidget(self.frame_content)
        self.frame_grip = QtWidgets.QFrame(self.frame_content_right)
        self.frame_grip.setMinimumSize(QtCore.QSize(0, 25))
        self.frame_grip.setMaximumSize(QtCore.QSize(16777215, 25))
        self.frame_grip.setStyleSheet("background-color: rgb(33, 37, 43);")
        self.frame_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_grip.setObjectName("frame_grip")
        self.horizontal_layout_6 = QtWidgets.QHBoxLayout(self.frame_grip)
        self.horizontal_layout_6.setContentsMargins(0, 0, 2, 0)
        self.horizontal_layout_6.setSpacing(0)
        self.horizontal_layout_6.setObjectName("horizontal_layout_6")
        self.frame_label_bottom = QtWidgets.QFrame(self.frame_grip)
        self.frame_label_bottom.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_label_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_label_bottom.setObjectName("frame_label_bottom")
        self.horizontal_layout_7 = QtWidgets.QHBoxLayout(self.frame_label_bottom)
        self.horizontal_layout_7.setContentsMargins(10, 0, 10, 0)
        self.horizontal_layout_7.setSpacing(0)
        self.horizontal_layout_7.setObjectName("horizontal_layout_7")
        #LABELS FOR BOTTOM FRAME
        self.label_credits = QtWidgets.QLabel(self.frame_label_bottom)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_credits.setFont(font)
        self.label_credits.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_credits.setObjectName("label_credits")
        self.horizontal_layout_7.addWidget(self.label_credits)
        self.label_version = QtWidgets.QLabel(self.frame_label_bottom)
        self.label_version.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        self.label_version.setFont(font)
        self.label_version.setStyleSheet("color: rgb(98, 103, 111);")
        self.label_version.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_version.setObjectName("label_version")
        self.horizontal_layout_7.addWidget(self.label_version)
        self.horizontal_layout_6.addWidget(self.frame_label_bottom)
        self.frame_size_grip = QtWidgets.QFrame(self.frame_grip)
        self.frame_size_grip.setMaximumSize(QtCore.QSize(20, 20))
        self.frame_size_grip.setStyleSheet("QSizeGrip {\n"
                                           "    background-image: url(:/16x16/icons/16x16/cil-size-grip.png);\n"
                                           "    background-position: center;\n"
                                           "    background-repeat: no-reperat;\n"
                                           "}")
        self.frame_size_grip.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_size_grip.setObjectName("frame_size_grip")
        self.horizontal_layout_6.addWidget(self.frame_size_grip)
        self.vertical_layout_4.addWidget(self.frame_grip)
        self.horizontal_layout_2.addWidget(self.frame_content_right)
        self.vertical_layout.addWidget(self.frame_center)
        self.grid_layout_2.addWidget(self.frame_main, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.central_widget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.btn_minimize, self.btn_maximize_restore)
        MainWindow.setTabOrder(self.btn_maximize_restore, self.btn_close)
        MainWindow.setTabOrder(self.btn_close, self.btn_toggle_menu)
        MainWindow.setTabOrder(self.btn_toggle_menu, self.audio_Check)
        MainWindow.setTabOrder(self.audio_Check, self.webcam_Radio)

    # Input:       a MainWindow created by PyQt5/PySide
    # Output:      none
    # Description: Lets the window be moved around the screen and be resized
    def retranslateUi(self, MainWindow) -> None:
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Social Distance Detector"))

        #SET TOOL TIPS
        self.btn_minimize.setToolTip(_translate("MainWindow", "Minimize"))
        self.btn_maximize_restore.setToolTip(_translate("MainWindow", "Maximize"))
        self.btn_close.setToolTip(_translate("MainWindow", "Close"))

        #,SET TEXT FOR ALL LABELS, TITLE,BUTTON
        self.label_title_bar_top.setText(_translate("MainWindow", "Main Window"))
        self.label_top_info_2.setText(_translate("MainWindow", "| HOME"))
        self.label_6.setText(_translate("MainWindow", "Social Distance Detector"))
        self.start_button.setText(_translate("MainWindow", "Start"))
        self.label_video.setText(_translate("MainWindow", "Choose Video File"))
        self.Open_v_button.setText(_translate("MainWindow", "Choose Video"))
        self.label_path.setText(_translate("MainWindow", "Choose Screen Shot Path"))
        self.Open_p_button.setText(_translate("MainWindow", "ChoosePath"))
        self.label_vo.setText(_translate("MainWindow", "Video Options"))
        self.label_do.setText(_translate("MainWindow", "Distincing Options"))
        self.webcam_Radio.setText(_translate("MainWindow", "Webcam (Default)"))
        self.audio_Check.setText(_translate("MainWindow", "Audio Alert"))
        self.video_Radio.setText(_translate("MainWindow", "Video"))
        self.screen_Check.setText(_translate("MainWindow", "Screen Shots"))
        self.camera_title.setText(_translate("MainWindow", "Camera Specification"))
        self.height_title.setText(_translate("MainWindow", "Height (Feet)"))
        self.angle_title.setText(_translate("MainWindow", "Angle (Degree)"))
        self.fov_v_title.setText(_translate("MainWindow", "Field Of View Vertical (Degree)"))
        self.fov_h_title.setText(_translate("MainWindow", "Field Of View Horizontal (Degree)"))
        self.label_credits.setText(_translate("MainWindow", "Social Distance Team"))
        self.label_version.setText(_translate("MainWindow", "v1.0.0"))

        #SET PLACEHOLDER TEXT
        self.video_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter video file here"))
        self.screenpath_lineEdit.setPlaceholderText(_translate("MainWindow", "Enter screen shot path here"))
        self.height_lineEdit.setPlaceholderText(_translate("MainWindow", "9 (default)"))
        self.angle_lineEdit.setPlaceholderText( _translate("MainWindow", "90 (default)"))
        self.fov_h_lineEdit.setPlaceholderText( _translate("MainWindow", "90 (default)"))
        self.fov_v_lineEdit.setPlaceholderText( _translate("MainWindow", "110 (default)"))

    # Input:       None
    # Output:      None
    # Description: Parses and verifies the input. If any input is not valid, show a popup error and have the user try again. If no input or valid input is given for all fields, send all user input and selections to main loop
    def show_popup(self) -> None:
        height = 9
        angle  = 90
        fov_h  = 90
        fov_v  = 110

        # Dummy variables for the otherboxes on GUI --
        webCheck    = self.webcam_Radio.isChecked()
        audioAlert  = self.audio_Check.isChecked()
        screenShots = self.screen_Check.isChecked()

        #CHECK INPUTS
        if bool(self.height_lineEdit.text()):
            if  ( not isinstance(int(float(self.height_lineEdit.text())), int) or not isinstance(float(self.height_lineEdit.text()), float)):
                height = -1
            else:
                height = float(self.height_lineEdit.text())

        if bool(self.angle_lineEdit.text()):
            if ( not isinstance(int(float(self.angle_lineEdit.text())), int) or not isinstance(float(self.angle_lineEdit.text()), float )):
                angle = -1
            else:
                angle = float(self.angle_lineEdit.text())

        if  bool(self.fov_h_lineEdit.text()):
            if ( not isinstance(int(float(self.fov_h_lineEdit.text())), int) or not isinstance(float(self.fov_h_lineEdit.text()), float)):
                fov_h = -1
            else:
                fov_h = float(self.fov_h_lineEdit.text())

        if bool(self.fov_v_lineEdit.text()):
            if ( not isinstance(int(float(self.fov_v_lineEdit.text())), int) or not isinstance(float(self.fov_v_lineEdit.text()), float)):
                fov_v = -1
            else:
                fov_v = float(self.fov_v_lineEdit.text())

        #IF A INVALID INPUT THROW ERROR MESSAGE
        if(height < 0.0 or height > 200.0 or angle < 0.0 or angle > 90.0  or \
           fov_h  < 0.0 or fov_h  > 359.0 or fov_v < 0.0 or fov_v > 359.0 or \
           os.path.isdir(self.video_lineEdit.text())):
            msg = QMessageBox()
            msg.setWindowTitle("ERROR")
            msg.setText("Invalid value(s) entered")
            msg.setIcon(QMessageBox.Critical)
            msg.setDetailedText("All values must be numbers and cannot be empty\n\n\
                                 Height must be in the range 0 to 200 feet\n\n\
                                 Angle must be in the range 0 to 90 degrees\n\n\
                                 Field of Views must be in the range 0 to 360 degrees\n\n\
                                 Video path must be a path to a video")
            x = msg.exec_()
        else: # VALID INPUT CONTINUE TO PROGRAM
            img.init_opencv()
            img.start_human_detection_loop(height, angle, fov_h, fov_v, webCheck, audioAlert, screenShots, self.screenpath_lineEdit.text(), self.video_lineEdit.text())
            img.stop_opencv()

    # Input:       None
    # Output:      None
    # Description: Lets the user choose an input video file
    def open_video_dialog(self):
        def updateText():
            # update the contents of the line edit widget with the selected files
            selected = []
            for index in view.selectionModel().selectedRows():
                  selected.append('"{}"'.format(index.data()))
            lineEdit.setText(' '.join(selected))
        check = QWidget()
        dialog = QtWidgets.QFileDialog(check)
        dialog.setFileMode(dialog.AnyFile)
        dialog.setOption(dialog.DontUseNativeDialog, True)
        dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

        stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
        view = stackedWidget.findChild(QtWidgets.QListView)
        view.selectionModel().selectionChanged.connect(updateText)

        lineEdit = dialog.findChild(QtWidgets.QLineEdit)
        # clear the line edit contents whenever the current directory changes
        dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

        dialog.exec_()
        print(QFileDialog.fileMode(dialog))
        path = dialog.selectedFiles()[0]
        self.video_lineEdit.setText(path)
        print(self.video_lineEdit.text())

    # Input:       None
    # Output:      None
    # Description: Lets the user choose a directory to save output videos
    def open_screenshot_dialog(self):
        def updateText():
            # update the contents of the line edit widget with the selected files
            selected = []
            for index in view.selectionModel().selectedRows():
                  selected.append('"{}"'.format(index.data()))
            lineEdit.setText(' '.join(selected))
        check = QWidget()
        dialog = QtWidgets.QFileDialog(check)
        dialog.setFileMode(dialog.Directory)
        dialog.setOption(dialog.DontUseNativeDialog, True)
        dialog.accept = lambda: QtWidgets.QDialog.accept(dialog)

        stackedWidget = dialog.findChild(QtWidgets.QStackedWidget)
        view = stackedWidget.findChild(QtWidgets.QListView)
        view.selectionModel().selectionChanged.connect(updateText)

        lineEdit = dialog.findChild(QtWidgets.QLineEdit)
        # clear the line edit contents whenever the current directory changes
        dialog.directoryEntered.connect(lambda: lineEdit.setText(''))

        dialog.exec_()
        print(QFileDialog.fileMode(dialog))
        path = dialog.selectedFiles()[0]
        self.screenpath_lineEdit.setText(path)
        print(self.screenpath_lineEdit.text())
