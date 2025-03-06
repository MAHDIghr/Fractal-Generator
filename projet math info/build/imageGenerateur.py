import fractalesDeJulia
import fractalesDeMandelbrot

from matplotlib import pyplot as plt

# Fonctions unitaires utiles pour les deux types de fractales
def sauvgarder_et_afficher_fractale(saveOrShow) : 
    if (saveOrShow == 'save') :
        plt.savefig('fractale_de_julia.png')
    else :
        plt.show()

#========== FRACTALES DE JULIA===========================================

def generer_fractale_de_julia(resolution, xC, yC, saveOrShow, couleur):
    reelZ0 = -2
    imZ0 = -2
    matrice_fractale = fractalesDeJulia.decoupagePlan(resolution, reelZ0, imZ0, xC, yC)
    # Afficher la fractale de Julia
    plt.imshow(matrice_fractale, cmap=couleur, extent=(-2, 2, -2, 2))
    plt.title('Fractale de Julia')
    sauvgarder_et_afficher_fractale(saveOrShow)

#==========FRACTALES DE MANDELBROT=========================================

def generer_fractale_de_mandelbrot(resolution, saveOrShow, couleur):
    reelZ0 = -2
    imZ0 = -2
    matrice_fractale = fractalesDeMandelbrot.decoupagePlan(resolution, reelZ0, imZ0, 0)
    # Afficher la fractale de mandelbrot
    plt.imshow(matrice_fractale, cmap=couleur, extent=(-2, 2, -2, 2))
    plt.title('Fractale de Mandelbrot')
    sauvgarder_et_afficher_fractale(saveOrShow)
    

    

