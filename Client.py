#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
import os
import json
import Operation
import Compte
import Historisation

class Client:
    def __init__(self, nom, mdp, adresse):
        self.id = newID()
        self.nom = nom
        self.mot_de_passe = mdp
        self.adresse = adresse
        self.compte = []
        self.historique = []
        self.operation = Operation.Operation(self)

    def setHistorique(self):
        pass

    def setID(self,id):
        self.id = id

    def _addCompteCourant(self, num, solde):
        compte = Compte.CompteCourant(num, solde)
        self.compte.append(compte)
        pass

    def _addCompteLivret(self, num, solde,interet):
        compte = Compte.CompteLivret(num, solde,interet)
        self.compte.append(compte)
        pass

    def envoyerReleve(self):
        for operation in self.historique:
            operation.printOperation()



def newID():
    id_clients = clientsId()
    ID = random.randint(100000,999999)
    compteur = 0
    while ID in id_clients:
        compteur += 1
        if compteur > 1000:
            return 0
        ID = random.randint(100000,999999)
    return ID


def clientsId():
    file = open("Sauvegarde/client.json", "r+")
    clients_db = list()
    clients_id = list()
    file.seek(0,2)
    if file.tell() > 1:
        file.seek(0, 0)
        clients_db = json.loads(file.read())
    else:
        pass
    for cli in clients_db:
        clients_id.append(cli["IDClient"])
    file.close()
    return clients_id


def connection(nom,mdp):
    client = None
    file = open("Sauvegarde/client.json", "r+")
    clients_db = list()
    file.seek(0, 2)
    if file.tell() > 1:
        file.seek(0, 0)
        clients_db = json.loads(file.read())
    else:
        pass
    file.close()
    for client in clients_db:
        if nom == client["nomClient"]:
            if mdp == client["mot_de_passe"]:
                return reCreeClient(client)
            else:
                pass
        else:
            pass
    return 0


def reCreeClient(client_data):
    client = Client(client_data["nomClient"],client_data["mot_de_passe"],client_data["adresseClient"])
    client.setID(client_data["IDClient"])
    for compte in client_data["comptes"]:
        if compte["compteType"] == "CompteCourant":
            client._addCompteCourant(compte["identifiant"],compte["solde"])
        elif compte["compteType"] == "CompteLivret":
            client._addCompteLivret(compte["identifiant"],compte["solde"],compte["interet"])
    for operation in client_data["historique"]:
        hist = Historisation.Historisation(operation["idCompte"],operation["montant"],operation["typeOperation"])
        hist.setDate(operation["Date"])
        client.historique.append(hist)
    return client