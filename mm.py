# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 18:52:01 2020

@author: pauli
"""

from random import randrange

if __name__ == "__main__":
    
    #On commence par afficher les instructions dés que le joueur sélectionne le MasterMind
    print("Instructions : ...")
    
    #On commence une partie, possibilité de rejouer si l'utilisateur demande
    stop = False
    while(stop == False):
        
        #NAO choisit la combinaison de couleurs de la partie
        combi = []
        for i in range(4):
            nb = randrange(4)
            if (nb == 0):
                combi.append('r')
            elif (nb == 1):
                combi.append('b')
            elif (nb == 2):
                combi.append('j')
            else:
                combi.append('v')
        
        trouve = False
        essais_max = 10
        k = 0
        #On recommence tant que l'utilisateur n'a pas trouvé la solution / dépassé le nombre d'essais maximum
        while ((trouve == False) and (k < essais_max)):
            k += 1
            combi_utilisateur = []
            rep_nao = []
            
            #L'utilisateur propose une solution
            for i in range(4):
                couleur_ok = False #Vérifie que l'utilisateur entre une couleur valide
                while(couleur_ok == False):
                    choix = input("Choisissez la couleur de la boule " + str(i+1) + " parmi : rouge (r), bleu (b), jaune (j) ou vert (v)\n")
                    if ((choix == 'b') or (choix == 'v') or (choix == 'j') or (choix == 'r')):
                        couleur_ok = True
                        combi_utilisateur.append(choix)
                    else:
                        print("Vous n'avez pas sélectionné une couleur valide. Réessayez")
            
            #NAO vérifie la combinaison entrée par l'utilisateur et donne sa réponse
            for i in range(4):
                if (combi[i] == combi_utilisateur[i]):
                    rep_nao.append("ok")
                elif (combi.count(combi_utilisateur[i]) > 0):
                    rep_nao.append("mal placé")
                else:
                    rep_nao.append("pas ok")
            print(rep_nao)
            if (combi == combi_utilisateur):
                print("Bravo, vous avez gagné !")
                trouve = True
        
        
        if (trouve == False):
            print("Vous n'avez pas trouvé la combinaison. J'ai donc gagné :D")
            print("La combinaison était : ")
            print(combi)
        rejoue = input("On rejoue ? (o/n)")
        if (rejoue == 'n'):
            stop = True
                
                
    
        