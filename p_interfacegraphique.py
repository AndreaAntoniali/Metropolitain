from __future__ import division
from tkinter import * 
import tkinter 
import time
from PIL import Image, ImageTk
import pickle

fen=Tk()
Descrip = StringVar()
Rep1 = StringVar()
Rep2 = StringVar()
Rep3 = StringVar()
def geoliste(g):
    r=[i for i in range(0,len(g))if not g[i].isdigit()]
    return [int(g[0:r[0]]),int(g[r[0]+1:r[1]]),int(g[r[1]+1:r[2]]),int(g[r[2]+1:])]

def update(delay=5):
    global ind
    ind += 1
    if ind == 6: ind = 0
    photo.configure(format="gif -index " + str(ind))
    fen.after(delay, update)#t
 
def centrefenetre(fen):
    fen.update_idletasks()
    l,h,x,y=geoliste(fen.geometry())
    l= 860 #longueur de la fenêtre 
    h=650 # hauteur de la fenêtre 
    fen.geometry("%dx%d%+d%+d" % (l,h,(fen.winfo_screenwidth()-l)//2,(fen.winfo_screenheight()-h)//2-50))
	
class Fenetre(tkinter.Frame):
     def _init_(self, master=None):
        tkinter.Frame._init_(elf, master)
     centrefenetre (fen)
     fen.resizable(width=False, height=False)
     fen.title("Métropolitain")
     fen['bg']='grey'

Description = Label(fen,width= 121,height=22,borderwidth=1,textvariable = Descrip, wraplength = 800)#fenetre de description
Description.place(x=5, y=5)
Label(fen,bg='BLACK',width=40,height=20,borderwidth=1).place(x= 572,y=342)
blue = Label(fen,bg='BLUE',width=80, height=20,borderwidth=1)
blue.place(x=5,y=342)

Reponses = Button(fen,bg='GREY',text='Inventaire',width=10, height=1,borderwidth=1).place(x=5,y=315)

#A partir d'ici, je code le jeu :
def Load(nom):
		with open(str(nom)+'.save', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier) #Je créé la fonction qui va importer le contenu de l'histoire. 
			global Scene
			Scene = mon_depickler.load()

Load("S1")#J'importe le fichier .save qui a été préalablement écrit : c'est l'histoire.
chainage = Scene[0][0] #Chainage va nous permetrre de travailler scène par scène, coordonnées par coordonnées.
Mike = False #Mike interviendra plus tard dans l'histoire.
#IJe définis mes variables qui seront le texte s'affichant sur les boites de dialogues.
def Affichage():
    global Rep1
    global Rep2
    global Rep3
    global Descrip
    if len(chainage.Reponses) == 3:
     Descrip.set(chainage.texte)
     Rep1.set(chainage.Reponses[0].texte)
     Rep2.set(chainage.Reponses[1].texte)
     Rep3.set(chainage.Reponses[2].texte)
    elif len(chainage.Reponses) == 2:
     Descrip.set(chainage.texte)
     Rep1.set(chainage.Reponses[0].texte)
     Rep2.set(chainage.Reponses[1].texte)
     Rep3.set("")
    else:
     Descrip.set(chainage.texte)
     Rep1.set(chainage.Reponses[0].texte)
     Rep2.set("")
     Rep3.set("")
if Mike == True:
     print("Mike :", chainage.mikeTexte)
Affichage()
def voyage(n):
    global chainage
    if n == 0 and Rep1.get() != "":
     chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
     Affichage()
    elif n == 1 and Rep1.get() != "":
     chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
     Affichage()
    elif n == 2 and Rep1.get() != "":
     chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
     Affichage()
    
#Ici, je définis les différents emplacements de réponses. Je fais la boite de dialogue.

Reponse1 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep1, fg = "WHITE") #Cadre pour la première réponse. 
Reponse1.bind("<Button-1>",lambda event, n = 0: voyage(n))
Reponse1.place(x = 0, y = 0)
B1 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=101) #Séparation entre la première et la deuxième.

Reponse2 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep2,  fg = "WHITE")#Cadre pour la deuxième réponse.
Reponse2.bind("<Button-1>",lambda event, n = 1: voyage(n))
Reponse2.place(x = 0, y = 102)
B2 = Label(blue,bg='WHITE',width=80,height=1).place(x=0,y=202) #Séparation entre la deuxième et la première.

Reponse3 = Label(blue, bg="BLACK", width=80, height = 7, borderwidth =1, textvariable = Rep3,  fg = "WHITE")#Cadre pour la troisième réponse.
Reponse3.bind("<Button-1>",lambda event, n = 2: voyage(n))
Reponse3.place(x = 0, y = 203)

#"Photo" de Mike
can = Canvas(fen, width=282, height=300, bg='white')
can.place(x= 570, y=342)
photo = PhotoImage(file="brouillage.gif")
can.create_image(0,0,anchor='nw', image=photo,tag='photo')


ind = -1

update()
 
fen.mainloop()
