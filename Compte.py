#!/usr/bin/python
#-*- coding: utf-8 -*-


class Compte:
    def __init__(self, num, solde):
        self.numero = num
        self.solde = solde

    def setSolde(self, solde):
        self.solde = solde

    def getSolde(self):
        return self.solde


class CompteCourant(Compte):
    def __init__(self, num, solde):
        Compte.__init__(self,num,solde)

    def info_compte(self):
        print(f'Compte courant n° {self.numero}  solde : {self.solde}')


class CompteLivret(Compte):
    def __init__(self, num, solde, interet):
        Compte.__init__(self,num,solde)
        self.interet = interet

    def info_compte(self):
        print(f'Compte livret n° {self.numero}  solde : {self.solde} interet {self.interet}')

    def getInteret(self):
        return self.interet
