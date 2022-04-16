import Compte
import Interface
import Client
import random
import Operation
import Sauvegarde
import os


def main():
    print("---Début programme---")
    Sauvegarde.checkRepSauvegarde()
    client = Interface.menuConection()
    choix = "aucun"
    while choix != "q":
        choix = "aucun"
        choix = choix.lower()
        if choix == "a":
            Interface.menuOuvireCompte(client)
        if choix == "b":
            Interface.menuDebiter(client)
        if choix == "c":
            Interface.menuCrediter(client)
        if choix == "d":
            Interface.menuVirement(client)
        if choix == "e":
            client.envoyerReleve()
        if choix == "f":
            for compte in client.compte:
                compte.info_compte()
    Sauvegarde.sauvegarde(client)
    pass


if __name__ == '__main__':
    main()



