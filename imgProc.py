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
print(img*255)

# global size 
print(img.size)

# long 
print(img.shape[0])

# larg
print(img.shape[1])

# Taille
print(img.shape[0]*img.shape[1])

# Dimensions
print(img.shape)
