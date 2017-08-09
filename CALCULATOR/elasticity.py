# -*- coding: utf-8 -*-
"""
Elasticity solutions calculator
Juan Vergara
Juan Gomez
"""
#
import scipy.special as sci
import numpy as np
import signals as sig
#
def myfunction(x,y,p):
    """
    Template for user defined elasticity solution.
    """
    ux=(x**2.+y**2.)**p
    return ux
#
def cunia(x,y,phi,l,nu,E,S):
    """Computes the solution for self-equilibated wedge
       at a point (x , y)

    Parameters
    ----------
    nu  :float, (-1, 0.5)
         Poisson coefficient.
    S   :float
         Applied shear traction over the faces of the wedge.
    E   :float, >0
         Young modulus.
    l   :float, >0
         Length of the inclined face of the wedge.
    phi :float, >0
         Half-angle of the wedge.

    Returns
    -------
    ux : float
         Horizontal displacement at (x , y).
    uy : float
         Vertical displacement at (x , y).       
    References
    ----------
    .. [1] Timoshenko, S. & Goodier, J., 1970. Theory of Elasticity,
        McGraw-Hill, 3rd Ed.

    """
#
    K1=(np.cos(phi)/np.sin(phi))+nu*(np.sin(phi)/np.cos(phi))
    K2=(np.sin(phi)/np.cos(phi))+nu*(np.cos(phi)/np.sin(phi))
    ux=(S/E)*K1*(x-l*np.cos(phi))
    uy=-(S/E)*K2*y
    sigx = S*(np.cos(phi)/np.sin(phi))
    sigy =-S*(np.sin(phi)/np.cos(phi))
    return ux , uy , sigx , sigy 
#
def beam(x, y, nu, P, E, I, L, h):
    """Compute the solution for a cantilever beam

    Parameters
    ----------
    x : ndarray (float)
        Array with x coordinates.
    y : ndarray (float)
        Array with y coordinates.
    nu : float, (-1, 0.5)
        Poisson coefficient.
    P : float
        Applied force at the end of the beam.
    E : float, >0
        Young modulus.
    I : float, >0
        Moment of inertia.
    L : float, >0
        Length of the beam.
    h : float, >0
        Height of the beam.

    Returns
    -------
    u : ndarray (float)
        Horizontal displacement at the nodes.
    v : ndarray (float)
        Vertical displacement at the nodes.
    exx : ndarray (float)
        xx component of the strain tensor.
    eyy : ndarray (float)
        yy component of the strain tensor.
    gammaxy : ndarray (float)
        xy component of the strain tensor.
        
    References
    ----------
    .. [1] Timoshenko, S. & Goodier, J., 1970. Theory of Elasticity,
        McGraw-Hill, 3rd Ed.

    """
    G = E/(2*(1 + nu))
    c = h/2
    C1 = -P/(2*E*I)
    C2 = -(nu*P)/(6*E*I)
    C3 = P/(2*I*G)
    C4 = (P*L**2)/(2*E*I)
    C5 = -(P*c**2)/(2*I*G)
    C6 = C4 + C5
    C7 = (nu*P)/(2*E*I)
    C8 = P/(6*E*I)
    C9 = -(P*L**2)/(2*E*I)
    C10 = (P*L**3)/(3*E*I)
    B1 = -P/(E*I)
    B2 = (nu*P)/(E*I)
    B3 = P/(2*I*G)
    u = C1*y*x**2 + C2*y**3 + C3*y**3 + (C5 + C6)*y
    v = C7*x*y**2 + C8*x**3 + C9*x + C10
    exx = B1*x*y
    eyy = B2*x*y
    gammaxy = B3*(y**2 - c**2)

    return u, v, exx, eyy, gammaxy        
#
def boussipol(x,y,p):
    r=(x**2.+y**2.)**0.5
    teta = np.arcsin(y/r)
    Pi = np.pi
    if (r < 0.00001):
        srp = 0.0
    else:
        srp = (-2*p/Pi)*(np.cos(teta)/r)
    sigma = srp
    return sigma
#
def boussicar(x,y,p):
    r=(x**2.+y**2.)**0.5
    teta = np.arcsin(y/r)
    Pi = np.pi
    if (r < 0.00001):
        Sxx = 0.0
        Syy = 0.0
        Txy = 0.0
    else:
        Sxx = (-2*p/Pi/r)*(np.cos(teta))**3
        Syy = (-2*p/Pi/r)*(np.cos(teta)*(np.sin(teta)**2))
        Txy = (-2*p/Pi/r)*(np.sin(teta)*(np.cos(teta)**2)) 
    return Sxx , Syy , Txy    
#
def boussidis(x , y , p , E , enu , d):
    r=(x**2.+y**2.)**0.5
    teta = np.arcsin(y/r)
    Pi = np.pi
    omnu = 1.0 - enu
    if (r < 0.00001):
        ur = 0.0 
        ut = 0.0
    else:
        ur = (-2*p/Pi/E)*(np.cos(teta)*np.log(r))-(omnu*p/Pi/E)*(teta*np.sin(teta))+(2*p/Pi/E)*(np.cos(teta)*np.log(d))
        ut = ( 2*enu*p/Pi/E)*(np.sin(teta)) + (2*p/Pi/E)*(np.sin(teta)*np.log(r))-(omnu*p/Pi/E)*(teta*np.cos(teta))+(omnu*p/Pi/E)*(np.sin(teta))-(2*p/Pi/E)*(np.sin(teta)*np.log(d))
    return ur , ut   
#
def flamantP(x , y , p , phi):
    r=(x**2.+y**2.)**0.5
    teta = np.arcsin(y/r)
    phir = radianes(phi)
    f1 = 2*phir
    f2 = np.sin(phir)
    f3 = f1+f2
    if (r < 0.001):
        srp = 0.0
    else:
        srp = (-2*p/f3)*(np.cos(teta)/r)
    sigma = srp
    return sigma    
#
def flamantQ(x , y , q , phi):
    r=(x**2.+y**2.)**0.5
    teta = np.arcsin(y/r)
    phir = radianes(phi)
    f1 = 2*phir
    f2 = np.sin(phir)
    f3 = f1-f2
    if (r < 0.001):
        srp = 0.0
    else:
        srp = (-2*q/f3)*(np.sin(teta)/r)
    sigma = srp
    return sigma    
#
def flamantM(x , y , m , phi):
    r=(x**2.+y**2.)**0.5
    teta = np.arcsin(y/r)
    phir = radianes(phi)
    f1 = np.sin(2*phir) 
    f2 = (2.0*phir)*np.cos(2.0*phir)
    f3 = (f1-f2)*r*r
    f4 = (np.cos(2.0*phir)-np.cos(2.0*teta))
    if (r > 0.1):
        srp = (2*m/f3)*(np.sin(2.0*teta))
        trp = (m/f3)*f4
    else:
        srp = 0.0
        trp = 0.0
    sigmar = srp
    taor   = trp
    return sigmar , taor        
#
def prering(x , y , a , b , pa , pb ):
    r=(x**2.+y**2.)**0.5
    k1 = ((a**2)*(b**2)/(b**2-a**2))*(pb-pa)
    k2 = (pa*a*a-pb*b*b)/(b**2-a**2)
    srr =  k1/(r**2)+k2
    stt = -k1/(r**2)+k2
    sigmar = srr
    sigmat = stt
    return sigmar , sigmat    
#
def radianes(ang_grad):
    ang_rad=ang_grad*np.pi/180    
    return ang_rad      
    
def grados(ang_rad):
    ang_grad=ang_rad*180/np.pi    
    return ang_grad      
#    
def tensor_polar(r,teta,f,beta,alfa):
    
    alfa=radianes(alfa) # para semi-espacio
    teta=radianes(teta) # paso teta a radianes
    beta=radianes(beta) # paso beta a radianes
    p=f*np.sin(beta)
    q=f*np.cos(beta)
    srp=-2.*p*np.cos(teta)/((2.*alfa+np.sin(2.*alfa))*r)
    srq=-2.*q*np.sin(teta)/((2.*alfa-np.sin(2.*alfa))*r)
    sigma=np.zeros((2,2))
    sigma[0,0]=srp+srq
    return sigma  
    
def tensor_cart(r,teta,f,beta):
    #################################### variables de entrada ####################
    # r=...........................radio (coordenada polar)
    # teta=........................Angulo en grados (coordenada polar)
    # f=...........................Fuerza ()
    # beta=....................... Angulo de la Fuerza en grados
    ##############################################################################
    teta=radianes(teta) # paso teta a radianes
    beta=radianes(beta) # paso beta a radianes
    #
    p=f*np.sin(beta)
    q=-f*np.cos(beta)
   
    sxp=-2.*p*np.cos(teta)**3./(np.pi*r)
    syp=-2.*p*np.cos(teta)*np.sin(teta)**2./(np.pi*r)
    txyp=-2.*p*np.cos(teta)**2.*np.sin(teta)/(np.pi*r)
    
    sxq=2.*q*np.cos(teta)**2.*np.sin(teta)/(np.pi*r)
    syq=2.*q*np.sin(teta)**3./(np.pi*r)
    txyq=2.*q*np.sin(teta)**2.*np.cos(teta)/(np.pi*r)
    #
    sigmaf=np.zeros((2,2))
    sigmaf[0,0]=sxp+sxq
    sigmaf[1,1]=syp+syq
    sigmaf[0,1]=txyp+txyq
    sigmaf[1,0]=txyp+txyq    
    return sigmaf       
    
def tensor_cart_m(r,teta,f,m,beta):    
    teta=radianes(teta) # paso teta a radianes
    beta=radianes(beta) # paso beta a radianes
    #
    p=f*np.sin(beta)
    q=-f*np.cos(beta)
# Carga Vertical   
    sxp=-2.*p*np.cos(teta)**3./(np.pi*r)
    syp=-2.*p*np.cos(teta)*np.sin(teta)**2./(np.pi*r)
    txyp=-2.*p*np.cos(teta)**2.*np.sin(teta)/(np.pi*r)
# CArga Horizontal   
    sxq=2.*q*np.cos(teta)**2.*np.sin(teta)/(np.pi*r)
    syq=2.*q*np.sin(teta)**3./(np.pi*r)
    txyq=2.*q*np.sin(teta)**2.*np.cos(teta)/(np.pi*r)
# Momento
    sxm=np.cos(teta)**3.*np.sin(teta)*(8.*m/(np.pi*r**2.))
    sym=np.cos(2.*teta)*np.sin(2.*teta)*(-2.*m/(np.pi*r**2.))
    txym=(3.*np.sin(teta)**2.*np.cos(teta)**2.-np.cos(teta)**4.)*(2.*m/(np.pi*r**2.))
# Tensor solución       
    sigmaf=np.zeros((2,2))
    sigmaf[0,0]=sxp+sxq+sxm
    sigmaf[1,1]=syp+syq+sym
    sigmaf[0,1]=txyp+txyq+txym
    sigmaf[1,0]=txyp+txyq+txym    
    return sigmaf   
#
def trifunac(x, y , Gamma , a):
    """
     Author: Juan Fernando Zapata
     Writes VTK files for visualization with paraview
    """
    
        ##################### DEFINICIÓN DE LOS VECTORES CON LOS TÉRMINOS DE HANKEL Y BESSEL ######################
        
    def Especiales(Delta, f): # El parámetro f define cuál de los 4 vectores voy a retornar
        sumatoria = 130 #Número de veces que se van a evaluar las sumatorias de Hankekl
        H = np.zeros((sumatoria), dtype = complex)  # Vector Hankel
        B = np.zeros((sumatoria)) # Vector Bessel 
        
        if f == 0:
            for i in range (0, sumatoria):        
                H[i] = sci.hankel2(i, Delta)
            return(H)
        else: 
            for i in range (0, sumatoria):
                B[i] = sci.jv(i, Delta)
            return(B)
                
        #############################################################################################################
    Beta = 1.0 # Velocidad de la onda incidente en el medio
#    Gamma = 0.523 # Ángulo de incidencia de la onda
#    a = 1.0 # Radio del cañón
    
    Tt = 16.0 #Tiempo total que tendrá el pulso
    Tc = 4.0 # Tiempo en el que estará centrado el pulso
    fc = 1.0 # Frecuencia del pulso
    Nf= 2048
    Nt= 2*Nf+1
    dt = Tt/(Nt-1)
    deta = 2.0*a/Beta/Tt # Delta de frecuencias
    neta  = int(4*fc*2/deta) # Número de frecuencias que se evaluaran
    
    lieta = deta # #Límite inferior para eta
    lfeta = deta*neta # Límite superior para x
    Eta = np.linspace(lieta, lfeta, neta, dtype=float)
    
    desplaz = np.zeros(len(Eta), dtype=complex)
    suma = 64
    
    
    if (y == 0):
            
        r = abs(x)
            
        if (x < 0):
                
            tetha = - np.pi/2.0
        else:
                
            tetha = np.pi/2.0
                
    elif (x == 0):
            
        r = y
        tetha = 0.0
            
    else:
        
        r = np.sqrt((x)**2 + (y)**2)
        tetha = np.arctan(x / y)
        
        
    for j in range (0, len(Eta)): # Variación de frecuencias para cada X
    
        kappa = (np.pi / a) * Eta[j]
        ka = kappa * a
        kr = kappa * r
        Hankel = Especiales(kr, 0) #Vector de Hankel con argumento kr
        Bessel = Especiales(kr, 1) # Vector de Bessel con argumento kr
        
        ######################################### CÁLCULO DEL INCOMING ###########################################         
        S1 = 0 # Acumulador de la primera sumatoria del incoming
        S2 = 0 #Acumulador de la segunda sumatoria del incoming
                
        for i in range (0,suma): #Términos de la sumatoria
            n1 = i+1
            S1 = S1 + ((-1)**n1 * Bessel[2*n1] * np.cos(2*n1*Gamma) * np.cos(2*n1*tetha))
            S2 = S2 + ((-1)**i * Bessel[2*i+1] * np.sin((2*i+1)*Gamma) * np.sin((2*i+1)*tetha))
                
        incoming = (2.0 * Bessel[0]) + (4.0 * S1) - (4j * S2) 
            
        ##############################################   CÁLCULO DEL SCATTER #############################################
                
        Hanka = Especiales(ka, 0) # Vector de hankel con argumento ka
        Beka = Especiales(ka, 1) # Vector de Bessel con argumento ka
        A0 = -2.0 * (Beka[1] / Hanka[1])
        B0 = 4j * np.sin(Gamma) * ((ka*Beka[0] - Beka[1]) / (ka*Hanka[0] - Hanka[1]))
                
        scatter = 0
                
        for i in range(0, suma):
            if i == 0:
                scatter = scatter + ( A0*Hankel[2*i]*np.cos(2*i*tetha) + B0*Hankel[2*i+1]*np.sin((2*i+1)*tetha) )
            else:
                    
                An = -4 * (-1)**i * np.cos(2*i*Gamma) * ((ka*Beka[2*i-1] - 2*i*Beka[2*i]) / 
                    (ka*Hanka[2*i-1] - (2*i)*Hanka[2*i])) 
                        
                Bn = 4j * ((-1)**i) * np.sin((2*i+1)*Gamma) * ((ka*Beka[2*i] - (2*i+1)*Beka[2*i+1]) / 
                    (ka*Hanka[2*i] - (2*i+1)*Hanka[2*i+1]))
                        
                scatter = scatter + ( An*Hankel[2*i]*np.cos(2*i*tetha) + Bn*Hankel[2*i+1]*np.sin((2*i+1)*tetha) )
                
        desplaz[j] = incoming + scatter
        
    #return(desplaz) #Tener en cuenta el lugar del return
    
    Rick, T= sig.ricker(Nt, Tt, Tc, fc)
    x , Sas , Saf , nfs = sig.Ftrans(Rick , Nt , dt , 10.0)
    
    TF = np.zeros(Nt, dtype=complex)
    for i in range(neta):
        
        TF[i+1] = desplaz[i]
        TF[-1-i] = np.conj(desplaz[i])
    
    for i in range(Nt):
        
        TF[i] = Saf[i] * TF[i]
        
    signal = sig.IFtrans(TF , Nt , dt)
    
    return(signal)

def dam(x,y,gamma):
    """Computes the solution for self-equilibated wedge
       at a point (x , y)

    Parameters
    ----------
    nu  :float, (-1, 0.5)
         Poisson coefficient.
    S   :float
         Applied shear traction over the faces of the wedge.
    E   :float, >0
         Young modulus.
    l   :float, >0
         Length of the inclined face of the wedge.
    phi :float, >0
         Half-angle of the wedge.

    Returns
    -------
    ux : float
         Horizontal displacement at (x , y).
    uy : float
         Vertical displacement at (x , y).       
    References
    ----------
    .. [1] Timoshenko, S. & Goodier, J., 1970. Theory of Elasticity,
        McGraw-Hill, 3rd Ed.

    """
#
    sigx =  gamma*x-2.0*gamma*y
    sigy = -gamma*x
    tao  = -gamma*y
    return sigx , sigy , tao
    
    
def DifractionSesma(x,y):
    
    Ui = 1j
    v = 3/2

    r0 = 10
    phi0 = 20*np.pi/180    
    
    r = np.sqrt((x)**2 + (y)**2)
    phi = np.arctan(x / y)
    
    R=[r,r0]   
    
    Beta = 1.0 # Velocidad de la onda incidente en el medio
    
    Tt = 16.0 #Tiempo total que tendrá el pulso
    Tc = 4.0 # Tiempo en el que estará centrado el pulso
    fc = 1.0 # Frecuencia del pulso
    Nf= 2048
    Nt= 2*Nf+1
    dt = Tt/(Nt-1)
    deta = 2.0/Beta/Tt # Delta de frecuencias
    neta  = int(4*fc*2/deta) # Número de frecuencias que se evaluaran
    
    lieta = deta # #Límite inferior para eta
    lfeta = deta*neta # Límite superior para x
    Eta = np.linspace(lieta, lfeta, neta, dtype=float)
    
    W = np.zeros(len(Eta), dtype=complex)

    Vdt =np.zeros(Nt)
                
    for i in range(Nt):
         Vdt[i] = i*dt    
    
    
    
    def Especiales(Delta, f): # El parámetro f define cuál de los vectores voy a retornar
        
        sumatoria = 100 #Número de veces que se van a evaluar las sumatorias de Hankel
        
        H = np.zeros((sumatoria), dtype = complex)  # Vector Hankel
        B = np.zeros((sumatoria)) # Vector Bessel 
        
        if f == 0:
            for i in range (0, sumatoria):        
                H[i] = sci.hankel1(i, Delta)
            return(H)
        else: 
            for i in range (0, sumatoria):
                B[i] = sci.jv(i, Delta)
            return(B)
    
    for j in range (0, len(Eta)):
       
        k = Eta[j]/Beta
        
        r = min(R)        
        bessel = Especiales(k*r,1)
        
        r = max(R)
        hankel = Especiales(k*r,0)
        
        S = hankel*bessel
        
        wii = 0
        n = 100

        for i in range (n):
            
            En = 0
            
            if i==0:
                En = 1
            else:
                En = 2
            
            wi = (Ui/(2*v))*En*np.cos((i/v)*(phi + v*np.pi*0.5))*np.cos((i/v)*(phi0 + v*np.pi*0.5))*S[i/v]
            
            wii = wii + wi
            
            
        W[j] = wii
        

    Rick, T= sig.ricker(Nt, Tt, Tc, fc)
    x , Sas , Saf , nfs = sig.Ftrans(Rick , Nt , dt , 10.0)
    
    TF = np.zeros(Nt, dtype=complex)
    for i in range(neta):
        
        TF[i+1] = W[i]
        TF[-1-i] = np.conj(W[i])
    
    for i in range(Nt):
        
        TF[i] = Saf[i] * TF[i]
        
        
    signal = sig.IFtrans(TF , Nt , dt)
    
    return(signal)


def single_ray(x, y , Gamma , Beta , Nt , Tt , Tc , fc):
    """Evaluates a plane wave

    Parameters
    ----------
    x : float
        x-coordinate
    y : float
        y-coordinate
    Gamma: float
        Angle of incidence
    Beta: float
        Velocity of wave propagation

    Returns
    -------
    signal : ndarray (float)
        Array with the time history at the point x-y.

    """                    
#
# Pulse parameters
#
    dt = 1.0/(8.0*fc)
    Nf =int((Nt - 1)/2) 
    df = 1/(Nt*dt)
    neta = Nf
    
    lif = df # #Límite inferior para eta
    lff = df*neta # Límite superior para x
    fre = np.linspace(lif, lff, neta, dtype=float)
    
    desplaz = np.zeros(len(fre), dtype=complex)
#
    nx = np.sin(Gamma)
    ny =-np.cos(Gamma) 
#
#   Compute the Transfer function
#            
    for j in range (0, len(fre)):
        kapa = 2.0*np.pi*fre[j]/Beta        
        pha_ang = - kapa*(nx*x + ny*y) 
        desplaz[j] = np.exp(1j*pha_ang)
#
#   Compute convolution and inverse transform.
#  
    TF = np.zeros(Nt , dtype=complex)
    Rick , T = sig.ricker(Nt , Tt , Tc , fc)
    x , Sas , Saf , nfs = sig.Ftrans(Rick , Nt , dt , 10.0)
    
    for i in range(neta):        
        TF[i+1] = desplaz[i]
        TF[-1-i] = np.conj(desplaz[i])
    
    for i in range(Nt):
        
        TF[i] = Saf[i] * TF[i]
        
    signal = sig.IFtrans(TF , Nt , dt)
    
    return(signal)
