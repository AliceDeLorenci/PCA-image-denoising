import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
from skimage import io

def noise(im,br):
    """ Cette fonction ajoute un bruit blanc gaussier d'ecart type br
       a l'image im et renvoie le resultat"""
    imt=np.float32(im.copy())
    sh=imt.shape
    bruit=br*np.random.randn(*sh)
    imt=imt+bruit
    return imt
    
raw = io.imread('../masque_bas_centre.tif')
ima = np.ones( raw.shape ) + ( raw > 0 )*99

plt.figure( figsize=(8,8) )
plt.imshow( ima, cmap='gray' )
plt.axis('off')
plt.show()