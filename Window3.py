#Created by Mateo LEBRUN

"""
Important Information about about translation :
lang == 2 means that the text must be written in Deutsch
lang== 3 means that the text must be written in Portuguese
else means that the text must be written in Lux

"""



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QMovie,QPixmap
from PyQt5.QtCore import QSize

import cv2
import os
import glob
import source


from display import fin
from Window5 import Ui_Window5

class Ui_Window3(QMainWindow):

    def __init__(self):
        super(Ui_Window3,self).__init__()

    #method that opens window5 and setup everything
    def openWindow5(self):
        self.qtimer.stop()
        self.ui5=Ui_Window5()
        self.ui5.setupUi(self.lang)
        self.ui5.show()
        self.ui5.stayBut.clicked.connect(lambda : self.ui5.closeWindow())
        reset_timer = 150000
        self.ui5.stayBut.clicked.connect(lambda : self.qtimer.start(reset_timer))

        self.ui5.leaveBut.clicked.connect(lambda : self.ui5.closeWindow())
        self.ui5.leaveBut.clicked.connect(lambda : self.close())
        self.ui5.windowTitleChanged.connect(lambda :self.close())


    #This method is build like previous methods we saw
    #We just added gif that are readable thanks to QMovie Object
    def setupUi(self,lang):
        self.lang = lang
        self.setObjectName("Window3")
        #self.resize(1920, 1080)
        self.centralwidget = QtWidgets.QWidget(self)
        
        self.timer = 300000 # in milliseconds
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
            "#centralwidget{background-image: url(:/images/assets/back1.jpg); background-repeat = no-repeat; background-position = center};")
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
        self.framelvl.setGeometry(QtCore.QRect(15, 160, 200, 880))
        self.framelvl.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.framelvl.setObjectName("framelvl")
        


        self.frameExplain = QtWidgets.QFrame(self.centralwidget)
        self.frameExplain.setGeometry(QtCore.QRect(215, 80, 1550, 925))
        self.frameExplain.setObjectName("frameExplain")
        self.frameExplain.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.gridLayout = QtWidgets.QGridLayout(self.frameExplain)
        self.gridLayout.setObjectName("gridLayout")


        self.verticalLayout_text = QtWidgets.QVBoxLayout()
        self.verticalLayout_text.setObjectName("verticalLayout_text")

        self.labeltext = QtWidgets.QLabel(self.frameExplain)
        self.labeltext.setObjectName("labeltext")
        self.labeltext.setScaledContents(True)
        self.labeltext.setStyleSheet(
            "font: 14pt \"Adobe Pi Std\";"
            "color: rgb(255, 255, 255);")
        self.verticalLayout_text.addWidget(self.labeltext)
        self.gridLayout.addLayout(self.verticalLayout_text, 0, 0, 1, 2)

        self.verticalLayout_img = QtWidgets.QVBoxLayout()
        self.verticalLayout_img.setObjectName("verticalLayout_img")

        self.labelimage = QtWidgets.QLabel(self.frameExplain)
        self.labelimage.setObjectName("labelimage")

        self.verticalLayout_img.addWidget(self.labelimage)
        self.gridLayout.addLayout(self.verticalLayout_img, 2, 0, 1, 2)



        self.gif=QMovie('assets/explain.gif')
        self.gif.setScaledSize(QSize(625,375))

        self.gif2=QMovie('assets/network.gif')
        self.gif2.setScaledSize(QSize(645,364))

        self.gif3=QMovie('assets/advanced.gif')
        self.gif3.setScaledSize(QSize(621,349))


        self.gif4=QMovie('tmp/movie.gif')
        self.gif4.setScaledSize(QSize(320,240))

        self.verticalLayout_more = QtWidgets.QVBoxLayout()
        self.verticalLayout_more.setObjectName("verticalLayout_more")

        self.HboxBot = QtWidgets.QHBoxLayout()
        self.HboxBot.setObjectName("Hboxbot")

        self.labelmore = QtWidgets.QLabel(self.frameExplain)
        self.labelmore.setObjectName("labelmore")
        self.labelmore.setStyleSheet(
            "font: italic 14pt \"Adobe Pi Std\";"
            "color: rgb(255, 255, 255);")
        self.labelmore.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
        self.labelmore.setScaledContents(True)

        self.labelLogo = QtWidgets.QLabel(self.frameExplain)
        self.labelLogo.setObjectName("labelLogo")
        self.labelLogo.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
        self.pixmap = QPixmap('assets/3b1b.png').scaled(64,64)

        self.HboxBot.addWidget(self.labelmore)
        self.HboxBot.addWidget(self.labelLogo)
        self.verticalLayout_more.addLayout(self.HboxBot)
        self.gridLayout.addLayout(self.verticalLayout_more,4,0,1,1)

        self.easyBut = QtWidgets.QPushButton(self.framelvl)
        self.easyBut.setGeometry(QtCore.QRect(0, 50, 141, 41))
        self.easyBut.setObjectName("easyBut")

        self.normalBut = QtWidgets.QPushButton(self.framelvl)
        self.normalBut.setGeometry(QtCore.QRect(0, 300, 141, 41))
        self.normalBut.setObjectName("normalBut")

        self.advancedBut = QtWidgets.QPushButton(self.framelvl)
        self.advancedBut.setGeometry(QtCore.QRect(0, 550, 141, 41))
        self.advancedBut.setObjectName("advancedBut")

        self.expertBut=QtWidgets.QPushButton(self.framelvl)
        self.expertBut.setGeometry(QtCore.QRect(0,800,141,41))
        self.expertBut.setObjectName("expertBut")
        
        self.Insideframe = QtWidgets.QFrame(self.centralwidget)
        self.Insideframe.setGeometry(QtCore.QRect(1350,600,200,200))
        self.Insideframe.setObjectName("Insideframe")
        self.Insideframe.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.InsideBut=QtWidgets.QPushButton(self.Insideframe)
        self.InsideBut.setGeometry(QtCore.QRect(0,0,141,41))
        self.InsideBut.setObjectName("InsideBut")

        self.InsideBut2 = QtWidgets.QPushButton(self.Insideframe)
        self.InsideBut2.setGeometry(QtCore.QRect(0,50,141,41))
        self.InsideBut2.setObjectName("InsideBut2")
        self.InsideBut2.hide()


        self.Insideframe.hide()

        self.popupLabel= QtWidgets.QLabel(self.Insideframe)
        self.popupLabel.setObjectName("popupLabel")
        self.popupLabel.setGeometry(QtCore.QRect(0,90,141,41))
        self.popupLabel.setStyleSheet(
            "font:  20pt \"Adobe Pi Std\";"
            "color: rgb(255, 255, 255);"
        )



        if lang ==0:
            self.titlelabel.setText("Comprendre le fonctionnement de cette Inteligence Arificielle ")
            self.easyBut.setText("Facile")
            self.normalBut.setText("Normal")
            self.advancedBut.setText( "Avancé")
            self.expertBut.setText("Expert")
            self.backBut2.setText("retour")
            self.labeltext.setText("")
        elif lang ==1:
            self.titlelabel.setText("Through different level of undestanding, learn how this artifical intelligence works")
            self.easyBut.setText("Easy")
            self.normalBut.setText("Normal")
            self.advancedBut.setText("Advanced")
            self.expertBut.setText("Expert")
            self.backBut2.setText("back")
            self.labeltext.setText("")

        elif lang ==2:
            self.titlelabel.setText("")
            self.easyBut.setText("")
            self.normalBut.setText("")
            self.advancedBut.setText("")
            self.expertBut.setText("")
            self.backBut2.setText("")
            self.labeltext.setText("")
        elif lang ==3:
            self.titlelabel.setText("")
            self.easyBut.setText("")
            self.normalBut.setText("")
            self.advancedBut.setText("")
            self.expertBut.setText("")
            self.backBut2.setText("")
            self.labeltext.setText("")
        else :
            self.titlelabel.setText("")
            self.easyBut.setText("")
            self.normalBut.setText("")
            self.advancedBut.setText("")
            self.expertBut.setText("")
            self.backBut2.setText("")
            self.labeltext.setText("")


        self.qtimer = QtCore.QTimer(self)
        self.qtimer.start(self.timer)
        self.qtimer.timeout.connect(self.openWindow5)


        self.easyBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.normalBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.advancedBut.clicked.connect(lambda: self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
        self.expertBut.clicked.connect(lambda : self.mousePressEvent(QtGui.QMouseEvent.MouseButtonPress))
       

        self.InsideBut.clicked.connect(lambda : self.disableBut())

        self.setCentralWidget(self.centralwidget)
        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def displayGif(self):
        self.labelimage.setMovie(self.gif4)
        self.gif4.start()
        self.InsideBut2.hide()
        self.enableBut()

    def createGif(self):
        path_img ='./detection/images/aligned/tmp/*'
        list_files = glob.glob(path_img)
        latest_file =max(list_files,key=os.path.getctime)
        if not latest_file:
            print("Pas d'images")
            return
        else :
            fin(latest_file)
            self.InsideBut2.show()
            self.InsideBut.setEnabled(False)



    def disableBut(self):
        if self.lang ==0:
            self.popupLabel.setText("PATIENTEZ...")
        elif self.lang ==1:
            self.popupLabel.setText("WAIT...")
        elif self.lang ==2:
            self.popupLabel.setText("")
        elif self.lang ==3:
            self.popupLabel.setText("")
        else :
            self.popupLabel.setText("")
        self.popupLabel.update
        self.backBut2.setEnabled(False)
        cv2.waitKey(125)
        self.createGif()
        self.popupLabel.setText("")
        

    def enableBut(self):
        self.backBut2.setEnabled(True)
        self.InsideBut.setEnabled(True)




    def addtimer(self):
        if self.qtimer.remainingTime() <= self.timer:
            new_timer = 450000 #milliseconds
            self.qtimer.setInterval(new_timer)
            self.qtimer.start()
   

    def mousePressEvent(self,event):
        if event == QtGui.QMouseEvent.MouseButtonPress:
            self.addtimer()
        else:
            self.addtimer()
    

    #This method speaks for itself, we just display the easy explanations
    def displayEasy(self,lang):
        self.labelimage.clear()
        self.Insideframe.hide()
        self.labelimage.setMovie(self.gif)
        self.labelLogo.setPixmap(self.pixmap)
        self.gif.start()
        if lang ==0:
            self.labeltext.setText(
                "Qu-est ce que l'intelligence arificielle?\n \n"
                "C'est une machine qui comme les humains, peut apprendre toute seule\n"
                "En dessous c'est un exemple, la machine arrive à reconnaître des chats et des chiens\n"
                "Chaque cercle représente un neurone, et ils sontt tous connectés entre eux, chaque ligne verticales de neurones sont appelées couches\n"
                "Et toutes les couches forment un réseau de neurones\n"
                "En donnant une image au reseau, les connections entre les neurones vont plus ou moins s'activer si l'image est un cat ou un chien\n"
                "A la fin, il y a seulement 2 neurones, donc si l'un est plus activé que l'autre, la machine sait que l'image est un chat et inversement avec le chien\n \n"
                "Le réseau que nous avons utilisé pour reconnaitre votre age et votre gender est un peu plus complexe\n"
                "Le réseau en dessous :  \t\t\t\t  Notre réseau : \n"
                "  Nombre de paramètres d'entrée : 3  \t\t\t  Nombre de paramètres d'entrée : 227*227*3 = 154 587 \n"
                "  Nombre de paramètres modifiables : 3*4*2 = 24  \t\t  Nombre de paramètres modifiables : 23 792 713\n"
                "  Nombre de couche intermédiaire : 1  \t\t\t  Nombre de couches intermédiaire : 174\n"
                "  Nombre de paramètres de sortie : 2  \t\t\t  Nombre de paramètre de sortie : 11\n")
            self.labelmore.setText("Si vous voulez en apprendre plus sur l'intelligence artificielle et le deep learning, allez sur la chaine youtube de 3Blue1Brown ! ")
        elif lang==1 :
            self.labeltext.setText(
                "What does Aritifical Intelligence mean?\n \n" 
                "It is a programm that, like humans,is able to learn simple things\n"
                "Below, the AI is able to distinguish cats and dogs.\n \n"
                "But How it works?\n \n"
                "Each circle represents a neuron, as you can see they are all connected. Vertical lines of neurons are named layer.\n"
                "The whole thing is called a  neural netwrok.\n"
                "When you are giving an image to the network, the connections between neurons will be more or less activated, if it is a dog or a cat.\n"
                "At end there are only 2 neurons, so if the first one is more activated than the second one, the network knows it's a cat and otherwise it's a dog \n \n"
                "The network we used to detect your age and your gender is more complex... :\n"
                "The network below :  \t\t\t\t  Our network :\n"
                "Input parameters :  3  \t\t\t\t\t  Input parameters : 227*227*3 = 154 587\n"
                "Parameters : 3*4*2 = 24  \t\t\t\t\t  Parameters : 23 792 713\n"
                "number of hidden layer : 1 \t\t\t\t  Number of hidden layer : 174\n"
                "Output parameters : 2  \t\t\t\t\t  Outputs parameters : 11\n")
            self.labelmore.setText("If you want to learn more about artificial intelligence and deep learning  go to 3Blue1Brown youtube channel ! ")
        elif lang ==2:
            self.labeltext.setText("")
            self.labelmore.setText("")
        elif lang ==3:
            self.labeltext.setText("")
            self.labelmore.setText("")  
        else :
            self.labeltext.setText("")
            self.labelmore.setText("")

    #This method speaks for itself, we just display the normal explanations
    def displayNormal(self,lang):
        self.Insideframe.hide()
        self.labelimage.clear()
        self.labelimage.setMovie(self.gif2)
        self.labelLogo.setPixmap(self.pixmap)
        self.gif2.start()
        if lang ==0:
            self.labeltext.setText(
                "Qu'est ce l'intelligence artificielle et comment ça marche?\n \n"
                "Enfaite ici pour être plus précis, c'est plûtot le deep learning qui nous intéresse\n"
                "le Deep learning décrit des algoritmhes qui ont une structure se rapprochant du cerveau humain, un réseau de neurones\n"
                "et tente de reporduire certaines de ces fonctions\n \n"
                "Comment c'est possible?\n \n"
                "Grâce à des enormes bases de données, les reseaux de neurones sont entrainés à reconnaitre des formes ou objets(par exemple)\n"
                "L'entrainement du reseau est une des phases des plus importante, pendant celle-ci on va lui donner des images de ce qu'il doit reconnaitre\n"
                "Et lui dire ce qu'il aurait dû obtenir. Avec ça il va pouvoir se corriger tout seul, et progressivement s'améliorer\n"
                "Si on regarde l'exemple en-dessous, chaque pixel de l'image est une entrée."
                "La première couche de neurones va généralement reconnaitre les formes caractéristiques simples: les countours.\n"
                "Les couches suivantes vont de plus en plus reconnaitre des patterns complexes. La dernière couche à autant de neurones qu'il y a de classes(chat,chien)\n"
                "Cette dernière couche represente alors les résultats du réseau \n \n"
                "Comparons le resau que nous avons utilisé reconnaitre votre age et votre gender et le réseau en dessous!\n"
                "Le réseau en dessous : \t\t\t\t\t  Notre réseau : \n"
                "  Nombre de paramètres d'entrée : 20*20*3 = 1200 \t\t  Nombre de paramètres d'entrée : 227*227*3 = 154 587 \n"
                "  Nombre de paramètres modifiables : 108 352 \t\t\t  Nombre de paramètres modifiables : 23 792 713\n" # 108 352 = 3x3x3*64 + 3*3*64*128+2*2*128*64+64*2 obtenu de façon un peu arbitraire
                "  Nombre de couche intermédiaire : 3  \t\t\t\t  Nombre de couches intermédiaire : 174\n"
                "  Nombre de paramètres de sortie : 2  \t\t\t\t  Nombre de paramètre de sortie : 11\n")
            self.labelmore.setText("Si vous voulez en apprendre plus sur l'intelligence artificielle et le deep learning, allez sur la chaine youtube de 3Blue1Brown ! ")
        elif lang==1 :
            self.labeltext.setText(
                "What does Articial Intelligence describe?\n \n"
                "Well, the question should be what is Deep Learning?\n"
                "It's a technique that construsts artificial neural networks and aim to mimic the structure and function of the human brain\n\n"
                "How it works?\n"
                "Thanks to massive amout of data, neural networks are trained to find and recognize patterns in order to make decisions\n"
                "During the training, we help them to know if their predictions were correct or not.\n"
                "Based on the results the neural network will increasingly become more accurate.\n \n"
                "Let's look at the example below\n"
                "The first layer will abstracts the pixels that are input data, and detect the edges of features in the image. The next one will detect something else and so on.\n"
                "At the end, the last layer, named output layer will return a number of value generally equals to the number of different classes(dog,cat)\n"
                "Representing the prediction of the neural network.\n\n"
                "Let's compare this network with the one we used to detect your gender and your age :\n"
                "The network below :  \t\t\t\t  Our network :\n"
                "Input parameters :  20*20*3 = 1200  \t\t\t  Input parameters : 227*227*3 = 154 587\n"
                "Parameters : 108 352  \t\t\t\t\t  Parameters : 23 792 713\n"
                "number of hidden layer : 3  \t\t\t\t  Number of hidden layer : 174\n"
                "Output parameters : 2  \t\t\t\t\t  Output parameters : 11\n")
            self.labelmore.setText("If you want to learn more about artificial intellience and deep learning  go to 3Blue1Brown youtube channel ! ")
        elif lang ==2:
            self.labeltext.setText("")
            self.labelmore.setText("")
        elif lang ==3:
            self.labeltext.setText("")
            self.labelmore.setText("")
        else :
            self.labeltext.setText("")
            self.labelmore.setText("")


    #This method speaks for itself, we just display the advanced explanations
    def displayAdvanced(self,lang):
        self.Insideframe.hide()
        self.labelimage.clear()
        self.labelimage.setMovie(self.gif3)
        self.gif3.start()
        self.labelLogo.setPixmap(self.pixmap)
        if lang ==0:
            self.labeltext.setText(
                "Qu'est ce l'intelligence artificielle et comment ça marche?\n \n"
                "Le domaine de l'intelligence artificielle recouvre l'ensemble des programmes capablent d'effectuer des tâches qui normalement demandent une intelligence humaine\n"
                "Le deep learning est une ramification du machine learning qui à pour but de résoudre des problèmes complexes avec ou sans données structurées\n"
                "Les algorithmes de deep learning se composent généralement d'un modèle de réseau de neurones, modèle que l'on va entraîner et qui va s'améliorer pendant cette phase.\n"
                "Comment ça marche?\n \n"
                "Prenons l'exemple en-dessous, on souhaite reconnaitre des chiffres écrit à la main\n"
                "L'image étant l'entrée, plus précisement les pixels de l'image. Donc en entrée nous avons la matrix de pixel."
                "Chaque neurone de la première couche contient la valeur d'un pixel, et chaque neurone de cette couche connecté à tous les neurones de la couche suivantes,\n"
                "ces connections ont toutes des valeurs associées, des poids.\n"
                "Pour obtenir les valeurs des neurones des autres couches on appliques des functions d'activations qui dependent de la couche précédente et des poids.\n"
                "En passant une image à travers le réseau on effectue un forward pass"
                "On note que la dernière couche, doit contenir un nombre de neurones égal aux nombres de classes, ici il y a 10 classes.\n"
                "Une fois le forward pass effectué on va regarder la dernière couche et la comparer à ce que le réseau aurait dû trouver (un 7 par exemple)\n"
                "Si le réseau de neurones c'est plus ou moins trompés il va corriger légèrement tous les poids, c'est la backpropagation\n"
                "L'enchainement forward pass backpropagation est répété un grand nombre de fois pour atteindre des résultats intéressant\n"
                "Finalement, comme dans l'exemple, lorsque l'entrainement est terminée, chaque chiffre va plus ou moins activée certaines parties du réseau, et il sera capable de le reconnaitre\n")
            self.labelmore.setText("Si vous voulez en apprendre plus sur l'intelligence artificielle et le deep learning, allez sur la chaine youtube de 3Blue1Brown ! ")
        elif lang==1 :
            self.labeltext.setText("What is deep learning?\n \n"
                "The field of artificial intelligence is mainly when machines can perform tasks that typically require human intelligence.\n"
                "Deep learning as a subset of machine learning focuses on solving complex problems even when using  diverse and unstructured data set\n"
                "The deep learning algorithm would perform a task repeatedly, each time tweaking it a little to improve the outcome\n \n"
                "How it works?\n \n"
                "Let's take the example below, we want to recognize hand written numbers.\n" 
                "The image is the input, more precisely, each pixel of the image. So we have a matrix containing the pixel values as input\n" 
                "Then, all input neurons are connected to neurons in the second layers, these connections have weights.\n"
                "The input neurons contains the value of each pixel. To get the value of the second layer, we apply an acitvation function to the inputs and weights and so on.\n"
                "It is called the forward pass\n"
                "As you can see, we are increasingly reducing the number of neurons, indeed, at the end of the network we want the exact number of classes it must recognize, there 10.\n"
                "On this example, the training part is already finished, so the network is directly able to detect a 7.\n"
                "Otherwise, the network would have compared the output layer and the true value then tweak all its weights to reduce the error between true and prediciton values\n"
                "It's called the backpropagation\n"
                "The training part will essentialy constist of repeating forward pass followed by backpropagtion for a large amount of images\n"
                "Once the training part is done, each hand written numbers will trigger specific connections and neurons through the network, to finally predict the correct answer.\n")
            self.labelmore.setText("If you want to learn more about artificial intellience and deep learning  go to 3Blue1Brown youtube channel ! ")

        elif lang ==2:
            self.labeltext.setText("")
            self.labelmore.setText("")
        elif lang ==3 :
            self.labeltext.setText("")
            self.labelmore.setText("")    
        else :
            self.labeltext.setText("")
            self.labelmore.setText("")
    #This method speaks for itself, we just display the expert explanations    
    def displayExpert(self,lang):
        self.Insideframe.show()
        self.labelLogo.setPixmap(self.pixmap)
        self.labelimage.clear()
        if lang ==0:
            self.labeltext.setText(
                "Avant de commencer, prenez connaissance des explications du niveau avancé car nous nous reposerons dessus ici\n \n"
                "En effet nous allons maintenant revenir à notre cas, la classification d'image et notamment suivant leur genre et leur age\n"
                "La classification de visage étant beacoup plus complexe que celle de chiffres, le réseau de neurones doit contenir beacoup plus de paramètres pour être peformant.\n"
                "Entrainer totalement tous ces paramètres demanderaient d'importantes ressources sans forcément de resultats..\n"
                "Généralement, pour palier à ce problème on utilise le transfert learning (surtout lorsque l'objectif est la classification d'image!).\n \n"
                "C'est quoi le transfer learning?\n \n"
                "Pour faire simple c'est lorsqu'on reutilise un modèle déjà entrainée sur une importante base de données comme base pour notre propre modèle\n"
                "Même si le réseau n'as pas été entrainé à reconnaitre ce qu'on désire classifier tout n'est pas à jeter! Un transfert de connaissance est possible!\n"
                "En utilisant un modèle pré-entrainé comme base, lors de l'entrainement de notre modèle, celui-ci sera bien plus rapide et efficace à reconnaitre des patterns simple\n"
                "Qu'il a déjà rencontré lors de son premier entrainement!\n"
                "A cette base, on rajoute par-dessus des couches qui elles seront choisies specifiquement pour notre modèle (la taille de la dernière couche dépend du nombre de classes)\n \n"
                "Maintenant que nous avons notre modèle, nous avons besoin d'image pour l'entrainer, beaucoup d'image, et des images différentes!\n"
                "Une partie très importante du deep learning est le data processing, c'est à dire le pré-traitement des images.\n"
                "C'est seulement si cette partie est bien réalisée que le réseau apprendra. Une fois cette partie terminée, on peut enfin lancer des entrainements.\n"
                "Mais les premiers résultats ne sont généralement pas satisfaisant, une autre phase commence alors : le fine-tunning \n"
                "Phase durant laquelle on va faire evoluer des paramètres du réseau. Finalement, suite à un certain nombre d'essais, on atteint enfin un modèle performant\n\n"
                "En appuyant sur le bouton Creer,  vous verrez apparitre un gif contenant une feature map(=sortie) pour chaque couche des 141 premières couches du réseau\n"
                "Les images sont de basses qualités car le réseau travaille avec des images de tailles fixes, ces sorties vous donnerons une idée de ce que reconnait le réseau\n"
                "Quand le gif sera terminée un autre bouton apparaitra pour afficher le gif !\n"
                )
            self.labelmore.setText("Si vous voulez en apprendre plus sur l'intelligence artificielle et le deep learning, allez sur la chaine youtube de 3Blue1Brown ! ")
            self.InsideBut.setText("Creer")
            self.InsideBut2.setText("Afficher")
            
        elif lang ==1:
            self.labeltext.setText(
                "Before starting, you should take notice of the advanced explanation, we will based ourself on it\n \n"
                "Indeed, we will now comeback to our case, the image classfication and more precisely the gender and age recognition\n"
                "This classification is alot more resource demanding than the hand writting one we saw previously. We need more parameters to achieve descent result.\n"
                "However, training all these parameters might request time and resource without guaranteed success. \n"
                "Thus,  to overcome this issue we usually use transfer learning. \n \n"
                "Whats tranfer learning? \n \n"
                "Well it allows the improvement of learning in a new task through the transfer of knowledge from a related task that has already been learned. \n"
                "To simplify it, some layers of the pre-trained model are already efficient for detecting simple patterns, so when training our model, we want to keep this knowledge.\n"
                "Consequently we tend to use a pre-trained model as a core of our model, then we add on top of it, more or less layer depending on our classification job \n"
                "Now that we have our model, we need images, a lot of images! \n "
                "Therefore finding these images and processing them to be able to feed them to the model is a huge part of the process \n"
                "Only when it's done, the training will be possible. Sadly first training sessions are usually not good. To improve our model we start fine tunning parameters that matters. \n"
                "Finally after many attempts we might end up with an accurate model \n \n"
                "Press the button that appeared, you will see a gif containing a feature map(=output) for each layer of the 100 firsts layers \n"
                "Images are not in high quality because the network  reduces increasingly the size of inputs, however this will an idea of what the network recognize\n"
                "When the gif will be finished a new bouton will appear, press it to see the result\n"
            )
            self.labelmore.setText("If you want to learn more about artificial intellience and deep learning  go to 3Blue1Brown youtube channel ! ")
            self.InsideBut.setText("Create")
            self.InsideBut2.setText("Display")
        elif lang ==2:
            self.labeltext.setText("")
            self.labelmore.setText("")
            self.InsideBut.setText("")
            self.InsideBut2.setText("")
        elif lang ==3:
            self.labeltext.setText("")
            self.labelmore.setText("")
            self.InsideBut.setText("")
            self.InsideBut2.setText("")
        else :
            self.labeltext.setText("")
            self.labelmore.setText("")
            self.InsideBut.setText("")
            self.InsideBut2.setText("")


    def retranslateUi(self, Window3):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Window3", "MainWindow"))





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = Ui_Window3()
    ui.setupUi(1)
    ui.show()
    sys.exit(app.exec_())
