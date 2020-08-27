##creeated by Mateo LEBRUN



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie,QPixmap
from PyQt5.QtCore import QSize
import source

#This window is simply used as a pop up to ask if someone wants to stay on the current page or leave it. Useful for incativity

DURATION = 10
class Ui_Window5(QMainWindow):
    
    def __init__(self):
        super(Ui_Window5,self).__init__()

    def setupUi(self,lang):
        self.setObjectName("Window5")
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setStyleSheet("border : 2px  solid gray")
        self.centralwidget = QtWidgets.QWidget(self)
        self.resize(400,200)
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

        self.gridLay = QtWidgets.QGridLayout(self.centralwidget)
        self.setObjectName("gridLay")

        self.leaveBut = QtWidgets.QPushButton(self.centralwidget)
        self.leaveBut.setObjectName("leaveBut")
        self.leaveBut.setFixedSize(QSize(141,41))
        self.stayBut = QtWidgets.QPushButton(self.centralwidget)
        self.stayBut.setObjectName("stayBut")
        self.stayBut.setFixedSize(QSize(141,41))

        self.infoLabel=QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setStyleSheet(
            "font: 14pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);"
            "border : None;")


        self.gridLay.addWidget(self.infoLabel,1,0,1,2)
        self.gridLay.addWidget(self.stayBut,0,0,1,1)
        self.gridLay.addWidget(self.leaveBut,0,1,1,1)

        self.timer_start()
        self.update_gui()

        if lang ==0:
            self.stayBut.setText("Rester")
            self.leaveBut.setText("Quitter")
        elif lang ==1:
            self.stayBut.setText("Stay")
            self.leaveBut.setText(" Quit")
        elif lang ==2:
            self.stayBut.setText("")
            self.leaveBut.setText("")
        elif lang ==3:
            self.stayBut.setText("")
            self.leaveBut.setText("")
        else :
            self.stayBut.setText("")
            self.leaveBut.setText("")
        self.setCentralWidget(self.centralwidget)
    

    def timer_start(self):
        self.timer_int = DURATION
        self.myqtimer = QtCore.QTimer(self)
        self.myqtimer.timeout.connect(self.timer_timeout)
        self.myqtimer.start(1000)
        self.update_gui()
    
    def timer_timeout(self):
        self.timer_int -= 1
        if self.timer_int==-1:
            self.setWindowTitle("")
            self.close()
        self.update_gui()

    def update_gui(self):
        self.infoLabel.setText("The window will be automatically closed in "+str(self.timer_int))

    def closeWindow(self):
        self.myqtimer.stop()
        self.close()

    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Window5", "MainWindow"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Window5()
    ui.setupUi(1)
    ui.show()
    sys.exit(app.exec_())

