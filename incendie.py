#########################################
# groupe MPCI 7
# Clement Coste
# Tom Le Goueff
# Yanis Kbayli
# Maeva Laurence
# https://github.com/uvsq-info/l1-python
#########################################

##import des modules##
import tkinter as tk
import random as rd

##constante##

COUL_FOND = "grey30"
COUL_QUARD = "grey60"
LARGEUR = 600
HAUTEUR = 600
COTE = 20

##fonction programme##
def quadrillage():
    y = 0
    while y <= HAUTEUR:
        canvas.create_line((0, y), (LARGEUR, y), fill= COUL_QUARD)
        y += COTE
    x = 0
    while x <= LARGEUR:
        canvas.create_line((x, 0), (x, HAUTEUR), fill= COUL_QUARD)
        x += COTE


##programme principale##

racine = tk.Tk()
canvas = tk.Canvas(racine, width = LARGEUR, height = HAUTEUR, bg = COUL_FOND)
racine.title("feu de foret")

#placement#

canvas.grid()

#fonction

quadrillage()

racine.mainloop()
