
import matplotlib.pyplot as plt
import fractalesDeJulia

# on utilise la fonction estBornee de fractale de julia avec 
# des parametres particuliers pour avoir la fractale de mandelbrot
def decoupagePlan(resolution, ReelC, ImC,incr_puissance):
   pas = abs (2 * ReelC/ resolution)
   mat = [[0] * resolution  for _ in range(resolution)]
   pourcentage = 0
   for i in range(resolution):
      pourcentage = ((i+1) * 100)/resolution
      for j in range(resolution):
         mat[j][i]  = fractalesDeJulia.estBorneeAverage(0,complex(ReelC, ImC), incr_puissance)
         ImC += pas
      ReelC += pas
      ImC = -2 
   return mat


