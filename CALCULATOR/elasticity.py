# -*- coding: utf-8 -*-
"""
Elasticity solutions calculator
Juan Vergara
Juan Gomez
"""
import numpy as np
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
def boussi(x,y,p):
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
    f3 = f1-f2
    f4 = (np.cos(2.0*phir)-np.cos(2.0*teta))/r/r
    if (r < 0.001):
        srp = 0.0
        trp = 0.0
    else:
        srp = (2*m/f3)*(np.sin(2.0*teta)/r/r)
        trp = (m/f3)*f4
    sigmar = srp
    sigmat = trp
    return sigmar , sigmat        
#
def prering(x , y , a , b , pa , pb ):
    r=(x**2.+y**2.)**0.5
    k1 = 1.0/((b**2)/(a**2)-1.0)
    k2 = 1.0/(1.0 - (a**2)/(b**2))
    f1 = (b**2)/(r**2) - 1.0 
    f2 = (b**2)/(r**2) + 1.0
    f3 = (a**2)/(r**2) + 1.0
    f4 = 1.0 - (a**2)/(r**2)
    srr = -k1*f1*pa-k2*f4*pb
    stt =  k1*f2*pa-k2*f3*pb
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