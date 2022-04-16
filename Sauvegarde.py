#!/usr/bin/python
#-*- coding: utf-8 -*-
import sys
from json import *
import os
import json
import Client
import Compte
import Historisation
import Operation


def checkRepSauvegarde():
    mwd = os.getcwd()
    if os.path.exists(os.curdir+"/Sauvegarde"):
        os.chdir(os.curdir + "/Sauvegarde")
        if os.path.exists(os.curdir+"/client.json"):
            pass
        else:
            fichier_sauvegarde = open("client.json", "w")
            fichier_sauvegarde.close()
    else:
        os.mkdir("Sauvegarde")
        os.chdir(os.curdir + "/Sauvegarde")
        fichier_sauvegarde = open("client.json", "w")
        fichier_sauvegarde.close()
    os.chdir(mwd)


def sauvegarde(client):
    print(os.getcwd())
    file = open("Sauvegarde/client.json", "r+")
    clients = list()
    file.seek(0,2)
    if file.tell() > 1:
        file.seek(0, 0)
        clients = json.loads(file.read())

    indexe = 0
    for cli in clients:
        indexe += 1
        if cli["IDClient"] == client.id:
            clients.remove(cli)

    comptes_json = list()
    for compte in client.compte:
        if type(compte).__name__ == "CompteLivret":
            comptes_json.append({"compteType": type(compte).__name__, "identifiant": compte.numero, "solde": compte.solde,"interet": compte.interet})
        elif type(compte).__name__ == "CompteCourant":
            comptes_json.append({"compteType": type(compte).__name__, "identifiant": compte.numero, "solde": compte.solde})
    historique_json = list()
    for historique in client.historique:
        historique_json.append({"Date": historique.date, "typeOperation": historique.libelle, "montant": historique.montant, "idCompte": historique.IDCompte})

    client_json = dict()
    client_json["IDClient"] = client.id
    client_json["nomClient"] = client.nom
    client_json["mot_de_passe"] = client.mot_de_passe
    client_json["adresseClient"] = client.adresse
    client_json["comptes"] = comptes_json
    client_json["historique"] = historique_json
    clients.append(client_json)
    data_client = json.dumps(clients,indent=4,ensure_ascii=False)
    file.seek(0, 0)
    file.write(data_client)
    file.close()