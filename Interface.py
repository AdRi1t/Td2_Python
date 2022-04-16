import random
import tkinter.commondialog
import tkinter.font
import tkinter.colorchooser
from tkinter import *
import os
import Client
import Compte
import json
import Sauvegarde
import threading


class Interface:
    def __init__(self):
        self.button = {}
        self.frame = {}
        self.label = {}
        self.canvas = {}
        self.input = {}
        self.window_ctx = tkinter.Tk()
        self.window_ctx.title('Banque')
        self.window_ctx.geometry("1000x600")
        self.window_ctx.resizable(False, False)
        self.window_ctx.config(bg='#e7e6ff')
        pass

    def deletAll(self):
        self.button.clear()
        self.input.clear()
        self.label.clear()
        self.canvas.clear()
        for item in self.frame:
            self.frame[item].destroy()


Application = Interface()
client_global = 0
check_courant = 0
check_livret = 0

def menuPrincipale():
    global Application
    Application.deletAll()
    Application.frame["top_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu2_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.canvas["banque_canvas"] = tkinter.Canvas(Application.frame["top_frame"], bg="black", bd=0, height=2,width=1000, highlightthickness=0)
    Application.canvas["banque_canvas"].create_rectangle(0, 0, 1000, 4)
    Application.label["titre_principal"] = Label(Application.frame["top_frame"], font=("Segoe UI", 24), text="Banque",bg="#e7e6ff", relief="flat")
    Application.label["titre_menu"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 22),text="Menu principale", bg="#e7e6ff")
    Application.button["button_credit"] = tkinter.Button(Application.frame["menu_frame"], text="Crédit",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=16,highlightcolor="#e7e6ff", command=menuConection)
    Application.button["button_debit"] = tkinter.Button(Application.frame["menu_frame"], text="Débit",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=16,highlightcolor="#e7e6ff", command=menuConection)
    Application.button["button_virement"] = tkinter.Button(Application.frame["menu_frame"], text="Virement",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=16,highlightcolor="#e7e6ff", command=menuConection)
    Application.button["button_ouvrire_compte"] = tkinter.Button(Application.frame["menu_frame"], text="Ouvire compte",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=16,highlightcolor="#e7e6ff", command=menuOuvireCompte)
    Application.button["button_info_compte"] = tkinter.Button(Application.frame["menu_frame"], text="Détaille comptes",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=16,highlightcolor="#e7e6ff", command=menuConection)
    Application.button["button_historique"] = tkinter.Button(Application.frame["menu_frame"], text="Historique",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=16,highlightcolor="#e7e6ff", command=menuConection)
    Application.button["quitter"] = tkinter.Button(Application.frame["menu2_frame"], text="Quitter", font=("Segoe UI", 16),bg="#4afac3", relief="solid", width=15, highlightcolor="#e7e6ff",command=quit)
    Application.button["button_retour"] = tkinter.Button(Application.frame["menu2_frame"], text="Déconnection",font=("Segoe UI", 16), bg="#4afac3", relief="solid", width=15,highlightcolor="#e7e6ff", command=menuConection)
    Application.label["titre_principal"].grid(row=0, column=0, pady=(10, 10))
    Application.frame["top_frame"].grid(row=0, column=0,sticky="n", pady=(0, 40))
    Application.canvas["banque_canvas"].grid(row=1, column=0)

    Application.label["titre_menu"].grid(row=0,column=0,columnspan=3)
    Application.button["button_ouvrire_compte"].grid(row=1,column=0,padx=(5,5),pady=(10,10))
    Application.button["button_info_compte"].grid(row=1, column=1, padx=(5, 5), pady=(10, 10))
    Application.button["button_historique"].grid(row=1, column=2, padx=(5, 5), pady=(10, 10))
    Application.button["button_credit"].grid(row=2, column=0, padx=(5, 5), pady=(10, 10))
    Application.button["button_virement"].grid(row=2, column=1, padx=(5, 5), pady=(10, 10))
    Application.button["button_debit"].grid(row=2, column=2, padx=(5, 5), pady=(10, 10))
    Application.frame["menu_frame"].grid(row=1,column=0,pady=20)

    Application.button["quitter"].pack(side="right",padx=20)
    Application.button["button_retour"].pack(side="left",padx=20)
    Application.frame["menu2_frame"].grid(row=2,column=0,sticky="s",pady=(20,0))
    Application.frame["menu_frame"].grid(row=1,column=0,pady=20)
    Application.window_ctx.mainloop()


def menuOuvireCompte():
    global Application
    global client_global
    global check_courant
    global check_livret
    check_courant = IntVar()
    check_livret = IntVar()
    Application.deletAll()
    Application.frame["top_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu2_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.label["titre_principal"] = Label(Application.frame["top_frame"], font=("Segoe UI", 24), text="Banque",bg="#e7e6ff", relief="flat")
    Application.canvas["banque_canvas"] = tkinter.Canvas(Application.frame["top_frame"], bg="black", bd=0, height=2,width=1000, highlightthickness=0)
    Application.canvas["banque_canvas"].create_rectangle(0, 0, 1000, 4)
    Application.label["titre_menu"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 22),text="Ouvrire un compte", bg="#e7e6ff")
    Application.input["courant_input"] = tkinter.Checkbutton(Application.frame["menu_frame"],text="Compte courant", font=("Segoe UI", 18),bg="#e7e6ff", relief="solid",width=16,selectcolor="#e7e6ff",activebackground="#e7e6ff",command=checkCompteCourant)
    Application.input["livret_input"] = tkinter.Checkbutton(Application.frame["menu_frame"], text="Compte sur livret",font=("Segoe UI", 18), bg="#e7e6ff", relief="solid",width=16, selectcolor="#e7e6ff",activebackground="#e7e6ff",command=checkCompteLivret)
    Application.button["button_retour"] = tkinter.Button(Application.frame["menu2_frame"], text="Retour",font=("Segoe UI", 16), bg="#4afac3", relief="solid", width=15,highlightcolor="#e7e6ff", command=menuPrincipale)

    Application.label["titre_principal"].grid(row=0, column=0, pady=(10, 10))
    Application.canvas["banque_canvas"].grid(row=1, column=0)
    Application.frame["top_frame"].grid(row=0, column=0, sticky="n", pady=(0, 40))
    Application.label["titre_menu"].grid(row=0, column=0,columnspan=2)
    Application.input["courant_input"].grid(row=1, column=0, pady=10, padx=15)
    Application.input["livret_input"].grid(row=1, column=1, pady=10, padx=15)
    Application.frame["menu_frame"].grid(row=1, column=0, pady=20)
    Application.button["button_retour"].grid(row=0, column=0)
    Application.frame["menu2_frame"].grid(row=2, column=0, sticky="s", pady=(20,0))
    Application.window_ctx.mainloop()


def checkCompteLivret():
    global Application
    global check_courant
    global check_livret
    if check_livret == 1:
        Application.input["interet_input"].destroy()
        Application.input["courant_input"].configure(bg="#4afac3")
        Application.input["livret_input"].configure(bg="#e7e6ff")
        Application.input["livret_input"].deselect()
        check_livret = 0
    else:
        Application.input["livret_input"].configure(bg="#4afac3")
        Application.input["interet_input"] = Scale(Application.frame["menu_frame"], orient='horizontal', from_=0, to=5,font=("Segoe UI", 16), resolution=0.05, tickinterval=0.5,bg="#e7e6ff", length=500, label='Interet %', bd=0, relief="flat",highlightthickness=0)
        Application.input["interet_input"].grid(row=2, column=0, columnspan=2, pady=20)
        Application.input["livret_input"].select()
        check_livret = 1
    if check_courant == 1:
        Application.input["livret_input"].configure(bg="#4afac3")
        Application.input["courant_input"].configure(bg="#e7e6ff")
        Application.input["interet_input"] = Scale(Application.frame["menu_frame"], orient='horizontal', from_=0, to=5,font=("Segoe UI", 16), resolution=0.05, tickinterval=0.5,bg="#e7e6ff", length=500, label='Interet %', bd=0, relief="flat",highlightthickness=0)
        Application.input["interet_input"].grid(row=2, column=0, columnspan=2, pady=20)
        check_courant = 0
        Application.input["courant_input"].deselect()
        Application.input["livret_input"].select()
        check_livret = 1
    Application.window_ctx.mainloop()


def checkCompteCourant():
    global Application
    global check_courant
    global check_livret
    if check_courant == 1:
        Application.input["livret_input"].configure(bg="#4afac3")
        Application.input["courant_input"].configure(bg="#e7e6ff")
        Application.input["courant_input"].deselect()
        check_courant = 0
    else:
        Application.input["courant_input"].configure(bg="#4afac3")
        Application.input["courant_input"].select()
        check_courant = 1
    if check_livret == 1:
        Application.input["interet_input"].destroy()
        Application.input["courant_input"].configure(bg="#4afac3")
        Application.input["livret_input"].configure(bg="#e7e6ff")
        check_courant = 1
        Application.input["livret_input"].deselect()
        Application.input["courant_input"].select()
        check_livret = 0
    Application.window_ctx.mainloop()
    choix = "0"
    if choix == "a":
        client_global._addCompteCourant("222", 0)
    if choix == "b":
        while interet == "aucun" or interet > 10:
            interet = float(input("Intérêt : "))
        client_global._addCompteLivret("222", 0, interet)


def menuCreeCompte():
    global Application
    Application.deletAll()
    Application.frame["top_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.canvas["banque_canvas"] = tkinter.Canvas(Application.frame["top_frame"], bg="black", bd=0, height=2,width=1000, highlightthickness=0)
    Application.canvas["banque_canvas"].create_rectangle(0, 0, 1000, 4)
    Application.label["titre_principal"] = Label(Application.frame["top_frame"], font=("Segoe UI", 24), text="Banque",bg="#e7e6ff", relief="flat")
    Application.label["titre_menu"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 22), text="Nouveau compte",bg="#e7e6ff")
    Application.label["nom"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 16), text="Nom", bg="#e7e6ff")
    Application.label["adresse"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 16), text="Adresse", bg="#e7e6ff")
    Application.label["mdp"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 16), text="Mot de passe",bg="#e7e6ff")
    Application.input["nom_input"] = tkinter.Entry(Application.frame["menu_frame"], font=("Segoe UI", 18),relief="solid", bg="#bdf6ff")
    Application.input["adresse_input"] = tkinter.Entry(Application.frame["menu_frame"], font=("Segoe UI", 18),relief="solid", bg="#bdf6ff")
    Application.input["mdp_input"] = tkinter.Entry(Application.frame["menu_frame"], font=("Segoe UI", 18),relief="solid", bg="#bdf6ff", show='#')
    Application.button["entrer"] = tkinter.Button(Application.frame["menu_frame"], text="Entrer", font=("Segoe UI", 18),bg="#4afac3", relief="solid", width=20, highlightcolor="#e7e6ff",command=checkEntryCreeCompte)
    Application.button["button_retour"] = tkinter.Button(Application.frame["menu_frame"], text="Retour",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=20,highlightcolor="#e7e6ff", command=menuConection)

    Application.label["titre_principal"].grid(row=0, column=0, pady=(10, 10))
    Application.frame["top_frame"].pack(fill="x", pady=(0, 40))
    Application.canvas["banque_canvas"].grid(row=1, column=0)

    Application.label["titre_menu"].pack()
    Application.label["nom"].pack()
    Application.input["nom_input"].pack()
    Application.label["adresse"].pack()
    Application.input["adresse_input"].pack()
    Application.label["mdp"].pack()
    Application.input["mdp_input"].pack()
    Application.button["entrer"].pack(pady=(20, 0),)
    Application.button["button_retour"].pack(pady=(10, 0))
    Application.frame["menu_frame"].pack()
    Application.window_ctx.mainloop()


def checkEntryCreeCompte():
    global client_global
    nom = "_"
    file = open("Sauvegarde/client.json", "r+")
    clients_db = list()
    clients_name = list()
    file.seek(0, 2)

    if file.tell() > 1:
        file.seek(0, 0)
        clients_db = json.loads(file.read())
    else:
        pass
    file.close()

    for cli in clients_db:
        clients_name.append(cli["nomClient"])

    nom = Application.input["nom_input"].get()
    adresse = Application.input["adresse_input"].get()
    mdp = Application.input["mdp_input"].get()
    if nom in clients_name:
        print("---Client déja crée  !!!")
    if nom != "_" and len(nom) > 2 and len(mdp) > 2 and nom not in clients_name:
        client_global = Client.Client(nom, mdp, adresse)
        Sauvegarde.sauvegarde(client_global)
        print("----Client crée !")
        menuPrincipale()
    else:
        print("----Client invalide !")
        menuCreeCompte()


def menuCrediter(client):
    choix = "aucun"
    if len(client.compte) == 0:
        print("----Client sans Compte !!!")
        return
    print("----Crédit compte----")
    print("----Choisir Compte ----")
    i = 0
    while choix == "aucun" or choix > i or choix < 0:
        i = 0
        for compte in client.compte:
            print("{} -{} n°{}  soldes: {}".format(i, type(compte).__name__, compte.numero, compte.solde))
            i += 1
        choix = int(input("choix :"))
    montant = int(input("montant: "))
    client.operation.crediter(client.compte[choix], montant)
    return


def menuVirement(client_origine):
    i = 0
    choix_origine = "aucun"
    client_name = []
    nom_destination = "_"
    choix_destination = "aucun"
    print("----Virement----")
    file = open("Sauvegarde/client.json", "r+")
    clients_db = list()
    file.seek(0, 2)
    if file.tell() > 1:
        file.seek(0, 0)
        clients_db = json.loads(file.read())
    else:
        return
    print("----Choisir Compte départ----")
    i = 0
    while choix_origine == "aucun" or choix_origine > i or choix_origine < 0:
        i = 0
        for compte in client_origine.compte:
            print("{} -{} n°{}  soldes: {}".format(i, type(compte).__name__, compte.numero, compte.solde))
            i += 1
        choix_origine = int(input("choix :"))
    montant = int(input("montant: "))

    for client in clients_db:
        client_name.append(client["nomClient"])

    while nom_destination not in client_name:
        nom_destination = input("Destinataire : ")

    for client in clients_db:
        if nom_destination == client["nomClient"]:
            client_destination = client

    client_destination = Client.connection(client_destination["nomClient"], client_destination["mot_de_passe"])

    print("----Choisir Compte déstination----")
    print("Destinataire {}".format(client_destination.nom))
    while choix_destination == "aucun" or choix_destination > i or choix_destination < 0:
        i = 0
        for compte in client_destination.compte:
            print("{} -{} n°{}  soldes: {}".format(i, type(compte).__name__, compte.numero, compte.solde))
            i += 1
        choix_destination = int(input("choix :"))
    client_origine.operation.virement(client_origine.compte[choix_origine], client_destination,client_destination.compte[choix_destination], montant)


def menuDebiter(client):
    choix = "aucun"
    if len(client.compte) == 0:
        print("----Client sans Compte !!!")
        return
    print("----Débit compte----")
    print("----Choisir Compte ----")
    i = 0
    while choix == "aucun" or choix > i or choix < 0:
        i = 0
        for compte in client.compte:
            print("{} -{} n°{}  soldes: {}".format(i, type(compte).__name__, compte.numero, compte.solde))
            i += 1
        choix = int(input("choix :"))
    montant = int(input("montant: "))
    client.operation.debiter(client.compte[choix], montant)
    return


def connectionClient():
    global Application
    Application.deletAll()
    Application.frame["top_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.canvas["banque_canvas"] = tkinter.Canvas(Application.frame["top_frame"], bg="black", bd=0, height=2,width=1000, highlightthickness=0)
    Application.canvas["banque_canvas"].create_rectangle(0, 0, 1000, 4)
    Application.label["titre_principal"] = Label(Application.frame["top_frame"], font=("Segoe UI", 24), text="Banque",bg="#e7e6ff", relief="flat")
    Application.label["titre_menu"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 22),text="Se connecter", bg="#e7e6ff")
    Application.label["nom"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 16), text="Nom", bg="#e7e6ff")
    Application.label["mdp"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 16), text="Mot de passe",bg="#e7e6ff")
    Application.input["nom_input"] = tkinter.Entry(Application.frame["menu_frame"],font=("Segoe UI", 18),relief="solid",bg="#bdf6ff")
    Application.input["mdp_input"] = tkinter.Entry(Application.frame["menu_frame"], font=("Segoe UI", 18),relief="solid", bg="#bdf6ff",show='#')
    Application.button["entrer"] = tkinter.Button(Application.frame["menu_frame"],text="Entrer",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=20,highlightcolor="#e7e6ff",command=checkEntryConnection)
    Application.button["button_retour"] = tkinter.Button(Application.frame["menu_frame"], text="Retour",font=("Segoe UI", 18), bg="#4afac3", relief="solid", width=20,highlightcolor="#e7e6ff", command=menuConection)

    Application.label["titre_principal"].grid(row=0, column=0, pady=(10, 10))
    Application.frame["top_frame"].pack(fill="x", pady=(0, 50))
    Application.canvas["banque_canvas"].grid(row=1, column=0)

    Application.label["titre_menu"].pack()
    Application.label["nom"].pack()
    Application.input["nom_input"].pack()
    Application.label["mdp"].pack()
    Application.input["mdp_input"].pack()
    Application.button["entrer"].pack(pady=(20,0))
    Application.button["button_retour"].pack(pady=(10,0))
    Application.frame["menu_frame"].pack()
    Application.window_ctx.mainloop()



def checkEntryConnection():
    global Application
    global client_global
    nom = "_"
    client = 0
    file = open("Sauvegarde/client.json", "r+")
    clients_name = list()
    file.seek(0, 2)
    if file.tell() > 1:
        file.seek(0, 0)
        clients_db = json.loads(file.read())
    else:
        print("Aucun client sauvegarder")
        return menuCreeCompte()
    file.close()
    for cli in clients_db:
        clients_name.append(cli["nomClient"])

    nom = Application.input["nom_input"].get()
    mdp = Application.input["mdp_input"].get()
    client_global = Client.connection(nom, mdp)
    if client_global == 0:
        print("---Non connecté !!!")
        connectionClient()
    else:
        print("----connecté----")
        menuPrincipale()


def menuConection():
    global Application
    Application.deletAll()
    Application.frame["top_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.frame["menu_frame"] = tkinter.Frame(Application.window_ctx, bg="#e7e6ff")
    Application.canvas["banque_canvas"] = tkinter.Canvas(Application.frame["top_frame"], bg="black", bd=0, height=2, width=1000, highlightthickness=0)
    Application.canvas["banque_canvas"].create_rectangle(0, 0, 1000, 4)
    Application.label["titre_principal"] = Label(Application.frame["top_frame"], font=("Segoe UI", 24), text="Banque", bg="#e7e6ff", relief="flat")
    Application.label["titre_menu"] = Label(Application.frame["menu_frame"], font=("Segoe UI", 22), text="Menu Connection", bg="#e7e6ff")
    Application.button["button_connection"] = tkinter.Button( Application.frame["menu_frame"], text="Connection", font=("Segoe UI", 18), bg="#4afac3",relief="solid", width=20, highlightcolor="#e7e6ff", command=connectionClient)
    Application.button["button_cree_compte"] = tkinter.Button(Application.frame["menu_frame"], text="Nouveau compte", font=("Segoe UI", 18), bg="#4afac3",relief="solid", width=20, highlightcolor="#e7e6ff", command=menuCreeCompte)
    Application.button["button_quit"] = tkinter.Button(Application.frame["menu_frame"], text="Quitter", font=("Segoe UI", 18), bg="#4afac3", relief="solid",width=20, highlightcolor="#e7e6ff", command=quit)

    Application.label["titre_principal"].grid(row=0, column=0, pady=(10, 10))
    Application.canvas["banque_canvas"].grid(row=1, column=0)
    Application.frame["top_frame"].pack(fill="x", pady=(0, 50))
    Application.label["titre_menu"].pack()
    Application.button["button_connection"].pack(pady=10)
    Application.button["button_cree_compte"].pack(pady=10)
    Application.button["button_quit"].pack(pady=10)
    Application.frame["menu_frame"].pack()
    Application.window_ctx.mainloop()
