import math
from tkinter import *
from PIL import ImageTk, Image


MAX_ITER = 100 
LARGEUR = 500
HAUTEUR = LARGEUR 

PARTIE_REELLE_C = 0.285
PARTIE_IMAGINAIRE_C = 0.013

class App(Tk):
    def __init__(self):
        super().__init__()

        self.label = Label(self)
        self.label.pack()

        self.bind("-", lambda e: self.dezoom())
        self.bind("<BackSpace>", lambda e: self.retour_vue_precedente())
        self.bind('<Button-1>', lambda e: self.click(e.x, e.y))
        self.bind('<ButtonRelease-1>', lambda e: self.click_relache(e.x, e.y))

        self.xmin, self.ymin = -2, -2
        self.xmax, self.ymax = 2, 2
        
        self.genere_image()

    def affiche_image(self, pil_img):
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
    
    def retourne_contour_image(self):
        return (self.xmin, self.ymin), (self.xmax, self.ymax)


    def genere_image(self):
        image = creer_image_vide()
        pixels = image.load()
        (xmin, ymin), (xmax, ymax) = self.retourne_contour_image()
        
        for i in range(LARGEUR):
            for j in range(HAUTEUR):
                z_r = xmin + (xmax - xmin) * i / LARGEUR
                z_im = ymin + (ymax - ymin) * j / HAUTEUR
                borne = calcule_convergence(z_r,z_im)

                if borne == -1:
                    pixels[i,j]=(0,0,0)
                else:
                    pixels[i,j]=(255,255,255)
            self.affiche_image(image)

def creer_image_vide():
    return Image.new('RGB', (LARGEUR,HAUTEUR), "white")


def calcule_convergence(z_r, z_im):
    compteur=0
    divergence=False
    
    while not divergence:
          compteur += 1
          if module(z_r,z_im) > 2:
             divergence = True
             break
          elif compteur==MAX_ITER:
             break
          
          z_r,z_im = complexe_carre(z_r, z_im)
          z_r,z_im = z_r + PARTIE_REELLE_C, z_im + PARTIE_IMAGINAIRE_C

    if divergence:
       return(compteur)
    else:
       return(-1)


def complexe_carre(c_r, c_im):
    return ((c_r*c_r) - (c_im*c_im), 2*c_r*c_im)


def module(c_r, c_im):
    return math.sqrt(c_r*c_r + c_im*c_im)

if __name__ == "__main__":
    app = App()
    app.title('Fractales')
    app.mainloop()