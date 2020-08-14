#Created by Mateo LEBRUN

#This file mostly contains concepts that has been alreazdy explained

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
import source

class Ui_Window3(QMainWindow):

    def __init__(self):
        super(Ui_Window3,self).__init__()

    
    def setupUi(self,lang):
        self.setObjectName("Window3")
        self.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(self)

        self.timer = 120000
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet(
            "QPushButton{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "background-color : rgb(0,0,0);"
                        "border-color: gray;"
                        "font: 14pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}"
            "#centralwidget {background-image: url(:/images/assets/back1.jpg);}")
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(30, 30, 1800, 71))
        self.titlelabel.setObjectName("titlelabel")
        self.titlelabel.setStyleSheet(
            "font: 32pt \"Adobe Pi Std\";"
            "color: rgb(255, 255, 255);")
        self.titlelabel.setAlignment(QtCore.Qt.AlignLeft)

        self.backBut2= QtWidgets.QPushButton(self.centralwidget)
        self.backBut2.setGeometry(QtCore.QRect(1780,980,110,41))
        self.backBut2.setObjectName("backBut2")
        icon = QtGui.QIcon('assets/r.png')
        self.backBut2.setIcon(icon)
        self.backBut2.setIconSize(QtCore.QSize(30,25))

        self.framelvl = QtWidgets.QFrame(self.centralwidget)
        self.framelvl.setGeometry(QtCore.QRect(30, 160, 221, 731))
        self.framelvl.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.framelvl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.framelvl.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.framelvl.setObjectName("framelvl")
        


        self.easyBut = QtWidgets.QPushButton(self.framelvl)
        self.easyBut.setGeometry(QtCore.QRect(0, 50, 141, 41))
        self.easyBut.setObjectName("easyBut")

        self.normalBut = QtWidgets.QPushButton(self.framelvl)
        self.normalBut.setGeometry(QtCore.QRect(0, 350, 141, 41))
        self.normalBut.setObjectName("normalBut")

        self.AdvancedBut = QtWidgets.QPushButton(self.framelvl)
        self.AdvancedBut.setGeometry(QtCore.QRect(0, 650, 141, 41))
        self.AdvancedBut.setObjectName("AdvancedBut")


        if lang ==0:
            self.titlelabel.setText("Comprendre le fonctionnement de cette Inteligence Arificielle marche ")
            self.easyBut.setText("Facile")
            self.normalBut.setText("Normal")
            self.AdvancedBut.setText( "Avancé")
            self.backBut2.setText("retour")
        elif lang ==1:
            self.titlelabel.setText("Through different level of undestanding, learn how this artifical intelligence works")
            self.easyBut.setText("Easy")
            self.normalBut.setText("Normal")
            self.AdvancedBut.setText("Advanced")
            self.backBut2.setText("back")

        elif lang ==2:
            pass
        else :
            pass

        self.qtim = QtCore.QTimer()
        self.qtim.start(self.timer)
        self.qtim.timeout.connect(self.close)


        self.easyBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.normalBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.AdvancedBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))



        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    

    def addtimer(self):
        if self.qtim.remainingTime() <= 60000:
            self.qtim.setInterval(self.timer)
            self.qtim.start()
    


    def mousePressEvent(self,event):
        if event == QtGui.QMouseEvent.MouseButtonPress:
            self.addtimer()
        else:
            self.addtimer()

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Window3", "MainWindow"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window3 = QtWidgets.QMainWindow()
    sys.exit(app.exec_())
