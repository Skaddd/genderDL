#Created by Mateo LEBRUN

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QImage,QPixmap 

import source
import glob
import os
import cv2
import time

from transfer_im import crop_center,load_image,styleT # functions that apply the style transfer model to a given image

from detection.face_alignment import date







class Ui_Window4(object):
    def setupUi(self, Window4):
        Window4.setObjectName("Window4")
        Window4.resize(1920, 1080)

        Window4.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(Window4)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("#centralwidget{background-image: url(:/images/assets/back1.jpg);}")
        #same as before since we are using once again camera and displaying content
        self.logic =1
        self.value =0
        self.stoploop=0
        #usefull, check below
        self.namestyle=""
        #Title
        self.labeltitle = QtWidgets.QLabel(self.centralwidget)
        self.labeltitle.setGeometry(QtCore.QRect(50, 30, 1121, 61))
        self.labeltitle.setObjectName("titlelabel")
        self.labeltitle.setStyleSheet("\n"
"font: 28pt \"Adobe Pi Std\";\n"
"color: rgb(255, 255, 255);")
        self.labeltitle.setTextFormat(QtCore.Qt.RichText)
        self.labeltitle.setScaledContents(True)
        self.labeltitle.setAlignment(QtCore.Qt.AlignLeft)
        self.labeltitle.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        #Box containing the camera output and images
        self.imgLabel = QtWidgets.QLabel(self.centralwidget)
        self.imgLabel.setGeometry(QtCore.QRect(1200, 100, 512, 512))
        self.imgLabel.setFrameShape(QtWidgets.QFrame.Box)
        self.imgLabel.setFrameShadow(QtWidgets.QFrame.Raised)
        self.imgLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.imgLabel.setLineWidth(6)
        self.imgLabel.setMidLineWidth(0)
        self.imgLabel.setText("")
        self.imgLabel.setStyleSheet("boder-radius : 10px;")
        self.imgLabel.setObjectName("imgLabel")


        #Frame to put buttons
        self.frameButtons=QtWidgets.QFrame(self.centralwidget)
        self.frameButtons.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.frameButtons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameButtons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameButtons.setObjectName("frameButtons")
        self.frameButtons.setGeometry(QtCore.QRect(1100,600,750,91))

        self.captureBut = QtWidgets.QPushButton(self.frameButtons)
        self.captureBut.setGeometry(QtCore.QRect(50, 30, 141, 41))
        self.captureBut.setMouseTracking(True)
        self.captureBut.setStyleSheet("QPushButton{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 14pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}")
        self.captureBut.setObjectName("captureBut")

        self.screenBut = QtWidgets.QPushButton(self.frameButtons)
        self.screenBut.setGeometry(QtCore.QRect(300, 30, 141, 41))
        self.screenBut.setMouseTracking(True)
        self.screenBut.setStyleSheet("QPushButton{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 14pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}")
        self.screenBut.setObjectName("screenBut")


        self.transferBut = QtWidgets.QPushButton(self.frameButtons)
        self.transferBut.setGeometry(QtCore.QRect(550, 30, 141, 41))
        self.transferBut.setMouseTracking(True)
        self.transferBut.setStyleSheet("QPushButton{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 14pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}")
        self.transferBut.setObjectName("transferBut")

        self.infoLabel = QtWidgets.QLabel(self.centralwidget)
        self.infoLabel.setGeometry(QtCore.QRect(30, 620, 1100, 300))
        self.infoLabel.setStyleSheet("font: italic 14pt \"Adobe Pi Std\";\n"
"\n"
"color: rgb(255, 255, 255);")
        
        self.infoLabel.setObjectName("infoLabel")
        self.infoLabel.setAttribute(QtCore.Qt.WA_TranslucentBackground)


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
        self.scrollArea.setStyleSheet("""  QScrollBar:horizontal{
     height: 20px;
     margin: 3px 15px 3px 15px;
     border-radius: 4px;
     background-color: yellow;    /* #2A2929; */
 }
 QScrollBar::handle:horizontal{
     background-color: gray;      /* #605F5F; */
     min-width: 5px;
     border-radius: 4px;
 }
 QScrollBar::add-line:horizontal{
     margin: 0px 3px 0px 3px;
     border-image: url(:/qss_icons/rc/right_arrow_disabled.png);
     width: 10px;
     height: 10px;
     subcontrol-position: right;
     subcontrol-origin: margin;
 }
 QScrollBar::sub-line:horizontal{
     margin: 0px 3px 0px 3px;
     border-image: url(:/qss_icons/rc/left_arrow_disabled.png);
     height: 10px;
     width: 10px;
     subcontrol-position: left;
     subcontrol-origin: margin;
 }
 QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal{
     background: none;
 }
 QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal{
     background: none;
 }""" )
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(-22, 0, 842, 268))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setAttribute(QtCore.Qt.WA_TranslucentBackground)
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
            print(name_but)
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
            self.buttons[(k)].setStyleSheet("QPushButton{\n"
                        "border-style: outset;""\n"
                        "border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 14pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}")
            self.buttons[(k)].setFlat(True)
            
            self.buttons[(k)].setCheckable(True)
            
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
        self.backBut.setStyleSheet("QPushButton{\n"
                        "border-style: outset;""\n"
                        " border-radius: 10px;"
                        "border-width: 2px;"
                        "border-color: gray;"
                        "font: 14pt \"Adobe Pi Std\";\n"
                        "color: rgb(255, 255, 255);}\n"
                        "QPushButton:pressed { border-style : inset; border-color:black}")
        self.backBut.setObjectName("backBut")

        Window4.setCentralWidget(self.centralwidget)

        self.retranslateUi(Window4)
        QtCore.QMetaObject.connectSlotsByName(Window4)
    

    ## The tricky part, since we generate buttons in a loop it's hard to access to a unique button, in order to create unique clicked.connect methods 
    #we can't use the lambda function directly because it processed in real time (so will always the current value when pressing the bbutton, so the last value in the loop)
    #so we create a method that itself create lambdas, so for each button we have a lambda function
    def make_callback(self,k):
        return lambda : self.storeButname(k)

    def storeButname(self,k):
        self.namestyle = self.buttons[(k)].text()

    ##

    def leavingWin(self,window):
        self.stoploop=1
        window.close()

    def launchCamera(self,TIMER):
        self.logic=1
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
                    self.displayImage(img)
                    cv2.waitKey() 
                    cur = time.time() 

                    if cur-prev >= 1: 
                        prev = cur 
                        TIMER = TIMER-1
                else :
                    date=time.strftime("%Y-%m-%d-%H-%M")
                    cv2.imwrite('portrait/im-'+date+'.jpg',img)
                    cv2.waitKey(125)
                    self.imgLabel.clear()
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
        path = os.path.join("portrait","*")
        list_images = glob.glob(path)
        latest_img = max(list_images,key=os.path.getctime)
        if self.namestyle=="":
            print("you did not selected an image")
        else :
            styleT(latest_img,'pictures/'+self.namestyle+'.jpg')
            im_transfer = cv2.imread('transfer.jpg')
            self.displayImage(im_transfer)





    def retranslateUi(self, Window4):
        _translate = QtCore.QCoreApplication.translate
        Window4.setWindowTitle(_translate("Window4", "MainWindow"))
        self.labeltitle.setText(_translate("Window4", "Fast Style transfer with Artificial Intelligence"))
        self.backBut.setText(_translate("Window4","back"))
        self.captureBut.setText(_translate("Window2", "Capture"))
        self.screenBut.setText(_translate("Window2","Take picture"))
        self.transferBut.setText(_translate("Window2","Apply Style"))
        self.infoLabel.setText(_translate("Window2", "Apply different style to your image!\n"
" \n"
"It's simple, First if you haven't  taken yet an image of yourself launch the camera with the button caputre and take a picture!"  "\n" "It will take a photo within 5 seconds.\n"
"Feel free to take another one if you don't like the last one !" "\n" "Now you have a beautfil image , Select the style you like from the different images presented!\n"
"Once you selected your style use the button  Apply Style to see the result!\n"
"The process might take some time, be Kind don't spam the other buttons "))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Window4 = QtWidgets.QMainWindow()
    ui = Ui_Window4()
    ui.setupUi(Window4)
    Window4.show()
    sys.exit(app.exec_())
