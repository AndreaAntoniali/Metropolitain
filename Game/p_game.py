import pickle
Scene = [[]]
def Load(nom):
		with open(str(nom)+'.save', 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			global Scene
			Scene = mon_depickler.load()
Load("S1")
chainage = Scene[0][0]
Mike = False
def Affichage():
    if len(chainage.Reponses) == 3:
     print("Description :", chainage.texte)
     print("Réponse 1 :", chainage.Reponses[0].texte)
     print("Réponse 2 :", chainage.Reponses[1].texte)
     print("Réponse 3 :", chainage.Reponses[2].texte)
    elif len(chainage.Reponses) == 2:
     print("Description :", chainage.texte)
     print("Réponse 1 :", chainage.Reponses[0].texte)
     print("Réponse 2 :", chainage.Reponses[1].texte)
    else:
     print("Description :", chainage.texte)
     print("Réponse 1 :", chainage.Reponses[0].texte)

if Mike == True:
     print("Mike :", chainage.mikeTexte)
     
def voyage(n):
 global chainage
 chainage = Scene[chainage.Reponses[n].pos.x][chainage.Reponses[n].pos.z]
 
while(True):
    Affichage()
    voyage(int(input("Réponse -> ")))
    print("\n")
