# importing the required libraries 
  
from PyQt5.QtCore import * 
from PyQt5.QtGui import * 
from PyQt5.QtWidgets import * 
import sys 
  
  
class Window(QMainWindow): 
    def __init__(self): 
        super().__init__() 
  
  
        # set the title 
        self.setWindowTitle("Python") 
  
        # setting  the geometry of window 
        self.setGeometry(60, 60, 600, 400) 
  

        # creating a label widget 
        self.label_2 = QLabel("Different curves", self) 
  
        # moving position 
        self.label_2.move(230, 200) 
  
        # setting curves at each corner 
        self.label_2.setStyleSheet("border :4px solid #555;"
                                   "border-top-left-radius :35px;"
                                   "border-top-right-radius : 35px; "
                                   "border-bottom-left-radius : 35px; "
                                   "border-bottom-right-radius : 35px;"
                                   "border-style: outset"
                                   )

  
        # resizing the label 
        self.label_2.resize(100, 100) 
  
        # show all the widgets 
        self.show() 
  
  
# create pyqt5 app 
App = QApplication(sys.argv) 
  
# create the instance of our Window 
window = Window() 
# start the app 
sys.exit(App.exec()) 