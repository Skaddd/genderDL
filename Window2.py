#Created by Mateo LEBRUN



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap #
from PyQt5.QtWidgets import QMainWindow
import cv2
import source # to add background image we use the source.py
import time
import glob
import os

from predict import prediction # used this method calls the pre-trained models
 #was to bored to recreate a variable, just the current date with hours and minutes
from Window3 import Ui_Window3
from Window4 import Ui_Window4

global TIMER
TIMER = int(5) 

class Ui_Window2(QMainWindow):

    def __init__(self):
        super(Ui_Window2,self).__init__()

    # Same thing, we create a method that will open the Window3 and setups all its buttons signals
    def openWindow3(self):
        self.stoploop =1
        self.imgLabel.clear()
        self.ui2= Ui_Window3()
        self.ui2.setupUi(self.language) #
        self.ui2.show()
        #self.window.showFullScreen() #
        self.ui2.backBut2.clicked.connect(lambda :self.ui2.close()) #just closing the window when the buttont back from the window2 is called

    #Same with Window4
    def openWindow4(self):
        self.stoploop =1
        self.imgLabel.clear()
        self.ui4 = Ui_Window4()
        self.ui4.setupUi(self.language)
        self.ui4.show()
        #self.win.showFullScreen()
        #the methods called are explained in their respective file
        self.ui4.backBut.clicked.connect(lambda : self.ui4.leavingWin())
        self.ui4.captureBut.clicked.connect(lambda : self.ui4.launchCamera(TIMER))
        self.ui4.screenBut.clicked.connect(lambda : self.ui4.takePicture())
        self.ui4.transferBut.clicked.connect(lambda : self.ui4.displayTransfer())
        for k in range (self.ui4.img_len):
            self.ui4.buttons[(k)].clicked.connect(self.ui4.make_callback(k))

    def setupUi(self,lang):
        self.language =lang
        self.setObjectName("Window2")
        self.resize(1920, 1080)
        width = self.width()
        #for the three next variables we will see later why we need them
        self.logic =1
        self.value =0
        self.stoploop = 0
        self.timer = 180000
        self.centralwidget = QtWidgets.QWidget(self)
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
        #Title label
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(width/4, 20, 1200, 61))
        self.titlelabel.setTextFormat(QtCore.Qt.RichText)
        self.titlelabel.setScaledContents(True)
        self.titlelabel.setAlignment(QtCore.Qt.AlignCenter)
        self.titlelabel.setObjectName("titlelabel")
        self.titlelabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.titlelabel.setStyleSheet(
            "font: 32pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")
        # We want to keep the background image as a global background , thus most of Layouts or Widgets avec transparent background

        self.infoLab = QtWidgets.QLabel(self.centralwidget)
        self.infoLab.setGeometry(QtCore.QRect(40, 570, 1100, 141))
        
        self.infoLab.setObjectName("infoLab")
        self.infoLab.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.infoLab.setStyleSheet(
            "font: italic 13pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")



        self.waitingLabel=QtWidgets.QLabel(self.centralwidget)
        self.waitingLabel.setGeometry(QtCore.QRect(40,800,500,101))
        self.waitingLabel.setTextFormat(QtCore.Qt.RichText)
        self.waitingLabel.setObjectName("infoLab")
        self.waitingLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.waitingLabel.setStyleSheet(
            "font: italic 13pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")


        #To display the camera output and results from prediciton we create a Label that will store images
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(40, 130, 581, 421))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.imgLabel.setLineWidth(6)
        self.imgLabel.setMidLineWidth(0)
        self.imgLabel.setStyleSheet("boder-radius : 10px;")
        self.imgLabel.setObjectName("imgLabel")

        # Same as before, we create a frame to place proprely our buttons
        self.lowerframe = QtWidgets.QFrame(self.centralwidget)
        self.lowerframe.setGeometry(QtCore.QRect(30,950, 1900, 91))
        self.lowerframe.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.lowerframe.setObjectName("lowerframe")

        self.captureBut = QtWidgets.QPushButton(self.lowerframe)
        self.captureBut.setGeometry(QtCore.QRect(20, 30, 201, 41))
        self.captureBut.setMouseTracking(True)
        self.captureBut.setObjectName("captureBut")


        self.screenBut = QtWidgets.QPushButton(self.lowerframe)
        self.screenBut.setGeometry(QtCore.QRect(300, 30, 201, 41))
        self.screenBut.setMouseTracking(True)
        self.screenBut.setObjectName("screenBut")


        self.infoBut = QtWidgets.QPushButton(self.centralwidget)
        self.infoBut.setGeometry(QtCore.QRect(40, 750, 201, 41))
        self.infoBut.setObjectName("infoBut")


        self.moreBut = QtWidgets.QPushButton(self.lowerframe)
        self.moreBut.setGeometry(QtCore.QRect(900,30,201,41))
        self.moreBut.setObjectName("moreBut")


        self.backbut = QtWidgets.QPushButton(self.lowerframe)
        self.backbut.setGeometry(QtCore.QRect(1750, 30, 110, 41))
        self.backbut.setMouseTracking(True)
        icon = QtGui.QIcon('assets/r.png')
        self.backbut.setIcon(icon)
        self.backbut.setIconSize(QtCore.QSize(30,25))
        self.backbut.setObjectName("backbut")

        if self.language==0:
            self.titlelabel.setText( "Intelligence artificielle qui prédit le sexe et l'âge")
            self.captureBut.setText("Camera")
            self.infoBut.setText( "Comment ça marche?")
            self.backbut.setText( "retour")
            self.screenBut.setText("Prendre Photo")
            self.infoLab.setText("L'IA va essayer de deviner votre sexe et votre age!\nMais il a besoin d'image de vous! Lancer la camera avec le bon bouton. Ensuite, quand tu es prêt prend une photo \nLa photo sera prise dans 5 secondes après avoir appuer sur le bouton.\nA partir de cette photo, l'IA va predire plus ou moins précisement ton age et ton genre! \nPour compendre ce qui s'est passé ou pourquoi les résults sont correctes, ou pas ...Appuyer sur le bouton en-dessous! \nEnvie d'essayer d'autre chose? Appuyer le bouton  Autre Jeu! ")
            self.moreBut.setText("Autre Jeu")

        elif self.language==1:
            self.titlelabel.setText("Artifical Intelligence Performing Gender and Age prediction")
            self.captureBut.setText("Capture")
            self.infoBut.setText("How it Works?")
            self.backbut.setText("back")
            self.screenBut.setText("Take picture")
            self.infoLab.setText("The AI is going to guess your age and your gender!\n"
            "But it needs a picture of you! So launch the camera with the button caputre. Then, when you are ready press the Screen button,\n"
            "a photo of you will be saved within 5 seconds.\n"
            "From this image, the AI will predicit more or less correctly your age and gender!\n"
            "To understand what happened or why the results are so good! or so bad... press the button below!\n"
            "Want to try something else? press the  Play More button! ")
            self.moreBut.setText("Play more!")

                
        elif self.language==2:
                pass

        else:
            pass

        
        self.qtim = QtCore.QTimer()
        self.qtim.start(self.timer)
        self.qtim.timeout.connect(self.close)


        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    

            
    



    #this method, binded to the backButton enables to go back to the previous window we were
    #to increase the robustness, we added a variable that will trigger the camera's stop if it was still on 
    def leavingWin(self):
        self.stoploop =1
        self.imgLabel.clear()
        self.close()

    # this metohd increment the logic value , and will let us know when someone wants to take a picture, this method is called when the button Take Picture is pressed
    def takePicture(self):
        
        self.logic+=1

    # this method launch the camera and is called by the button Capture
    def launchCam(self,TIMER):
        self.waitingLabel.setText("The Camera is launched""\n Once you take a picture, it will take some time to show the result !")
        self.stoploop=0
        self.logic=1 # preventing people pressing take picture before launch camera
        cam=cv2.VideoCapture(0) # take the camera stream
        self.imgLabel.clear() 
        while (cam.isOpened()  and self.stoploop==0) : # while the camera is open
            ret, img = cam.read() # read images
            if ret == True :
                self.displayImage(img) # using the method displayImage that just display the image in the label imgLabel
                cv2.waitKey()

            if (self.logic==2): #the logic value is incremented when someone is pressing the button Take Picture
                self.logic=1
                prev = time.time() # we store the current time
  
                while TIMER >= 0: # delaying the photo by TIMER seconds
                    ret, img = cam.read()
                    self.displayImage(img)
                    cv2.waitKey() 
                    cur = time.time() 
   
                    if cur-prev >= 1: # just to decrement the TIMER value to 0
                        prev = cur 
                        TIMER = TIMER-1
                else : # while else is a loop in python!
                    date=time.strftime("%Y-%m-%d-%H-%M")
                    cv2.imwrite('portrait/im-'+date+'.jpg',img)
                    cv2.waitKey(125) # Thus after 5 seconds we saves the last image
                    self.imgLabel.clear() # clearing the label that contains the image
                    self.value+=1 # this value enables us to know whether or not someone took a picture
                    
                    break # since we took the wanted picture we stop the loop

                                           
        cam.release() # stop the camera stream /or unbinding the camera
        cv2.destroyAllWindows() 
        self.imgLabel.clear()

        if self.value != 0 : # to prevent problem the method displayResults can be called only if someone took a picture before
            
            self.displayResults() # then we display the results in the image Label
            self.waitingLabel.setText("Done!")
        else : 
            pass
        
    #method that display an image in the imgLabel, we use  the opencv lib to get the camera stream, 
    #however this lib returns BGR images so we read the image with the same pattern then swap to rbg
    # and create a Pixmap and add it to the label 
    def displayImage(self,img): 
        qformat = QImage.Format_Indexed8 
        if (len(img.shape)==3): 
            if(img.shape[2])==4: 
                qformat=QImage.Format_BGRA888 
            else : 
                qformat=QImage.Format_BGR888 
            img = QImage(img,img.shape[1],img.shape[0],qformat) 
            img.rgbSwapped() 
            self.imgLabel.setPixmap(QPixmap.fromImage(img)) 
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) 

    #We apply to the last image taken the models  
    def displayResults(self):
        
        path = os.path.join("portrait","*")
        list_images = glob.glob(path)
        latest_img = max(list_images,key=os.path.getctime) # we want to apply the models to the last image taken so we browse the folder to find it
        print(latest_img)
        prediction(latest_img)# we apply the models calling the prediction function from predict.py(cropping + face align then applying models)
        img_dir = os.path.join('detection','images','detected','*')
        list_of_files = glob.glob(img_dir) 
        latest_file = max(list_of_files, key=os.path.getctime) # we extract the image that display on it the predictions
        print (latest_file)
        if latest_file.endswith(".png"):
            img=cv2.imread(latest_file)
            self.displayImage(img) 
            # we call the method to display the image




    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Window2", "MainWindow"))
        




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sys.exit(app.exec_())
