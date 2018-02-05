"""
Description missing.
"""
from __future__ import division, print_function
import numpy as np
import matplotlib.pyplot as plt


def Ftrans(datos, ndats, dt, fs):
    """
    Compute the Fourier spectra of datos[] and
    returns the result in SaS after smoothing by the
    smootinh factor fs.
    """
    nfr = int(ndats/2)
    df = 1.0/(ndats*dt)
    x = np.arange(df,nfr*df, df)
    A = np.fft.fft(datos)
    Aa = np.abs(A)

    # Smooth the spectrum.
    Sa = Aa[1:nfr]
    Samag = smooth(Sa , x , fs)
    Samag = Samag/ndats
    nfs = nfr-1
    return x, Samag , A , nfs


def IFtrans(datos , ndats , dt):
    """
    Integrate an acceleration history into a velocity history
    proceeding in the frequency domain.
    """
    B = np.fft.ifft(datos)
    return np.real(B)


def smooth(Sa, Freq, fftfs):
    """
    Parameters
    ----------
    Sa : ndarray
        Original spectrum.
    Freq : float
        Frequency.
    fftfs : float
        Smoothing factor.
    """
    Sas  = np.zeros([len(Sa)],dtype=float)
    fia = 1
    fma = 1
    suma = Sa[0] * Sa[0]
    pot = 1./2./fftfs
    fsexpi = 2**(-pot)
    fsexpm = 2**( pot)
    Sas[0] = Sa[0]
    NNfft = len(Sa)
    for i in range(1, NNfft):
    # #    for i=2:NNfft
        fi = int((i + 1) * fsexpi)
        fm = int((i + 1) * fsexpm)
        if fi < 1:
            fi = 1
        if fm > NNfft:
            fm = NNfft

        for Num in range(fia - 1, fi - 1):
        #         #for j=fia:fi-1:
            suma = suma - Sa[Num] * Sa[Num]

        for Num in range(fma, fm):
        #         #for j=fma+1:fm:
            suma = suma + Sa[Num]*Sa[Num]

        Nf = fm - fi + 1
        fia = fi
        fma = fm
        Sas[i]=np.sqrt(suma/Nf)
    return (Sas)


def ricker(nt, Tt, tc, fc):
     time = np.linspace(0, Tt, nt)
     tau = np.pi*fc*(time - tc)
     Rick = (2.0*tau**2 - 1.0) * np.exp(-tau**2)
     return Rick, time


def grafsignalG(A, var1, label1, units, ymin, ymax, dt, Ngra):
    """
     Plots the generalized time signal A[ndats] into Ngra
     The plot is also stored into var.pdf
    """
    ndats  = len(A)
    x=np.zeros([ndats], dtype=float)
    x=np.arange(0,ndats*dt,dt)
    var1=var1 + '.pdf'
    plt.figure(Ngra)
    plt.plot(x,A)
    plt.grid()
    plt.xlabel('Tiempo (s)' + str(Ngra))
    plt.ylabel(label1 + ' ' + units)
#    plt.ylim(ymin,ymax)
    plt.savefig(var1)
#
    return

def grafFourier(Sas , x , nfr , var, xmin , xmax , ymin , ymax , Nfig):
    """
     Plots the Fourier spectral amplitude Sas into Nfig.
     Sas : Spectrum
     x   : frecuency
     xmin,xmax,ymin,ymax
    """
#    path = '../RESULTADOS/'
    plt.figure(Nfig)
    plt.plot(x,Sas)
    var1= var + '.pdf'
    plt.grid()
    plt.xlabel('Frecuencia (Hz)')
    plt.ylabel('Amplitud')
    #plt.legend(['Fourier spectral amplitude'])
    plt.xlim(xmin,xmax); plt.ylim(ymin,ymax)
#    plt.xscale('log')
#    plt.yscale('log')
    plt.savefig(var1)
#
    return