import numpy as np
import matplotlib.pyplot as plt
import skimage as sk
from skimage import io
from sklearn.preprocessing import label_binarize


# i: linha
# j: coluna

def error( x, x0, m, s ):
    e = np.sum( x0 - x**2 + 2*(s**2) )/m
    return e

def LPG( ima, i0, j0, s, L=41, K=5, c=8, T=25 ):

    x0 = ima[i0-K//2:i0+(K//2)+1+1, j0-K//2:j0+(K//2)+1+1].reshape(-1,1)

    m = K**2
    max_n = (L-K+1)**2

    # print('L:[{},{}]'.format( i0-L//2, i0+L//2 ) ) 

    lbi = max(0, i0-L//2)
    ubi = min( ima.shape[0]-K+1, i0+L//2-K+1)

    lbj = max(0, j0-L//2)
    ubj = min( ima.shape[1]-K+1, j0+L//2-K+1)

    Xv = np.array( (m, max_n ) )
    E = np.array( max_n )

    # print(lbi, ' ', ubi)
    for i in range( lbi, ubi+1 ):
        for j in range( lbj, ubj+1 ):

            x = ima[i:i+K, j:j+K].reshape(-1,1)
            Xv[:,i*j] = x
            E[i*j] = error( x, x0, m, s )



        # print( '[{},{}]'.format(i, i+K-1) )

ima = np.random.randint( 0, 50, size=(10,10) )
print( ima )
LPG( ima, 3, 0, -1, L=5, K=3 )