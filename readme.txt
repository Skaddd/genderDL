Explication de la structure du projet:
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

assets/ :

Contient les images utilisées par l'application
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

data/ : 

Contient les images et labels utilisées pour entrainer le réseau de neurones
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

detection/ : 

Contient plusieurs fichiers, les fichiers .dat et .bz sont modèles pré-entrainé
Appartenant à  la librairie opencv.

detection/images/ :

Contient les images des visages reconnus lorsqu'une image est prise sur l'application
Mais aussi le résultat des predictions affichée sur l'image de base

les dossier saved/ : Contiendront les images sauvegardée

face_alignement.py :

Fichier faisant appel aux model pré-entrainée pour detecter les visages

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

models/ :

Contient les models d'age et de sexe que j'ai entrainée

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

pictures/: 

Contient les images de style utilisée pour le fast transfer style

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

portrait/ :

Stocke les images prisent sur l'applcation

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------

Concernant les fichiers python :

test.py, predicit.py train.py permettent de tester et entrainer le réseau de neurones

il faudra changer le nom à chaque entrainement pour ne pas voir le model precedent écrasé

transfer_im.py


permet l'application du fast style transfer




L'ensemble des fichiers WindowX.py contiennent le GUI de l'app

display.py et keract_display.py snt utilisée pour l'affichage de "l'interieur" du réseau



-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------



Commandes pour transformer un .ui généralement crée à partir de Qt Designer, en .py.
Si le .ui utilise un ficher qrc, il faut aussi transformer ce fichier en fichier .py

pyuic5 -x input.ui -o output.py


pyrcc5 -o source.py source.qrc

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------


les librairies à installer:

tensorflow==2.1.0
numpy==1.9
scipy==1.4.1
sklearn=0.23.1
glob
dlib==19.20
PyQt5
python-opencv==4.3.0
time

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------


POUR CHANGER L'image de FOND


Normalement il faut juste ajouter la nouvelle image au dossier assets

Puis dans chaque fichier WindowX.py 

Chercher self.setStyleSheet et changer dans #centralwidget background-image : avec le nouveau nom de l'image choisi

Si probleme m'appeler.

-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
-----------------------------------------------------------------------------------
Pour recreer l'exuctable juste lancer 
make_exe.bat