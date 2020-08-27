#Created by Mateo LEBRUN

"""
Important Information about about translation :
lang == 2 means that the text must be written in Deutsch
lang== 3 means that the text must be written in Portuguese
else means that the text must be written in Lux

"""


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap, QMovie, QColor
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize

import math
import cv2
import source 
import time
import glob
import os
import shutil

#prediction is a method that calls the pre-trained models

from predict import prediction

#We will call the follow windows from window2 so we need to import the classes to get the acces

from Window3 import Ui_Window3
from Window4 import Ui_Window4

#timer beofre taking a picture
global TIMER
TIMER = int(5) 

class Ui_Window2(QMainWindow):

    def __init__(self):
        super(Ui_Window2,self).__init__()

    # this method will open window3 by calling the setupUi from the Ui_Window3
    #every signals are also setup up with the corresponding slots( buttons,etc)
    #clearing the imglabel is also a plus 
    #Because Qtimer are always running in background, in order to close automacially windows, when we open window3 from window2
    #we don't want the window2 to close itself, so we restart the timer with a big value
    def openWindow3(self):
        self.reset_values()
        self.timer = 1200000
        self.qtim.start(self.timer)
        self.imgLabel.clear()
        self.ui2= Ui_Window3()
        self.ui2.setupUi(self.language) #
        self.ui2.show()
        #self.window.showFullScreen() #
        self.ui2.backBut2.clicked.connect(lambda :self.ui2.close())
        self.ui2.easyBut.clicked.connect(lambda :self.ui2.displayEasy(self.language))
        self.ui2.normalBut.clicked.connect(lambda : self.ui2.displayNormal(self.language))
        self.ui2.advancedBut.clicked.connect(lambda : self.ui2.displayAdvanced(self.language))
        self.ui2.expertBut.clicked.connect(lambda : self.ui2.displayExpert(self.language))
        self.ui2.InsideBut.clicked.connect(lambda :self.ui2.createGif())
        self.ui2.InsideBut2.clicked.connect(lambda : self.ui2.displayGif())

    #Same with Window4
    def openWindow4(self):
        self.timer = 1200000
        self.qtim.start(self.timer)
        self.reset_values()
        self.imgLabel.clear()
        self.ui4 = Ui_Window4()
        self.ui4.setupUi(self.language)
        self.ui4.show()
        #self.win.showFullScreen()
        self.ui4.backBut.clicked.connect(lambda : self.ui4.leavingWin())
        self.ui4.captureBut.clicked.connect(lambda : self.ui4.launchCamera(TIMER))
        self.ui4.screenBut.clicked.connect(lambda : self.ui4.takePicture())
        self.ui4.transferBut.clicked.connect(lambda : self.ui4.displayTransfer())
        for k in range (self.ui4.img_len):
            self.ui4.buttons[(k)].clicked.connect(self.ui4.make_callback(k))

   

    #This method  setups  everything inside the window2
    #language will be used to display the text in the right language
    #There we have a title label, 4 buttons in a frame, 2text label separeted by a button and finally a label with pixmap to display the camera output
    # We want to keep the background image as a global background , thus most of Layouts or Widgets have transparent background
    #We initialize the timer variable that we will use later to close automatically the window
    #This window contains a lot of widgets and layouts,
    def setupUi(self,lang):
        self.language =lang
        self.setObjectName("Window2")
        self.resize(1920, 1080)
        width = self.width()
        self.timer = 300000
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
        


        self.frameInfo = QtWidgets.QFrame(self.centralwidget)
        self.frameInfo.setGeometry(QtCore.QRect(650, 160, 1250, 450))
        self.frameInfo.setObjectName("frameInfo")

        self.gridLayout_frameInfo = QtWidgets.QGridLayout(self.frameInfo)
        self.gridLayout_frameInfo.setObjectName("gridLayout_frameInfo")


        self.HBoxBottom=QtWidgets.QHBoxLayout()
        self.HBoxBottom.setObjectName("HBoxBottom")

        self.waitingLabel2=QtWidgets.QLabel(self.frameInfo)
        self.waitingLabel2.setObjectName("waitingLabel2")
        self.waitingLabel2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.waitingLabel2.setStyleSheet(
            "font: italic  25pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")

            

        self.infoBut = QtWidgets.QPushButton(self.frameInfo)
        self.infoBut.setObjectName("infoBut")
        self.infoBut.setFixedSize(QSize(201,41))


        self.HBoxBottom.addWidget(self.waitingLabel2)
        self.HBoxBottom.addWidget(self.infoBut,alignment=QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
        

        self.gridLayout_frameInfo.addLayout(self.HBoxBottom, 1, 0, 1, 1)

        self.vBoxTop = QtWidgets.QVBoxLayout()
        self.vBoxTop.setObjectName("vBoxTop")

        self.infoLab = QtWidgets.QLabel(self.frameInfo)
        self.infoLab.setObjectName("infoLab")
        self.infoLab.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.infoLab.setAlignment(QtCore.Qt.AlignTop | QtCore.Qt.AlignLeft)
        self.infoLab.setStyleSheet(
            "font: italic 18pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")


        self.vBoxTop.addWidget(self.infoLab)
        self.gridLayout_frameInfo.addLayout(self.vBoxTop, 0, 0, 1, 1)


        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(40, 130, 581, 421))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.imgLabel.setLineWidth(6)
        self.imgLabel.setMidLineWidth(0)
        self.imgLabel.setObjectName("imgLabel")

        self.resultLabel = QtWidgets.QLabel(self.centralwidget)
        self.resultLabel.setGeometry(QtCore.QRect(40,550,600,60))
        self.resultLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.resultLabel.setObjectName("resultLabel")
        self.resultLabel.setStyleSheet(
            "font: italic 14pt \"Adobe Pi Std\";\n"
            "color: rgb(119,181,254);"
        )

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



        self.framekeep = QtWidgets.QFrame(self.centralwidget)
        self.framekeep.setGeometry(QtCore.QRect(30,650,700,150))
        self.framekeep.setObjectName("framekeep")
        self.framekeep.hide()

        self.VLayout_framekeep = QtWidgets.QVBoxLayout(self.framekeep)
        self.VLayout_framekeep.setObjectName("gridLayout_keepframe")


        self.keepPhotoBut = QtWidgets.QPushButton(self.framekeep)
        self.keepPhotoBut.setObjectName("keepPhotoBut")

        self.keepPhotoBut.setText("Sauvegarder")
        self.keepPhotoBut.setFixedSize(QSize(141,41))



        self.KeepLabel = QtWidgets.QLabel(self.framekeep)
        self.KeepLabel.setObjectName("keepLabel")
        self.KeepLabel.setStyleSheet(
            "font: italic 14pt \"Adobe Pi Std\";\n"
            "color: rgb(255,255,255);"
        )

        self.VLayout_framekeep.addWidget(self.keepPhotoBut)
        self.VLayout_framekeep.addWidget(self.KeepLabel)
        

        if self.language==0:
            self.titlelabel.setText( "Intelligence artificielle qui prédit le sexe et l'âge")
            self.captureBut.setText("Camera")
            self.infoBut.setText( "Comment ça marche?")
            self.backbut.setText( "retour")
            self.screenBut.setText("Prendre Photo")
            self.infoLab.setText(
                "1. L'IA va essayer de deviner votre sexe et votre age!\n"
                "2. Lancez la camera avec le bon bouton\n"
                "3. Regarder bien la camera et prenez une photo de vous! La photo sera prise dans 5 secondes.\n"
                "4. Directement après l'Intelligence artificielle va predire plus ou moins précisement ton age et ton genre! \n"
                "5. Cela peut prendre un peu de temps...\n"
                "6. Pour compendre ce qui s'est passé et les résults obtenus, appuie sur le bouton en-dessous! \n"
                "7. Envie d'essayer d'autre chose? Appuyez sur le bouton  Autre Jeu! ")
            self.moreBut.setText("Autre Jeu")
            self.KeepLabel.setText(
                "Contribuer à nos projets d'intelligence artificielle en sauvegardant votre image.\n"
                "Elle ne sera utilisée que par le Science Center et seulement à des fins de recherches.\n"
                "Autrement l'image sera automatiquement supprimée"
            )
            

        elif self.language==1:
            self.titlelabel.setText("Artifical Intelligence Performing Gender and Age prediction")
            self.captureBut.setText("Capture")
            self.infoBut.setText("How it Works?")
            self.backbut.setText("back")
            self.screenBut.setText("Take picture")
            self.infoLab.setText(
                "1. The AI is going to guess your age and your gender!\n"
                "2. But it needs a picture of you! So launch the camera with the button caputre.\n"
                "3. Look the camera then take a picture when you are ready. The photo will be saved within 5 seconds.\n"
                "4. From this image, the AI will predicit more or less correctly your age and gender!\n"
                "5. This process might take some time, be patient...\n"
                "5. To understand what happened or why the results are so good! or so bad... press the button below!\n"
                "6. Want to try something else? press the  Play More button! ")
            self.moreBut.setText("Play more!")
            self.KeepLabel.setText(
                "Contribute to our AI projects by saving your image to our database\n"
                "It will be only used by the Sciencer Center and only for research purpose\n"
                "Otherwise the picture will be discarded automtically"
            )

                
        elif self.language==2:
        
            self.titlelabel.setText("")
            self.captureBut.setText("")
            self.infoBut.setText("")
            self.backbut.setText("")
            self.screenBut.setText("")
            self.infoLab.setText("")
            self.moreBut.setText("")
            self.KeepLabel.setText("")
        elif self.language==3:
            self.titlelabel.setText("")
            self.captureBut.setText("")
            self.infoBut.setText("")
            self.backbut.setText("")
            self.screenBut.setText("")
            self.infoLab.setText("")
            self.moreBut.setText("")
            self.KeepLabel.setText("")
            pass
        else:
            self.titlelabel.setText("")
            self.captureBut.setText("")
            self.infoBut.setText("")
            self.backbut.setText("")
            self.screenBut.setText("")
            self.infoLab.setText("")
            self.moreBut.setText("")
            self.KeepLabel.setText("")
            pass

        self.reset_values()

        #we create a QTimer object which will play its role as a timer and send signal when hitting 0s. Thus we will be able to close the window
        self.qtim = QtCore.QTimer(self.centralwidget)
        self.qtim.start(self.timer)
        self.qtim.timeout.connect(self.close)


        #We need to know when buttons are clicked on this window for the addtimer method

        self.captureBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.screenBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.infoBut.clicked.connect(lambda : self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))

        
        
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    #This method prevents a lot of bottleneck problems
    #the stoploop is used to traceback the current state of the camera so we can close it when we change window
    #the logic value is used to know when a picture must be taken, so screenBut only works if someone took a picture
    #and self.value to make it more robust 
    #face detect is used to know if the face_detection algoritm was able to detect faces from the image taken
    #we also clear labels because we don't want to keep displayed the previous results
    def reset_values(self):
        
        self.logic =1
        self.value =0
        self.stoploop = 1
        self.facedetec =0
        
        self.imgLabel.clear()
        self.framekeep.hide()
        self.resultLabel.setText("")
        self.waitingLabel2.setText("")
 
    #This method concerns the Qtimer, because we wanted to build something more complex, every time someone presses a button or just the screen
    #the Qtimer will restart
    def addtimer(self):
        print(self.qtim.remainingTime())
        if  self.qtim.remainingTime() <= 1200000:
            new_timer = 600000
            self.qtim.setInterval(new_timer)
            self.qtim.start()

    

    #This method will allow us to know if someone clicked on the window or buttons, to know is someone is using actively the app,
    #if not the timer will hit 0 and close the window
    def mousePressEvent(self,event):
        if event == QtGui.QMouseEvent.MouseButtonPress:
            self.addtimer()
            
        else : 
            self.addtimer()


    #this method, binded to the backButton enables to go back to the previous window we were
    def leavingWin(self):
        self.reset_values()
        self.close()

    # this metohd increment the logic value , and will let us know when someone wants to take a picture
    def takePicture(self):
        self.disableBut()
        self.logic+=1


    #This method blocks the buttons action and is mainly used when a photo is taken, and helps preventing problems
    def disableBut(self):
        self.moreBut.setEnabled(False)
        self.captureBut.setEnabled(False)
        self.infoBut.setEnabled(False)
        self.backbut.setEnabled(False)
    #Once the buttons are disabled we need to active them back
    def enableBut(self):
        self.moreBut.setEnabled(True)
        self.captureBut.setEnabled(True)
        self.infoBut.setEnabled(True)
        self.backbut.setEnabled(True)

    #This method launch the camera with cv2
    #while the camera is open we read and display the images
    #When someone wants to take a photo a countdown is displayed, then at the end a photo is taken and displayed by calling the DisplayImg() method
    #If faces are found we call the displayResults() method after clearing the label
    #A Quick message to ask client to wait is also added
    def launchCam(self,TIMER):
        self.removeImg()
        font = cv2.FONT_HERSHEY_SIMPLEX
        self.reset_values()
        self.stoploop=0
        cam=cv2.VideoCapture(0) 
        
        while (cam.isOpened()  and self.stoploop==0) : 
            ret, img = cam.read() 
            if ret == True :
                self.displayImage(img) 
                cv2.waitKey()

            if (self.logic==2): 
                self.logic=1
                prev = time.time() 
  
                while TIMER >= 0: # delaying the photo by TIMER seconds
                    ret, img = cam.read()
                    if TIMER== 0:
                        pass
                    else: 
                        cv2.putText(img, str(TIMER),  
                            (100, 125), font, 
                            2, (105, 105, 105), 
                            4, cv2.LINE_AA)
                    self.displayImage(img)
                    cv2.waitKey() 
                    cur = time.time() 
                    if cur-prev >= 1: 
                        prev = cur 
                        TIMER = TIMER-1
                else : # while else is a loop in python!
                    date=time.strftime("%Y-%m-%d-%H-%M %S")
                    cv2.imwrite('portrait/im-'+date+'.jpg',img)
                    if self.language==0:
                        self.waitingLabel2.setText("PATIENTEZ..")
                    elif self.language==1:
                        self.waitingLabel2.setText("WAIT..")
                        pass
                    elif self.language==2:
                        pass
                    elif self.language==3:
                        pass
                    else:
                        pass
                    
                    self.waitingLabel2.update()
                    cv2.waitKey(125) 
                    self.imgLabel.clear()
                    self.value+=1 # this value enables us to know whether or not someone took a picture
                    
                    break 

                                           
        cam.release() 
        cv2.destroyAllWindows() 
        self.imgLabel.clear()
        if self.value != 0 : # to prevent problem, the method displayResults can be called only if someone took a picture before
            
            self.displayResults()
            cv2.waitKey(1000) # then we display the results in the image Label
            self.enableBut()
            if self.facedetec==1:
                self.waitingLabel2.setText("No faces found")
                self.waitingLabel2.update()
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


    #This method will look for the last image taken
    #Then call the prediction method that loads model and evalute images
    
    #because the last picutre might not contain faces we use try catch, to get the Exception is no faces were found and update the face_detec variable
    #If faces are found we finally display the resulting image is displayed and prediction pourcentage are also given.
    def displayResults(self):
        
        path = os.path.join("portrait","*")
        list_images = glob.glob(path)
        latest_img = max(list_images,key=os.path.getctime) 
        try :
            age_deteced,gender_detected =prediction(latest_img)
            age_deteced=[math.floor(k*100) for k in age_deteced]
            for k in range(len(gender_detected)):
                gen = gender_detected[k]
                if gen< 0.5:
                    gen = math.floor((1-gen)*100)
                else :
                    gen = math.floor(gen*100)
                gender_detected[k]=gen
            
            img_dir = os.path.join('detection','images','detected','*')
            list_of_files = glob.glob(img_dir) 
            latest_file = max(list_of_files, key=os.path.getctime)

            if latest_file.endswith(".png"):
                img=cv2.imread(latest_file)
                self.displayImage(img)
            if self.language==0:

                self.resultLabel.setText(f" L'IA prédit à {gender_detected} % de confiance votre genre \net à {age_deteced} % de confiance votre age ")

            elif self.language==1:

                self.resultLabel.setText(f" The IA predicts your gender with {gender_detected} % of confidence\nand your age with {age_deteced} % of confidence ")

            elif self.language==2:

                self.resultLabel.setText(f" The IA predicts your gender with {gender_detected} % of confidence\nand your age with {age_deteced} % of confidence ")

            elif self.language==3:

                self.resultLabel.setText(f" The IA predicts your gender with {gender_detected} % of confidence\nand your age with {age_deteced} % of confidence ")

            else :

                self.resultLabel.setText(f" The IA predicts your gender with {gender_detected} % of confidence\nand your age with {age_deteced} % of confidence ")
            self.framekeep.show()
        except Exception :
            self.facedetec = 1
            os.remove(latest_img)
        

    #This method is used to save images, after an image is taken we ask to the client if they accept the LSC to keep it
    #We obviously don't want to save an image without faces
    #we basically save the raw image, the result image and the aligned faces from the raw image
    def saveImg(self):
        tmp_path = os.path.join('detection','images','aligned','tmp','*.png')
        list_tmp = glob.glob(tmp_path)
        print(list_tmp)
        for file in list_tmp:
            shutil.copy(file,os.path.join('detection','images','aligned','saved',''))
            
        

        if self.facedetec==0:    
            portrait_path = os.path.join("portrait","*.jpg")
            list_portrait = glob.glob(portrait_path)
            latest_portrait = max(list_portrait,key=os.path.getctime)
            shutil.copy(latest_portrait,os.path.join('portrait','saved',''))
        else: 
            pass
        
        detected_path = os.path.join('detection','images','detected','*.png')
        list_detected=glob.glob(detected_path)
        latest_detected = max(list_detected,key=os.path.getctime)
        shutil.copy(latest_detected,os.path.join('detection','images','detected','saved',''))

    #This method allow us to remove the last image taken automatically if the client doesn't activly save its image
    def removeImg(self):
        if self.facedetec==0:
                
            portrait_path = os.path.join("portrait","*.jpg")
            list_portrait = glob.glob(portrait_path)
            print(list_portrait)
            if not list_portrait:
                pass   
            else :
                latest_portrait = max(list_portrait,key=os.path.getctime)
                os.remove(latest_portrait)
            
            detected_path = os.path.join('detection','images','detected','*.png')
            list_detected=glob.glob(detected_path)
            if not list_detected:
                pass
            else :
                latest_detected = max(list_detected,key=os.path.getctime)
                os.remove(latest_detected)

        else :
            pass

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Window2", "MainWindow"))
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Window2()
    ui.setupUi(lang=1)
    ui.show()
    sys.exit(app.exec_())
