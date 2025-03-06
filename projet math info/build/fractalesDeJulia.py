import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as FunctionAnimation

#pour avoir la fractale de mandelbrot z = 0 et incr_puissance = 0
def estBorneeAverage(z, c, incr_puissance):
    # z et c sont des nombres complexes
    borne = 100
    rang = 0
    while rang < borne:
        z = z**(2 + incr_puissance) + c
        if abs(z) > 2:
            return 100 - rang
        rang += 1
    return 100

def decoupagePlan(resolution, reelZ0,imZ0, xC, yC):
    #pour avoir une image de taille moyenne imZ = -2 et reelz = -2
    # pour eveter une resolution de 0 pixel
    if resolution == 0 :
        resolution = 50
        
    taille_Pixel = abs(2 * imZ0 / resolution)
    mat = np.zeros((resolution, resolution), dtype=int)
    for i in range(resolution):
        for j in range(resolution):
            mat[i,j] = estBorneeAverage(complex(reelZ0, imZ0), complex(xC, yC), 0)
            imZ0 += taille_Pixel
        reelZ0 += taille_Pixel
        imZ0 = -2
    return mat




