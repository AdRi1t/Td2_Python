#!/usr/bin/python
#-*- coding: utf-8 -*-
import datetime

class Historisation:
    def __init__(self, numero_compte, montant, type):
        self.date = datetime.datetime.now().isoformat()
        self.libelle = type
        self.IDCompte = numero_compte
        self.montant = montant

    def setDate(self,date):
        self.date = date

    def setIDCompte(self, id):
        self.IDCompte = id

    def printOperation(self):
        print("Compte n° {} .  Le {}   . Operation: {} de {} ".format(self.IDCompte,self.date,self.libelle, self.montant))
