# image-processing-python

import numpy as np
#Importation du module image
import matplotlib.image as mpimg
#Importation du module pyplot
import matplotlib.pyplot as plt
#Lecture d'une image au format png dans Python
img = mpimg.imread("Joconde.png")
#Affichage
plt.imshow(img)
#Sauvegarde sur disque
# plt.imsave ("Joconde.png ", image)

# liste de pixels
img*255
