#!/usr/bin/python
#-*- coding: utf-8 -*-
import Compte
import Historisation
import Client
import Sauvegarde

class Operation:
    def __init__(self,Client):
        self.client = Client
        pass

    def debiter(self, compte, montant):
        if type(montant) == int and compte.getSolde() > montant:
            compte.setSolde(compte.getSolde() - montant)
            save = Historisation.Historisation(compte.numero, montant, "débit")
            self.client.historique.insert(0,save)
        else:
            print("Error in {}".format(__file__))
            return


    def crediter(self, compte, montant):
        if type(montant) == int:
            compte.setSolde(compte.getSolde() + montant)
            save = Historisation.Historisation(compte.numero, montant, "dépos")
            self.client.historique.insert(0, save)
        else:
            print("Error mauvais type in {}".format(__file__))
            return

    def virement(self, CompteEmetteur,client_recepteur,CompteDestination, montant):
        if type(montant) == int:
            CompteEmetteur.setSolde(CompteEmetteur.getSolde() - montant)
            CompteDestination.setSolde(CompteDestination.getSolde() + montant)
            save_origine = Historisation.Historisation(CompteEmetteur.numero, montant, "virement")
            self.client.historique.insert(0, save_origine)
            save_destination = Historisation.Historisation(CompteDestination.numero, montant, "virement")
            client_recepteur.historique.insert(0, save_destination)
            Sauvegarde.sauvegarde(client_recepteur)
        else:
            print("Error mauvais type in {}".format(__file__))
            return

    def crediter_interet(self,compte):
        montant = compte.getSolde()*compte.getInteret()/100
        compte.setSolde(compte.getSolde() + montant)
        save = Historisation.Historisation(compte, montant, "intérêt")
        self.client.historique.insert(0, save)

