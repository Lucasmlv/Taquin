###                            Projet d'informatique 19 : Jeu du Taquin             ###
'''GERME Marceau, MAKARISON MAC MIOU FO Jolyane, HAVRET Benjamin'''

### Bibliothèques utilisées
import random as r
import numpy as np
from tkinter import *
import os

os.chdir('C:/Users/bavre/OneDrive/Bureau/Projet Info/image/imaged')

### Initialisation du Taquin

Taquin_fini = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]])
T=[]


def Recherche_nombre(n,T):
    for i in range (4):
        for j in range (4):
            if T[i][j]==n:
                l=i
                c=j
                break
    return (l,c)



def Taquin_resolvable():
    '''La fonction génère un taquin après avoir vérifié qu'il soit résolvable'''
    deplacement=0
    T=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,0]]
    (l0,c0)=Recherche_nombre(0,T)
    for k in range (200):
        for h in range (4):
            for j in range(4):
                if T[h][j]==0:
                    x0=j
                    y0=h

        p=r.randint(1,4)
        if p==1 and y0!=0:
            T[l0][c0],T[l0-1][c0]=T[l0-1][c0],T[l0][c0] # déplacement vers le haut
            deplacement=deplacement+1
            l0=l0-1
        if p==2 and y0!=3:
            T[l0][c0],T[l0+1][c0]=T[l0+1][c0],T[l0][c0] # déplacement vers le bas
            deplacement=deplacement+1
            l0=l0+1
        if p==3 and x0!=0:
            T[l0][c0],T[l0][c0-1]=T[l0][c0-1],T[l0][c0] # déplacement vers la gauche
            deplacement=deplacement+1
            c0=c0-1
        if p==4 and x0!=3:
            T[l0][c0],T[l0][c0+1]=T[l0][c0+1],T[l0][c0] # déplacement vers la droite
            deplacement=deplacement+1
            c0=c0+1
    while l0!=3:                                        # déplacement du 0 en bas à droite
        T[l0][c0]=T[l0+1][c0]
        T[l0+1][c0]=0
        l0=l0+1
        deplacement=deplacement+1
    while c0!=3:
        T[l0][c0]=T[l0][c0+1]
        T[l0][c0+1]=0
        c0=c0+1
        deplacement=deplacement+1
    return (T)



def Taquin_fini_verifier(T):
    '''1er argument -> tableau de type array
    La fonction permet de vérifier si le taquin est résolu ou non'''

    a = True
    for i in range (4):
        for j in range (4):
            if Taquin_fini[i][j]!=T[i][j]:
                a = False
    return a

### Jouabilité

def compresserd(T,i,j):
    '''1er argument: T -> tableau de type array
    2eme argument: i -> int
    3ème argument: j -> int
    La fonction renvoie un tableau après le déplacement d'1 à 3 cases vers la droite'''

    for l in range (3-i):
        if T[j][3-l]==0 and T[j][2-l]!=0:
            T[j][3-l]=T[j][2-l]
            T[j][2-l]=0
    return (T)


def compresserg(T,i,j):
    '''1er argument: T -> tableau de type array
    2eme argument: i -> int
    3eme argument : j -> int
    La fonction renvoie un tableau après le déplacement d'1 à 3 cases vers la gauche en partant de la case [i][j]'''

    for l in range (i):
        if T[j][l]==0 and T[j][1+l]!=0:
            T[j][l]=T[j][1+l]
            T[j][1+l]=0
    return (T)


def compresserb(T,i,j):
    '''1er argument: T -> tableau de type array
    2eme argument: i -> int
    3eme argument : j -> int
    La fonction renvoie un tableau après le déplacement d'1 à 3 cases vers le bas en partant de la case [i][j]'''

    for l in range (3-j):
        if T[3-l][i]==0 and T[2-l][i]!=0:
            T[3-l][i]=T[2-l][i]
            T[2-l][i]=0
    return (T)


def compresserh(T,i,j):
    '''1er argument: T -> tableau de type array
    2eme argument: i -> int
    3eme argument : j -> int
    La fonction renvoie un tableau après le déplacement d'1 à 3 cases vers le haut en partant de la case [i][j]'''
    for l in range (j):
        if T[l][i]==0 and T[1+l][i]!=0:
            T[l][i]=T[1+l][i]
            T[1+l][i]=0
    return (T)


def verifiermouvement(T,i,j):
    '''1er argument: T -> tableau de type array
    2eme argument: i -> int
    3eme argument : j -> int
    La fonction renvoie le type de mouvements possibles ou 'aucun' si aucun mouvement n'est possible dans le tableau à partir des indices i et j'''

    mvt='aucun'
    for k in range (i):
        if T[j][k]==0:
            mvt='horizontalgauche'
    for k in range (i,4):
        if T[j][k]==0:
            mvt='horizontaldroite'

    for k in range(j):
        if T[k][i]==0:
            mvt='verticalhaut'
    for k in range (j,4):
        if T[k][i]==0:
            mvt='verticalbas'

    return(mvt)


def deplacement(event):
    '''1er argument: event -> évènement
    La fonction effectue des déplacements lorsque l'utilisateur appuie sur les touches et affiche le taquin après déplacement
    La fonction sera appelée pour afficher l'interface'''
    touche=event.keysym
    deplacement=0

    (l0,c0)=Recherche_nombre(0,T)

    if touche == 'z' and l0 != 0 :                 # déplacement vers le haut
        T[l0][c0],T[l0-1][c0]=T[l0-1][c0],T[l0][c0]
        deplacement=deplacement+1
        l0=l0-1
    elif touche == 's' and l0 != 3 :               # déplacement vers le bas
        T[l0][c0],T[l0+1][c0]=T[l0+1][c0],T[l0][c0]
        deplacement=deplacement+1
        l0=l0+1
    elif touche == 'q' and c0 != 0 :               # déplacement vers la gauche
        T[l0][c0],T[l0][c0-1]=T[l0][c0-1],T[l0][c0]
        deplacement=deplacement+1
        c0=c0-1
    elif touche == 'd' and c0 != 3 :               # déplacement vers la droite
        T[l0][c0],T[l0][c0+1]=T[l0][c0+1],T[l0][c0]
        deplacement=deplacement+1
        c0=c0+1
    if z == 2:
        ret = affichage2(T)
    else:
        ret = affichage1(T)
    return(ret)


def deplacementsouris(event):
    '''1er argument : event -> évènement
    La fonction, en fonction des possibilités de déplacements, effectuera des mouvements de cases lorsque le joueur sollicitera sa souris
    La fonction renvoie le tableau après déplacements'''
    x=event.x       # coordonnée en x de la case que le joueur aura cliqué
    y=event.y       # coordonnée en y de la case que le joueur aura cliqué
    i=int(x/200)   # indice associée à la coordonnée en x
    j=int(y/200)   # indice associée à la coordonnée en y
    global T

    r = verifiermouvement(T,i,j)
    if r == 'verticalbas':
        T = compresserb(T,i,j)
    if r == 'verticalhaut':
        T = compresserh(T,i,j)
    if r == 'horizontalgauche':
        T = compresserg(T,i,j)
    if r == 'horizontaldroite':
        T = compresserd(T,i,j)
    if z == 1:
        ret = affichage1(T)
    else:
        ret = affichage2(T)
    return(ret)

### Affichage de l'interface

global root
root = Tk()      # création de la fenêtre d'accueil
root.title("Mode de jeu")
root.geometry("800x800") # dimensionnement de la fenêtre d'accueil
root.configure(background="white")


label=Label(root, text="MAKARISON Jolyane, GERME Marceau, HAVRET Benjamin",bg="white",fg="black",font="Helvetic 16 italic")
label.place(relx=0.14, rely=0.4) # création d'une zone de texte

label1=Label(root,text="LE JEU DU TAQUIN",bg="white",fg="IndianRed3",font="calibri 36 bold")
label1.place(relx=0.27, rely=0.1)


## Jeu avec des images
def affichage1(h): # affichage de l'interface avec les images
    canvas.delete(ALL) # permet d'actualiser l'affichage de l'interface après chaque mouvement effectué
    i=0

    for k in range (4):
        j=0
        if k == 0:
            i += 100
        else:
            i += 200
        for m in range (4):
            if m == 0:
                j += 100
            else:
                j += 200
            if h[m][k] != 0:
                if h[m][k] == 1:
                    canvas._photo1 = photo1 = PhotoImage(file="1.gif")
                    canvas.create_image(i,j,image=photo1)
                if h[m][k] == 2:
                    canvas._photo2 = photo2 = PhotoImage(file="2.gif")
                    canvas.create_image(i,j,image=photo2)
                if h[m][k] == 3:
                    canvas._photo3 = photo3 = PhotoImage(file="3.gif")
                    canvas.create_image(i,j,image=photo3)
                if h[m][k] == 4:
                    canvas._photo4 = photo4 = PhotoImage(file="4.gif")
                    canvas.create_image(i,j,image=photo4)
                if h[m][k] == 5:
                    canvas._photo5 = photo5 = PhotoImage(file="5.gif")
                    canvas.create_image(i,j,image=photo5)
                if h[m][k] == 6:
                    canvas._photo6 = photo6 = PhotoImage(file="6.gif")
                    canvas.create_image(i,j,image=photo6)
                if h[m][k] == 7:
                    canvas._photo7 = photo7 = PhotoImage(file="7.gif")
                    canvas.create_image(i,j,image=photo7)
                if h[m][k] == 8:
                    canvas._photo8 = photo8 = PhotoImage(file="8.gif")
                    canvas.create_image(i,j,image=photo8)
                if h[m][k] == 9:
                    canvas._photo9 = photo9 = PhotoImage(file="9.gif")
                    canvas.create_image(i,j,image=photo9)
                if h[m][k] == 10:
                    canvas._photo10 = photo10 = PhotoImage(file="10.gif")
                    canvas.create_image(i,j,image=photo10)
                if h[m][k] == 11:
                    canvas._photo11 = photo11 = PhotoImage(file="11.gif")
                    canvas.create_image(i,j,image=photo11)
                if h[m][k] == 12:
                    canvas._photo12 = photo12 = PhotoImage(file="12.gif")
                    canvas.create_image(i,j,image=photo12)
                if h[m][k] == 13:
                    canvas._photo13 = photo13 = PhotoImage(file="13.gif")
                    canvas.create_image(i,j,image=photo13)
                if h[m][k] == 14:
                    canvas._photo14 = photo14 = PhotoImage(file="14.gif")
                    canvas.create_image(i,j,image=photo14)
                if h[m][k] == 15:
                    canvas._photo15 = photo15 = PhotoImage(file="15.gif")
                    canvas.create_image(i,j,image=photo15)

                canvas.pack()

def Jouer1():
    '''création d'une fonction qui affichera la fenêtre de jeu contenant le taquin
    La fonction a été créée pour être utilisée comme commande pour jouer avec les images'''

    global canvas, T
    global z
    z = 1
    T= Taquin_resolvable()
    root.destroy() # ferme la fenêtre d'accueil 'root'
    fenetre=Tk()
    fenetre.title("TAQUIN")
    canvas = Canvas(fenetre, width=800, height=800, background='antiquewhite1')

    affichage1(T) # affiche le Taquin

    fenetre.focus_set() # sélectionne 'fenêtre' pour recevoir les modifications des claviers

    fenetre.bind("<Button-1>", deplacementsouris) # l'évènement 'click souris gauche' renvoie à la fonction 'déplacementsouris'
    fenetre.bind('<Key>', deplacement)          # l'évènement 'pression sur une touche' renvoie à la fonction 'déplacement'


    fenetre.mainloop() # fait tourner la boucle d'affichage de l'interface en boucle, permet de maintenir la fenêtre de jeu affichée

## Jeu avec des chiffres

def affichage2(h):
    canvas.delete(ALL) # permet d'actualiser l'affichage de l'interface après chaque mouvement effectué
    i=0

    for k in range (4):
        canvas.create_line(k*200, 0, k*200, 800) #création des subdivisions de lignes verticales
        canvas.create_line(800, k*200, 0, k*200) #création des subdivisions de lignes horizontales
        j=0
        if k == 0:
            i += 100
        else:
            i += 200
        for m in range (4):
            if m == 0:
                j += 100
            else:
                j += 200
            if h[m][k] != 0:
                canvas.create_text(i,j,fill='black',text=str(h[m][k]),font=("arial",30,"bold"))

            canvas.pack()

def Jouer2():
    '''création d'une fonction qui affichera la fenêtre de jeu contenant le taquin
    La fonction a été créée pour être utilisée comme commande pour jouer avec les nombres'''

    global canvas, T
    global z # déterminer les différents modes de jeu
    z = 2
    T= Taquin_resolvable()
    root.destroy()
    fenetre=Tk()
    fenetre.title("TAQUIN")
    canvas = Canvas(fenetre, width=800, height=800, background='lightslategrey')

    affichage2(T)

    fenetre.focus_set()

    fenetre.bind("<Button-1>", deplacementsouris)
    fenetre.bind('<Key>', deplacement)


    fenetre.mainloop
bouton1=Button(root, text="Jouer avec des images",command=Jouer1,bg="#594949", fg="white", font="none 12 bold")
bouton1.place(relx = 0.2, rely=0.65)

bouton2=Button(root, text="Jouer avec des nombres",command=Jouer2,bg="#594949", fg="white", font="none 12 bold")
bouton2.place(relx = 0.6, rely=0.65)

# def Victoire():
#     if Taquin_fini_verifier(T) == True:
#         victoire()

# def victoire(): # A REVOIR
#     Victoire=TK
#     Victoire.config(width = 100, height = 100, bg='peachpuff2')
#     Texte1=Label(Victoire, text="Vous avez gagné !",bg="peachpuff2",fg="brown4",font="arial 32 bold")
#     Texte1.pack()
#
root.mainloop()



