import math

from tkinter import *
from PIL import ImageTk, Image


MAX_ITER = 100 # maximum d'iteration avant de decider que la suite des zn ne diverge pas
LARGEUR = 500
HAUTEUR = LARGEUR # on force l'image à être carrée

# les valeurs de du nombre complexe c pour la suite zn+1 = zn^2 + c
PARTIE_REELLE_C = 0.3
PARTIE_IMAGINAIRE_C = 0.5

class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        self.bind("-", lambda e: self.dezoom())
        self.bind("<BackSpace>", lambda e: self.retour_vue_precedente())
        self.bind('<Button-1>', lambda e: self.click(e.x, e.y))
        self.bind('<ButtonRelease-1>', lambda e: self.click_relache(e.x, e.y))

        # gestion des coordonnées pour l'image
        # au depart on trace l'image de cote [-2, 2]
        self.xmin, self.ymin = -2, -2
        self.xmax, self.ymax = 2, 2

        # vous pouvez ajouter des attributes pour gérer le zoom dans un rectangle

    def affiche_image(self, pil_img):
        """affiche l'image donnée dans tkinter"""
        tk_img = ImageTk.PhotoImage(pil_img)
        self.label.configure(image=tk_img)
        self.label.image = tk_img

    def dezoom(self):
        print("-") # a modifier

    def click(self, x, y):
        print("click", x, y) # a modifier

    def click_relache(self, x, y):
        print("relache", x, y) # a modifier

    def retour_vue_precedente(self):
        print("retour") # a modifier

    def retourne_contour_image(self):
        """Retourne le contour de l'image dans le plan complexe pour generer l'image"""
        return (self.xmin, self.ymin), (self.xmax, self.ymax)

    def genere_image(self):
        image = creer_image_vide()
        pixels = image.load()
        (xmin, ymin), (xmax, ymax) = self.retourne_contour_image()
        self.affiche_image(image)
        for i in range(LARGEUR):
            for j in range(LARGEUR):
                z_r = xmin + (i / LARGEUR) * (xmax - xmin)
                z_im = ymin + (j / HAUTEUR) * (ymax - ymin)
                borne=calcule_convergence(z_r,z_im)

                if borne!=-1:
                    pixels[i,j]=(0,0,0) #255,255,255
                else:
                    pixels[i,j]=(255,255,255) #test c'est 0,0,0
        # produit en croix -2 et 2 avec 500 et -500
        # z= x + iy
        # si -1 pixel noir sinon pixel blanc
        # parcours de tous les pixels
        # pour chaque pixel on calcul le z dans le plan complexe correspondant
        # on regarde la convergence de la suite et on decide de la couleur a afficher

        # REMARQUE : pour modifier un pixel dans l'image on fait
        # pixels[i,j] = (0, 0 ,0)
        # 0 pour noir 255 pour blanc et entre les deux pour le niveau de gris et la couleur

        

def creer_image_vide():
    return Image.new('RGB', (LARGEUR,HAUTEUR), "white") # cree une image blanche

def calcule_convergence(z_r, z_im): #calcule borné
    compteur=0
    divergence=False
    while divergence!=True:
          compteur+=1
          if compteur==MAX_ITER:
             break
          if module(z_r,z_im)>=2:
             divergence=True
    for i in range(compteur):
        z_r,z_im=complexe_carre(z_r,z_im)
        z_r,z_im=z_r+ PARTIE_REELLE_C, z_im + PARTIE_IMAGINAIRE_C
    if divergence==True:
       return(compteur)
    else:
         return(-1)
    # calcule le nombre d'iteration necessaire pour diverger
    # on prend comme critere de divergence si le module depasse 2
    # si la suite converge la fonction retourne -1


def complexe_carre(z_r, z_im): #c_r c_im # calcule le carre d'un nombre complexe en retournant sa partie reelle et imaginaire
    return z_r**2-z_r**2, 2*z_r*z_im

def module(z_r, z_im):
    return(math.sqrt(z_r**2+z_im**2))

if __name__ == "__main__":
    app = App()
    app.title('Fractales')
    app.genere_image()

    app.mainloop()