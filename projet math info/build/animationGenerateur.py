import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import fractalesDeJulia
import fractalesDeMandelbrot
import math
#============================================================================
#                    Animation julia
#============================================================================
def generer_animation_fractale_julia_resolution(resolutionMax, couleur, xc, yc, nbFrames, saveOrShow):
    fig = plt.figure()
    ims = []
    
    pas = int(resolutionMax/nbFrames)
    for resolution in range(10, resolutionMax + 1, pas):
        print("Resolution:", resolution)
        mat = fractalesDeJulia.decoupagePlan(resolution, -2, -2, xc, yc)
        im = plt.imshow(mat, cmap=couleur, animated=True)
        ims.append([im])

    ani = animation.ArtistAnimation(fig, ims, interval=200, blit=True)

    if saveOrShow == 'save':
        ani.save('mandelbrot_animation.gif', fps=10)
    else:
        plt.show()

#=====================================================================
#                   Aniomation cercle de julia 
#=====================================================================

def generer_animation_cercle_Julia(complexe_depart, resolution, couleur, savOrShow):
    def anim_cercle_Julia(numImage):
        degre = numImage / 50 * 360
        reelC = complexe_depart * math.cos(math.radians(degre))
        imC = complexe_depart * math.sin(math.radians(degre))
        res = plt.imshow(fractalesDeJulia.decoupagePlan(resolution, -2, -2, reelC, imC), cmap=couleur)  
        return [res]
    
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, anim_cercle_Julia, frames=40, interval=1/50, blit=True)
    if savOrShow == 'save':
        ani.save('cercle_Julia_animation.gif', fps=10)
    else:
        plt.show()

#==========================================================
#               Animation de fractale de mandelbrot
#==========================================================

def generer_animation_fractale_multibrot(frames, resolution, couleur, saveOrShow):
    def anim_fractale_puissance(num_frame):
        incr_puissance = num_frame / frames * 4  
        mat = fractalesDeMandelbrot.decoupagePlan(resolution, -2, -2, incr_puissance)  
        im = plt.imshow(mat, cmap=couleur, animated=True)
        return [im]
    
    fig = plt.figure()
    ani = animation.FuncAnimation(fig, anim_fractale_puissance, frames=frames, interval=200, blit=True)
    
    if saveOrShow == 'save':
        ani.save('fractale_puissance_animation.gif', fps=10)
    else:
        plt.show()
