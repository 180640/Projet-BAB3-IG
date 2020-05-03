# NAO joue au Tic Tac Toe et au Mastermind

L'ensemble des codes de notre projet sont disponibles sur ce GitHub. 
L'application principale - celle permettant de faire jouer NAO aux TTT et au MM - se trouve dans le fichier menu.zip.

Color.py est un code Python nous ayant permis de définir les plages de segmentation des couleurs. Les 2 autres codes sont des versions
des jeux du TTT et du MM pouvant se jouer uniquement sur ordinateur (pas sur NAO) via la console de Spyder par exemple.

-------------------------------------------------------------------------------------------------------------------------------------

Manuel d'installation des logiciels

-------------------------------------------------------------------------------------------------------------------------------------

1) Télécharger Chorégraphe

(a) 	Ouvrez le lien suivant : https://community.ald.softbankrobotics.com/en/resources/software/language/en-gb/field_software_type/choregraphe/robot/nao-2 

(b) 	Entrer les informations de connexion afin d’avoir accès aux différents logiciels relatifs à NAO. (Il est nécessaire d'avoir une licence avec une clé de produit. 
      Dans notre cas, notre co-promoteur de projet nous a transmis ses informations afin que nous puissions installer ce logiciel sur nos machines)

(c) 	Sélectionner "Choregraphe Setup" sous l’onglet Windows

2) 	Télécharger Python 2.7.

(a) 	Cliquez sur le lien suivant: https://www.python.org/downloads/release/python-2717/ Ce lien permet d’accéder directement aux fichiers d’installation pour python 2.7.17.

(b) 	Sélectionner "Windows x86 MSI installer". Attention, le lien "Windows x86-64 MSI installer" n’est pas valide pour l’utilisation que nous souhaitons en faire

(c) 	Installer le fichier python sur votre ordinateur par exemple sur "C:\Python27"

3) 	Télécharger la librairie Naoqi 

(a) 	Cliquez sur le lien suivant https://community.ald.softbankrobotics.com/en/resources/software/former-nao-versions-python-naoqi-sdk 

(b) 	Sélectionner "Python 2.7 SDK 2.1.4 Win 32 Setup" sous l’onglet Windows

(c) 	Lorsque le fichier est téléchargé, exécuter le programme. Une fenêtre avec un fond bleu apparait.

(d) 	Suivez les étapes et faites bien attention si vous possédez plusieurs versions de Python sur votre machine de sélectionner Python 2.7 lorsque l’option vous est proposée

(e) 	Finissez l’installation 

4) 	Installation de Numpy 

(a) 	Cliquez sur le lien suivant https://sourceforge.net/projects/numpy/files/NumPy/1.7.1/numpy-1.7.1-win32-superpack-python2.7.exe/download (le téléchargement se lance automatiquement) 

(b)  	Le fichier portant le nom "numpy-1.7.1-win32-superpack-python2.7.exe" est téléchargé. 

(c) 	Lorsque le fichier est téléchargé exécuter le programme, une fenêtre avec un fond bleu apparait

(d)   Suivez les étapes et faites bien attention si vous possédez plusieurs versions de Python sur votre machine de sélectionner Python 2.7 lorsque l’option vous est proposée

(e)   Finissez l’installation

(f)   Ouvrez Python IDLE (relatif à python2.7) et tapez la commande suivante "import numpy"

(g)  	Vérifiez que cette commande fonctionne 

5)  Installation OpenCV 

(a) 	Ouvrez le lien suivant: https://sourceforge.net/projects/opencvlibrary/files/opencv-win/2.3.1/ (La version d’OpenCV choisie n’est pas la dernière version mais date de 2012 car il faut
      que la version d’OpenCV sur votre machine soit la même que la version installée sur NAO) 

(b) 	Cliquez sur "OpenCV-2.3.1-win-superpack.exe" pour débuter le téléchargement 

(c) 	Une fois le téléchargement terminé suivez les instructions d’installation et choississez un endroit où installer OpenCV sur votre machine par exemple sur "C:\OpenCV"

(d) 	Lorsque l’installation est terminée copiez le fichier "cv2.pyd"  qui se trouve dans "C:\OpenCV\opencv\build\python\2.7" et collez-le dans "C:\Python27\Lib\site-packages"

(e) 	Ouvrez Python IDLE (relatif à python2.7) et tapez la commande suivante "import cv2" puis "print cv2.__version__" si aucun message d’erreur ne vous est retourné, l’installation d’OpenCV est terminée et vous pouvez commencer à utiliser NAO. 

--------------------------------------------------------------------------------------------------------------------------------------

Manuel d'utilisation

--------------------------------------------------------------------------------------------------------------------------------------


Se connecter à NAO
------------------

Pour se connecter à NAO il faut effectuer les étapes suivantes : 

1) Allumer NAO en appuyant sur le bouton qui se trouve sur son torse.

2) Connecter NAO au réseau. Il y a plusieurs manières de connecter NAO au réseau. 
     
(a) Pour se connecter par câble, il suffit de relier votre ordinateur et NAO avec un câble Ethernet (la prise se trouve à l'arrière du crâne du robot). L'ordinateur doit lui être connecté à internet via le réseau WiFi. Lorsque les branchements sont effectués, il suffit d'appuyer sur le bouton situé sur son torse. Il va alors se présenter et vous indiquer l'adresse IP à laquelle il s'est connecté. Vous devez recopier cette adresse IP dans un navigateur. Il vous est alors demandé d'entrer un nom d'utilisateur et un mot de passe qui sont fournis avec le robot. Vous avez dès lors accès à différentes informations de NAO via la navigateur. Ce mode de connexion est nécessaire lors de la première connexion afin que le réseau puisse être reconnu par NAO. Pour permettre à NAO de reconnaitre un réseau WiFi il faut vous rendre sur la page précédemment ouverte dans le navigateur. Rendez-vous alors sur l'onglet correspondant au réseau et cliquez sur le réseau sans fil que vous souhaitez faire reconnaitre à NAO. (Vous pouvez également brancher votre ordinateur et NAO via le cable au même modem) 
     
(b) Pour se connecter sans fil, votre ordinateur doit être connecté au même réseau qui est reconnu par NAO (expliqué dans le point précédent). Pour vous assurer de la bonne connnexion de NAO, appuyez sur le bouton situé sur son torse et s'il est connecté il vous dictera son adresse IP. Sinon, il vous informera qu'il n'a pas pu se connecter au réseau. 
    
3) Placer NAO en mode inactif. Pour ce faire, utilisez le logiciel Choregraphe connecté à NAO et appuyez sur le bouton représentant un coeur en haut à droite de l'écran. 

Lancer le programme 
------------------

Une fois NAO prêt, sur le dépôt GitHub de notre projet, cliquez sur le bouton vert "clone or download" situé en haut à droite de l'écran puis cliquez sur l'option "Download ZIP". Une fois le téléchargement terminé, placez l'ensemble du projet à l'emplacement de votre choix sur votre machine et dézippez le dossier. 

Vous devez à présent ouvrir les 3 fichiers suivants : "main_xo" du dossier "menu", "main_xo" du dossier "nao-xo-master" et "main_xo" du dossier "nao-mind-master". Pour chacun de ces fichiers, à la ligne ip= "/*ADRESSE IP DU ROBOT*/", veuillez placer l'adresse IP de votre robot à l'intérieur des guillemets, en lieu et place du présent commentaire. 

Il vous faut maintenant connaitre le chemin d'accès à votre dossier. Pour ce faire, vous pouvez cliquer droit sur le dossier "menu" et sélectionner l'onglet "Propriétés". Veuillez copier le chemin de votre dossier. 
Ouvrez une invite de commandes et entrez la commande suivante:

                                                  cd chemin_de_votre_dossier
                                                        
Par exemple: cd C:\Users\Louis\Documents\ProjetIG\menu

Assurez-vous que la profondeur du chemin aille bien jusqu'au dossier intitulé "menu". Veuillez ensuite taper la commande suivante:

                                                   main_xo.py -i adresse_IP_NAO
                                                      
Par exemple, si l'adresse IP est 192.254.29.237: main_xo.py -i 192.254.29.237

Le menu de jeu se lance alors, il ne vous reste plus qu'à jouer!

Jouer avec NAO
-------------

Une fois le menu lancé, NAO vous demandera à quel jeu vous voulez jouer. En fonction du jeu, vous devrez toucher soit le capteur situé sur le dos de sa main droite soit le capteur situé sur le dos de sa main gauche. Pour fermer le menu, appuyer du plat de la main sur la tête du robot.


----------  Tic Tac Toe ------------

Préparez les pions de couleurs jaunes et rouges ainsi que le plateau 3x3 à placer devant NAO dans son champ de vision. Choississez votre couleur de pions sachant que les pions rouges jouent toujours en premier. Votre but est d'aligner 3 pions de votre couleur. Les alignements gagnants doivent prendre place sur un plateau de 3x3 et correspondent donc à des lignes, des colonnes ou des diagonales. Le premier joueur à aligner 3 de ses pions remporte la partie.
Si vous avez choisi les pions rouges, vous pouvez commencer à jouer. Placer un pion sur le plateau et lorsqu'un cadre vert se dessine autour du plateau sur l'outil "Image" lancé automatiquement à l'écran de votre machine, appuyez sur la tête de NAO pour lancer la partie. NAO prend en compte votre premier coup et vous demandera alors de placer son pion à sa place en vous donnant le numéro de la case correspondant à la disposition de plateau représentée au schéma suivant:

                                                       1   2   3
                                                       4   5   6
                                                       7   8   9
                                                            
  Le schéma suivant correspond à celui que voit NAO. Si vous jouez en face de lui le schéma est donc, pour vous, le suivant: 
  
                                                       9  8  7   
                                                       6  5  4
                                                       3  2  1


Une fois que vous avez placé le pion de NAO, vous pouvez directement enchainer avec votre coup suivant. Pour vous aider, NAO reproduit l'acquisition du plateau de jeu sur un plateau virtuel ouvert automatiquement sur votre machine. Vous pouvez alors constater les pions reconnus ou non. Si l'un des pions n'est pas reconnu, veuillez bouger légèrement le plateau jusqu'à ce qu'un cadre vert se dessine autour de celui-ci sur l'outil "Image" ou reprendre le pion et le replacer. Vous pouvez également vérifier l'état du jeu dans l'invite de commande dans laquelle vous avez lancé l'exécution du programme. 
Si vous avez choisi les pions jaunes, c'est à NAO de commencer. Plateau vide, appuyez sur la tête du robot lorsqu'un cadre vert se dessine sur le même outil que précédemment. Le déroulement de la partie est identique à celui décrit plus haut.Si vous jouez avec les pions jaunes et que vous commencez à jouer, NAO mettra fin à la partie car c'était à son tour de jouer.


------------  Mastermind  -------------

Pour ce jeu, votre but sera de découvrir la combinaison de couleur créée par NAO. La combinaison de couleurs comporte trois couleurs distinctes. Il n'est pas autorisé qu'une combinaison comporte plusieurs fois la même couleur. Vous aurez 10 essais pour trouver la combinaison correcte en vous aidant des corrections données par NAO. 
Veuillez préparer les 3 plateaux de jeu. Le seul plateau de jeu avec lequel NAO joue est le plateau 3x3, veuillez le placer devant lui dans son champ de vision. Les 2 autres plateaux de 3x10 sont pour vous. Préparez également les pions pouvant servir aux combinaisons à savoir les pions de couleur jaune, bleue, mauve, rose et orange. Seules ces couleurs doivent servir à la combinaison. Vous disposez également de pions rouges et blancs qui vous serviront uniquement pour la correction. 
Lorsque le jeu du Mastermind se lance, vous devez placer votre première combinaison sur la ligne médiane horizontale du plateau de jeu 3x3 comme indiqué à la figure suivante (les pions sont représentés par "O"):

                                                      [ ]  [ ]  [ ]  
                                                           
                                                      [O]  [O]  [O] 
                                                           
                                                      [ ]  [ ]  [ ]
                                                           
 (Ce plateau est face à NAO)

Une fois votre combinaison placée, appuyez sur la tête de NAO du plat de la main une première fois pour lancer la partie et lorsque la combinaison est correctement acquise (visualisation sur le plateau virtuel ou dans la console), appuyez à nouveau sur sa tête pour demander la correction. 
NAO vous indique le nombre de couleurs correctement placées et le nombre de couleurs qui sont présentes dans la combinaison mais à la mauvaise position. Vous pouvez alors commencer à vous servir des deux autres plateaux 3x10. Déplacer votre combinaison sur l'un des deux plateaux. Celui-ci vous permettra de vous souvenir de vos combinaisons en y déplaçant au fur et à mesure les combinaisons proposées à NAO. Sur l'autre plateau, servez-vous des pions blancs et rouges pour reproduire la correction donnée par NAO. Par exemple, si la première correction est "Une couleur à la bonne place et 2 couleurs présentes mais mal placées", vous pouvez disposer 1 pion rouge et 2 pions blancs sur la première ligne de ce 2e plateau. Vous aurez donc en vis-à-vis, une sauvegarde de vos combinaisons et des corrections de celles-ci, ce qui vous aidera grandement à trouver la combinaison correcte!
Rappelez-vous que vous devez appuyer sur la tête de NAO pour chaque correction. 

---------- Enchainer les parties -----------

Une fois la partie finie, NAO relance le menu de jeu. Vous pouvez alors jouer à nouveau au même jeu ou choisir le second jeu. Pour sortir du menu, appuyez sur la tête de NAO.



