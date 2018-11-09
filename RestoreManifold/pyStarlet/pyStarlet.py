import numpy as np
import starlet2d as st2

def Forward(X,J=2,h=[0.0625,0.25,0.375,0.25,0.0625]):

    lh = len(h)
    nX = np.shape(X)
    x = st2.Starlet2D(nX[1],nX[2],nX[0],J,lh).forward2d_omp(np.real(X),np.array(h))

    return x

def Backward(X):

    lh = 5
    nX = np.shape(X)
#    x = st2.Starlet2D(nX[1],nX[2],nX[0]-1,nX[3]-1,lh).backward2d_omp(X)
    x = st2.Starlet2D(nX[1] ,nX[2],nX[0],nX[3]-1,lh).backward2d_omp(X)
    return x

def Filter(X,J=2,th=0,L0=0):

    w = Forward(X,J=J)
    nW = np.shape(w)
    n_channels = nW[0]-1
    npix = nW[1]

    for r in range(J):
        c = w[n_channels,:,:,r]
        if L0:
            c = c*(c - th > 0)
        else:
            c = (c - th)*(c - th > 0)
        w[n_channels,:,:,r] = c

    return Backward(w)
