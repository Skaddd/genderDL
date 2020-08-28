#Created by Mateo LEBRUN

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap,QMovie,QColor
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QSize
import source
import glob
import os
import cv2
import time
from Window5 import Ui_Window5
from transfer_im import crop_center,load_image,styleT 
# functions that apply the style transfer model to a given image



class Ui_Window4(QMainWindow):

    def __init__(self):
        super(Ui_Window4,self).__init__()




    def openWindow5(self):
        self.qtim.stop()
        self.ui5=Ui_Window5()
        self.ui5.setupUi(self.language)
        self.ui5.show()
        self.ui5.stayBut.clicked.connect(lambda : self.ui5.closeWindow())
        reset_timer = 300000 
        self.ui5.stayBut.clicked.connect(lambda : self.qtim.start(reset_timer))
        self.ui5.leaveBut.clicked.connect(lambda : self.ui5.closeWindow())
        self.ui5.leaveBut.clicked.connect(lambda : self.close())
        self.ui5.windowTitleChanged.connect(lambda :self.close())



    #we used alot of concepts already explained,
    #we added a namestyle variable to know when a style is selected or not
    #this method contains a huge part of object positioning (frames, layout ,...)
    def setupUi(self,lang):
        self.setObjectName("Window4")
        #self.resize(1920, 1080)
        self.setAnimated(True)
        self.language = lang
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
            "QScrollBar:horizontal{"
                "height: 20px;"
                "margin: 3px 15px 3px 15px;"
                "border-radius: 4px;"
                "border: 1px transparent;"
                "background-color: black;}"

            "QScrollBar::handle:horizontal{"
                "background-color: gray;"
                "min-width: 5px;"
                "border-radius: 4px;}"
            "QScrollBar::add-line:horizontal{"
                "margin : 0px 3px 0px 3px;"
                "border-image: url(:/qss_icons/rc/right_arrow_disabled.png);"
                "width: 10px;"
                "height: 10px;}"
            "QScrollBar::sub-line:horizontal{"
                    "border-image: url(:/qss_icons/rc/left_arrow.png);"
                    "height: 10px;"
                    "width: 10px;}"

            "QScrollBar::up-arrow:horizontal,QScrollBar::down-arrow:horizontal {"
                "background : none;}"
            "QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{"
                "background: none;}"
            "#centralwidget{background-image: url(:/images/assets/back1.jpg); background-repeat = no-repeat; background-position = center};")

        self.logic =1
        self.value =0
        self.stoploop=0
        self.timer = 600000
        
        self.namestyle=""
        self.labeltitle = QtWidgets.QLabel(self.centralwidget)
        self.labeltitle.setGeometry(QtCore.QRect(50, 30, 1121, 61))
        self.labeltitle.setObjectName("titlelabel")
        self.labeltitle.setStyleSheet(
            "font: 28pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")
        self.labeltitle.setTextFormat(QtCore.Qt.RichText)
        self.labeltitle.setScaledContents(True)
        self.labeltitle.setAlignment(QtCore.Qt.AlignCenter)
        self.labeltitle.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        #Box containing the camera output and images
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(1200, 100, 512, 450))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.imgLabel.setLineWidth(6)
        self.imgLabel.setMidLineWidth(0)
        self.imgLabel.setText("")
        self.imgLabel.setObjectName("imgLabel")


        #Frame to put buttons
        self.frameLeft=QtWidgets.QFrame(self.centralwidget)
        self.frameLeft.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frameLeft.setObjectName("frameLeft")
        self.frameLeft.setGeometry(QtCore.QRect(1100,600,800,250))
        
        self.gridframe=QtWidgets.QGridLayout(self.frameLeft)
        self.gridframe.setObjectName("gridframe")

        self.VBoxtop = QtWidgets.QVBoxLayout()
        self.VBoxtop.setObjectName("VBoxtop")
        self.VBoxbot=QtWidgets.QVBoxLayout()
        self.VBoxbot.setObjectName("VBoxbot")
        

        self.HBoxtop = QtWidgets.QHBoxLayout()
        self.HBoxtop.setObjectName("HBoxtop")
        self.HBoxtop.setSpacing(110)
        


        self.captureBut = QtWidgets.QPushButton(self.frameLeft)
        self.captureBut.setFixedSize(QSize(141,41))
        self.captureBut.setMouseTracking(True)
        self.captureBut.setObjectName("captureBut")

        self.screenBut = QtWidgets.QPushButton(self.frameLeft)
        self.screenBut.setFixedSize(QSize(141,41))
        self.screenBut.setMouseTracking(True)
        self.screenBut.setObjectName("screenBut")


        self.transferBut = QtWidgets.QPushButton(self.frameLeft)
        self.transferBut.setFixedSize(QSize(141,41))
        self.transferBut.setMouseTracking(True)
        self.transferBut.setObjectName("transferBut")

        self.waitingLabel = QtWidgets.QLabel(self.frameLeft)
        self.waitingLabel.setAlignment(QtCore.Qt.AlignLeft| QtCore.Qt.AlignVCenter)
        self.gif=QMovie('assets/load6.gif')
        self.gif.setScaledSize(QSize(400,300))
        self.gif.setBackgroundColor(QColor("transparent"))
        self.waitingLabel.setMovie(self.gif)
        

        self.waitingLabel2=QtWidgets.QLabel(self.frameLeft)
        self.waitingLabel2.setObjectName("waitingLabel2")
        self.waitingLabel2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.waitingLabel2.setStyleSheet(
            "font: italic  18pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")
        self.waitingLabel2.hide()
        

        self.HBoxtop.addWidget(self.captureBut)
        self.HBoxtop.addWidget(self.screenBut)
        self.HBoxtop.addWidget(self.transferBut)

        self.VBoxtop.addLayout(self.HBoxtop)
        self.gridframe.addLayout(self.VBoxtop,0,0,1,1)

        self.VBoxbot.addWidget(self.waitingLabel, alignment=QtCore.Qt.AlignVCenter |QtCore.Qt.AlignHCenter )
        self.VBoxbot.addWidget(self.waitingLabel2, alignment=QtCore.Qt.AlignVCenter |QtCore.Qt.AlignHCenter )
    
        self.gridframe.addLayout(self.VBoxbot,1,0,1,1)



        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(30, 680, 1100, 300))
        self.infoLabel.setStyleSheet(
            "font: italic 16pt \"Adobe Pi Std\";\n"
            "color: rgb(255, 255, 255);")
        
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.infoLabel.setAlignment(QtCore.Qt.AlignLeft)


        ### All this part focuses on the image style browser,
        ### To sum it up we created a frame with a Grid Layout,
        ### Inside we added a ScrollArea(+Scrollareacontent)
        ###Which Inside we created a frame with a Grid Layout
        ### And for each style images this frame contains a HBox and a PushButton, the HBox will contains a Label that show the Image and the Button to select the image

        self.frameScroll = QtWidgets.QFrame(self.centralwidget)
        self.frameScroll.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frameScroll.setGeometry(QtCore.QRect(20, 250, 1000, 400))
        self.frameScroll.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameScroll.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameScroll.setObjectName("frameScroll")


        self.gridLayout = QtWidgets.QGridLayout(self.frameScroll)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        

        self.scrollArea = QtWidgets.QScrollArea(self.frameScroll)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.scrollArea.setStyleSheet("background-color:transparent;")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-22, 0, 842, 268))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_Scrollarea = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_Scrollarea.setObjectName("gridLayout_Scrollarea")
        
        self.frame = QtWidgets.QFrame(self.scrollAreaWidgetContents)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setAttribute(QtCore.Qt.WA_TranslucentBackground)



        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.buttons={}
        self.images =[]

        #We search all the style images and get the total length
        for file in glob.glob("pictures/*.*g"):
            self.images.append(file)
        self.img_len = len(self.images)
        for k in range (self.img_len):
            name_but=os.path.basename(self.images[k])
            name_but=name_but[:name_but.find('.')]
            #print(name_but)
            horizontalLayout = QtWidgets.QHBoxLayout()
            QLabel=QtWidgets.QLabel(self.frame)
            QLabel.setFixedHeight(150)
            image_data=self.images[k]

            if image_data ==None:
                print("Image non trouvée")
            else :
                self.pix =QPixmap()
                self.pix.load(self.images[k])
            self.pix = self.pix.scaled(256, 256, QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation)
            QLabel.setPixmap(self.pix)
            horizontalLayout.addWidget(QLabel)
            self.buttons[(k)] = QtWidgets.QPushButton(name_but,self.frame)
            self.buttons[(k)].setFlat(True)   
            self.buttons[(k)].setCheckable(True)
            self.buttons[(k)].clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))

            
            self.gridLayout_4.addLayout(horizontalLayout, 1, k, 1, 1)
            self.gridLayout_4.addWidget(self.buttons[(k)], 2, k, 1, 1)

        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_Scrollarea.addWidget(self.frame, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.scrollArea, 0, 1, 1, 1)


        ###
        ###

        #button to return to the previous Window
        self.backBut= QtWidgets.QPushButton(self.centralwidget)
        self.backBut.setGeometry(QtCore.QRect(1780,980,110,41))
        self.backBut.setObjectName("backBut")
        icon = QtGui.QIcon('assets/r.png')
        self.backBut.setIcon(icon)
        self.backBut.setIconSize(QtCore.QSize(30,25))


        if self.language ==0:
            self.labeltitle.setText("Fusion de style avec l'intelligence artificielle")
            self.backBut.setText("retour")
            self.captureBut.setText( "Camera")
            self.screenBut.setText("Prendre photo")
            self.transferBut.setText("Application  style")
            self.infoLabel.setText(
                "1. Applique differents styles à ton image!\n"
                "2. Si tu n'as pas encore pris de photo de toi lance la camera et prend une photo quand tu es prêt!\n"
                "3. La Photo sera prise après 5 secondes.\n"
                "4. Choisi le style que tu aimes dans le catalogue d'image au dessus!\n"
                "5. Une fois que tu as choisi le style que tu veux en appuyant sur le bouton correspondant, applique le style\n"
                "6. Soit patient cela prend du temps\n"
                "7. Votre image sera automatiquement supprimée dès qu'une nouvelle photo sera prise\n")



        elif self.language==1:
            self.labeltitle.setText("Fast Style transfer with Artificial Intelligence")
            self.backBut.setText("back")
            self.captureBut.setText( "Capture")
            self.screenBut.setText("Take picture")
            self.transferBut.setText("Apply Style")
            self.infoLabel.setText(
                "1. Apply different style to your image!\n"
                "2. First if you haven't taken yet an image of yourself launch the camera with the button caputre and take a picture!\n"
                "3. It will take a photo within 5 seconds.\n"
                "4. Select a style image from the different images presented above!\n"
                "5. Once you selected your style use the button  Apply Style to see the result!\n"
                "6. Be patient, it might take some time\n"
                "7. Your image will be automatically discarded once a new photo is taken\n")

        elif self.language ==2:
            self.labeltitle.setText("")
            self.backBut.setText("")
            self.captureBut.setText("")
            self.screenBut.setText("")
            self.transferBut.setText("")
            self.infoLabel.setText("")

        elif self.language==3:
            self.labeltitle.setText("")
            self.backBut.setText("")
            self.captureBut.setText("")
            self.screenBut.setText("")
            self.transferBut.setText("")
            self.infoLabel.setText("")

        else:
            self.labeltitle.setText("")
            self.backBut.setText("")
            self.captureBut.setText("")
            self.screenBut.setText("")
            self.transferBut.setText("")
            self.infoLabel.setText("")


        
        self.captureBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.screenBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.transferBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
               
        self.qtim = QtCore.QTimer()
        self.qtim.start(self.timer)
        self.qtim.timeout.connect(self.openWindow5)
        
        self.setCentralWidget(self.centralwidget)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    

    def addtimer(self):
        if self.qtim.remainingTime() <= self.timer:
            new_timer =  450000
            self.qtim.setInterval(new_timer)
            self.qtim.start()
    

    
    def mousePressEvent(self,event):
        if event == QtGui.QMouseEvent.MouseButtonPress:
            self.addtimer()
            
        else : 
            self.addtimer()
    

    ## The tricky part, since we generate buttons in a loop it's hard to access to a unique button, in order to create unique clicked.connect methods 
    #we can't use the lambda function directly because it processed in real time (so will always the current value when pressing the bbutton, so the last value in the loop)
    #so we create a method that itself create lambdas, so for each button we have a lambda function
    def make_callback(self,k):
        return lambda : self.storeButname(k)

    def storeButname(self,k):
        self.waitingLabel2.show()
        if self.language==0:
            self.waitingLabel2.setText("Appliquer le style puis patientez...")
        elif self.language==1:
            self.waitingLabel2.setText("Apply the style then wait...")
        elif self.language ==2:
            self.waitingLabel2.setText("")
        elif  self.language==3:
            self.waitingLabel2.setText("")
        else :
            self.waitingLabel2.setText("")

        self.namestyle = self.buttons[(k)].text()

    ##

    def leavingWin(self):
        self.imgLabel.clear()
        self.stoploop=1
        self.close()

    def launchCamera(self,TIMER):
        self.waitingLabel2.hide()
        self.gif.start()
        self.logic=1
        self.stoploop=0
        font = cv2.FONT_HERSHEY_SIMPLEX
        cam=cv2.VideoCapture(0)
        self.imgLabel.clear()
        while (cam.isOpened()  and self.stoploop==0) :
            ret, img = cam.read() 
            if ret == True :
                self.displayImage(img)
                cv2.waitKey()

            if (self.logic==2):
                self.logic=1
                prev = time.time() 

                while TIMER >= 0: 
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
                else :
                    self.removeImg
                    date=time.strftime("%Y-%m-%d-%H-%M")
                    cv2.imwrite(resource_path('portrait\\im-'+date+'.jpg'),img)
                    cv2.waitKey(250)
                    self.value+=1
                    break

                                            
        cam.release()
        cv2.destroyAllWindows()
    
    def takePicture(self):
        self.logic+=1
        

    def displayImage(self,img): #
        qformat = QImage.Format_Indexed8 #
        if (len(img.shape)==3): #
            if(img.shape[2])==4: #
                qformat=QImage.Format_BGRA888 #
            else : # 
                qformat=QImage.Format_BGR888 #
            img = QImage(img,img.shape[1],img.shape[0],qformat) #
            img.rgbSwapped() #
            self.imgLabel.setPixmap(QPixmap.fromImage(img)) #
            self.imgLabel.setAlignment(QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter) #


    #pretty much the same as displayResults, we get the last image, 
    #we check that a style image was chosen thanks to the variable namestyle that will store the last button's name pressed(nameBut +jpg = path)
    def displayTransfer(self):
        self.waitingLabel2.show()
        path = os.path.join("portrait","*")
        list_images = glob.glob(resource_path(path))
        
        if self.namestyle=="" or  not list_images:
            print("you did not selected an image")
            if self.language==0:
                self.waitingLabel2.setText("Aucune image de style selectionnée / Aucune image prises")
            elif self.language==1:
                self.waitingLabel2.setText("No style image were selected / No image taken")
            elif self.langugage ==2:
                self.waitingLabel2.setText("")
            elif self.language==3:
                self.waitingLabel2.setText("")
            else:
                self.waitingLabel2.setText("")
        else :
            latest_img = max(list_images,key=os.path.getctime)
            self.stoploop=1
                    
            path_img = resource_path('pictures\\'+self.namestyle)
            if os.path.isfile(path_img+'.png'):
                path_img = path_img+'.png'
            elif os.path.isfile(path_img+'.jpg'):
                path_img = path_img+'.jpg'
            elif os.path.isfile(path+'.jpeg'):
                path_img = path_img+'.jpeg'
            else :
                print("Le type de l'image n'est pas supportée")
                return 
            styleT(latest_img,path_img)
            im_transfer = cv2.imread('transfer.jpg')
            self.displayImage(im_transfer)
            self.waitingLabel2.hide()

    def removeImg(self):
            portrait_path = os.path.join("portrait","*.jpg")
            list_portrait = glob.glob(resource_path(portrait_path))
            if not list_portrait:
                pass   
            else :
                latest_portrait = max(list_portrait,key=os.path.getctime)
                os.remove(latest_portrait)


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Window4", "MainWindow"))
 
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui=Ui_Window4()
    ui.setupUi(lang=1)
    ui.show()
    #ui.showFullScreen()
    Window4 = QtWidgets.QMainWindow()
    sys.exit(app.exec_())
