#Created by Mateo LEBRUN

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap
from PyQt5.QtWidgets import QMainWindow
import source
import glob
import os
from Window2 import Ui_Window2
#THe main window contains methods that are openning subWindows 
class Ui_MainWindow(QMainWindow):

        def __init__(self):
                super(Ui_MainWindow,self).__init__()

        #This method opens and setup the Window2 and all its buttons
        def openWindow(self):

                self.ui = Ui_Window2() #

                self.ui.setupUi(lang) #
                self.ui.show()
                #self.window.showFullScreen() #
                self.ui.backbut.clicked.connect(lambda :self.ui.leavingWin()) #
                self.ui.captureBut.clicked.connect(lambda : self.ui.launchCam(5)) #
                self.ui.screenBut.clicked.connect(lambda : self.ui.takePicture())
                self.ui.infoBut.clicked.connect(lambda : self.ui.openWindow3())
                self.ui.moreBut.clicked.connect(lambda :self.ui.openWindow4())
                        

        #This method is called when creating the window 



        def setupUi(self):
                self.setObjectName("MainWindow")
                self.resize(1920, 1080)
                width = self.width()
                self.setAnimated(True)
                self.centralwidget = QtWidgets.QWidget(self)
                self.centralwidget.setObjectName("centralwidget")
                self.centralwidget.setStyleSheet(
                        "QPushButton[objectName^=\"but\"]{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 12pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}"
                        "#centralwidget{background-image: url(:/images/assets/back1.jpg);}\n")

                #a frame to contain buttons
                self.titlelabel = QtWidgets.QLabel(self.centralwidget)
                self.titlelabel.setGeometry(QtCore.QRect(width/4, 20, 961, 61))
                self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
                self.titlelabel.setStyleSheet("\n"
        "font: 32pt \"Adobe Pi Std\";\n"
        "color: rgb(255, 255, 255);")
                self.titlelabel.setTextFormat(QtCore.Qt.RichText)
                self.titlelabel.setScaledContents(True)
                self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
                self.titlelabel.setObjectName("titlelabel")
                self.titlelabel.setAttribute(QtCore.Qt.WA_TranslucentBackground) # We want to keep the background image as a global background , thus most of Layouts or Widgets avec transparent background

                self.frameInfo = QtWidgets.QFrame(self.centralwidget)
                self.frameInfo.setGeometry(QtCore.QRect(50, 300, 1400, 800))
                self.frameInfo.setAttribute(QtCore.Qt.WA_TranslucentBackground) #transparent frame
                self.frameInfo.setObjectName("frameInfo")

                self.frameInfo.hide()
                
                self.labelIntro=QtWidgets.QLabel(self.frameInfo)
                self.labelIntro.setGeometry(QtCore.QRect(10,10,1350,225))
                self.labelIntro.setScaledContents(True)
                self.labelIntro.setAttribute(QtCore.Qt.WA_TranslucentBackground) 
                self.labelIntro.setAlignment(QtCore.Qt.AlignLeft)
                self.labelIntro.setStyleSheet("\n"
        "font: 24pt \"Adobe Pi Std\";\n"
        "color: rgb(255, 255, 255);")
                self.labelIntro.setObjectName("labelIntro")


                self.frameLang = QtWidgets.QFrame(self.centralwidget)
                self.frameLang.setGeometry(QtCore.QRect(20,800, 1600, 250))
                self.frameLang.setAttribute(QtCore.Qt.WA_TranslucentBackground) #transparent frame
                self.frameLang.setObjectName("frameLang")

                self.butFr = QtWidgets.QPushButton(self.frameLang)
                self.butFr.setGeometry(QtCore.QRect(20, 30, 160, 80))
                self.butFr.setObjectName("butFr")
                icon = QtGui.QIcon('assets/fr.jpg')
                self.butFr.setIcon(icon)
                self.butFr.setIconSize(QtCore.QSize(30,25))



                self.butEng = QtWidgets.QPushButton(self.frameLang)
                self.butEng.setGeometry(QtCore.QRect(470, 30, 160, 80))
                self.butEng.setObjectName("butEng")
                icon = QtGui.QIcon('assets/eng.jpg')
                self.butEng.setIcon(icon)
                self.butEng.setIconSize(QtCore.QSize(30,25))


                self.butDe = QtWidgets.QPushButton(self.frameLang)
                self.butDe.setGeometry(QtCore.QRect(920, 30, 160, 80))
                self.butDe.setObjectName("butDe")
                icon = QtGui.QIcon('assets/de.png')
                self.butDe.setIcon(icon)
                self.butDe.setIconSize(QtCore.QSize(30,25))

                self.butLu = QtWidgets.QPushButton(self.frameLang)
                self.butLu.setGeometry(QtCore.QRect(1370, 30, 160, 80))
                self.butLu.setObjectName("butLu")
                icon = QtGui.QIcon('assets/lu.png')
                self.butLu.setIcon(icon)
                self.butLu.setIconSize(QtCore.QSize(30,25))


                self.butFr.clicked.connect(lambda :self.switchLanguage(0))
                self.butEng.clicked.connect(lambda : self.switchLanguage(1))





                self.frame = QtWidgets.QFrame(self.centralwidget)
                self.frame.setGeometry(QtCore.QRect(1500, 200, 331, 591))
                self.frame.setAttribute(QtCore.Qt.WA_TranslucentBackground) #transparent frame
                self.frame.setObjectName("frame")

                self.frame.hide()
                self.exploreBut = QtWidgets.QPushButton(self.frame)
                self.exploreBut.setGeometry(QtCore.QRect(20, 30, 301, 51))
                self.exploreBut.setMouseTracking(True)
                #css stylesheet to definie our buttons
                self.exploreBut.setStyleSheet("QPushButton{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 18pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}")
                self.exploreBut.setObjectName("exploreBut")
                self.exploreBut.clicked.connect(self.openWindow) #binding click signals to the button, so the Window 2 will be opened once button is clicked
                
                self.setCentralWidget(self.centralwidget)
                self.retranslateUi()
                QtCore.QMetaObject.connectSlotsByName(self)



        def switchLanguage(self,num):
                global lang
                lang = num
                if num ==0:
                        print("You picked French")
                        self.titlelabel.setText(" L'Intelligence Arificielle")
                        self.labelIntro.setText("L'intelligence artificielle est la nouvelle tendance qui fait rêver tout le monde.\n"
                        "Mais qu'est-ce que l'intelligence artificielle? Comment ça marche? Que peut faire la machine?\n"
                        "Eh bien, vous pourriez être surpris ... Explorons cela ensemble!")

                elif num==1:
                        print("You picked English")
                        self.titlelabel.setText("Artificial Intelligence")
                        self.labelIntro.setText("Artifical Intelligence is the new on going trend that makes everyone dreaming.\n"
                        "But what is Artifical Intelligence? How does it work? What can the machine do?\n"
                        "Well you might be surprised...\nLet's Explore this Together!")
                elif num ==2:
                        print("You picked Deutsch")
                        self.titlelabel.setText("Künstliche Intelligenz")
                        
                else : 
                        print("Luxem")
                self.frame.show()
                self.frameInfo.show()





        def retranslateUi(self):
                _translate = QtCore.QCoreApplication.translate
                self.setWindowTitle(_translate("MainWindow", "MainWindow"))
                self.exploreBut.setText(_translate("MainWindow", "Explore!"))
                self.titlelabel.setText(_translate("MainWindow","Artificial Intelligence"))
                self.labelIntro.setText(_translate("MainWindow","Artifical Intelligence is the new on going trend that makes everyone dreaming.\nBut what is Artifical Intelligence? How does it work? What can the machine do?\nWell you might be surprised...\nLet's Explore this Together!"))
                self.butFr.setText(_translate("MainWindow","Français"))
                self.butEng.setText(_translate("MainWindow","English"))
                self.butDe.setText(_translate("MainWindow","Deutsche"))
                self.butLu.setText(_translate("MainWindow","Lëtzebuergesch"))
                

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_MainWindow()
    ui.setupUi()
    ui.show()
    #MainWindow.showFullScreen()
    #print(MainWindow.height())
    #print(MainWindow.width())
    sys.exit(app.exec_())
    
