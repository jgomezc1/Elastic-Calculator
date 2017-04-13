#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 10 12:10:08 2017

@author: casierraa
"""
from os import sys
sys.path.append('../CALCULATOR/')
from sympy import init_printing
init_printing()


def mesh_gui():
    try:
        import easygui
        msg = "General Discretization Parameters"
        title = "Mesh parameters"
        fieldNames = ["Element size","Element type (2: lin.triang.; 3 quad4; 9.quad.triang.)","Intrpolation order"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
    
        c = float(fieldValues[0])
        ietype = int(fieldValues[1])
        order = int(fieldValues[2])
    except:
        c1 = raw_input("Element size")
        ietype1 = raw_input("Element type")
        order1 = raw_input("Interpolation order")
        c = float(c1)
        ietype = int(ietype1)
        order = int(order1)
    
    return c, ietype , order

def ring_prs():
    try:
        import easygui
        msg = "Cylinder under internal pressure"
        title = "Problem parameters"
        fieldNames = ["Internal radius","External radius","Internal pressure","External pressure"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

        a = float(fieldValues[0])
        b = float(fieldValues[1])
        pa = float(fieldValues[2])
        pb = float(fieldValues[3])
    except:
        a1 = raw_input("Internal radius")
        b1 = raw_input("Eternal radius")
        c1 = raw_input("Internal pressure")
        d1 = raw_input("xternal pressure")
        a  = float(a1)
        b  = float(b1)
        pa = float(c1)
        pb = float(d1)
    
    return a , b , pa , pb

def ring_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Cylinder under internal and external pressure", 
        ok_button="Continuar",
        image='anillo.gif')
    except:
        print ("No easygui module")
    
    return



def wedge_prs():
    
    
    try:
        import easygui
        msg = "Self equilibrated wedge"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length", "Poissons ratio" , "Youngs modulus" , "External shear"]
        fieldValues = []  
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
        
    
        phid = float(fieldValues[0])
        l = float(fieldValues[1])
        enu = float(fieldValues[2])
        emod = float(fieldValues[3])
        S = float(fieldValues[4])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Poissons ratio")
        d1 =raw_input("Youngs modulus")
        e1 = raw_input("External shear")
        phid = float(a1)
        l = float(b1)
        enu = float(c1)
        emod = float(d1)
        S = float(e1)
        
    return phid , l , enu , emod , S

def wedge_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Self-equilibrated wedge", 
        ok_button="Continuar",
        image='cunia.gif')
    except:
        print ("No easygui module")
    
    return

def beam_prs():
    
    try:
        import easygui
        msg = "Cantilever beam (Timoshenko Sln)"
        title = "Enter the problem parameters"
        fieldNames = ["Length","Height","Inertia","Poissons ratio","Young modulus", "Load"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
        
    
        L  = float(fieldValues[0])
        h  = float(fieldValues[1])
        I  = float(fieldValues[2])
        nu = float(fieldValues[3])
        E  = float(fieldValues[4])
        P  = float(fieldValues[5])
    except:
        a1 = raw_input("Length")
        b1 = raw_input("Height")
        c1 = raw_input("Inertia")
        d1 = raw_input("Poissons ratio")
        e1 = raw_input("Youngs modulus")
        f1 = raw_input("Load")
        L = float(a1)
        h = float(b1)
        I = float(c1)
        nu = float(d1)
        E = float(e1)
        P = float(f1)
            
    return L , h , I , nu , E , P

def beam_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Cantilever beam under point load (Timoshnko sln)", 
        ok_button="Continuar",
        image='viga.gif')
    except:
        print ("No easygui module")
    
    return


def boussi_prs():
    try:
        import easygui
        msg = "Half-space under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Length","Height","Point load","Poissons ratio","Youngs modulus"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
        
    
        l  = float(fieldValues[0])
        h  = float(fieldValues[1])
        P  = float(fieldValues[2])
        nu = float(fieldValues[3])
        E  = float(fieldValues[4])
    except:
        a1 = raw_input("Length")
        b1 = raw_input("Height")
        c1 = raw_input("Point load")
        d1 = raw_input("Poissons ratio")
        e1 = raw_input("Youngs modulus")
        l  = float(a1)
        h  = float(b1)
        P  = float(c1)
        nu = float(d1)
        E  = float(e1)
    
    return l, h , P, nu , E 

def boussi_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Half-space under point loads", 
        ok_button="Continuar",
        image='boussi.gif')
    except:
        print ("No easygui module")
    
    return


def flamantP_prs():
    
    try:
        import easygui
        msg = "Wedge under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length","Point load"]
        fieldValues = []  
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

        phid = float(fieldValues[0])
        l    = float(fieldValues[1])
        P    = float(fieldValues[2])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Point load")
        phid = float(a1)
        l    = float(b1)
        P    = float(c1)
    
    
    return phid , l , P

def flamantp_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Wedge under point load (Flamant sln)", 
        ok_button="Continuar",
        image='flamantP.gif')
    except:
        print ("No easygui module")
    
    return



def flamantM_prs():
    
    try:
        import easygui
        msg = "Wedge under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length","Applied moment"]
        fieldValues = []  
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

        phid = float(fieldValues[0])
        l    = float(fieldValues[1])
        P    = float(fieldValues[2])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Applied moment")
        phid = float(a1)
        l    = float(b1)
        P    = float(c1)
    
    
    return phid , l , P

def flamantM_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Wedge under point moment (Flamant sln)", 
        ok_button="Continuar",
        image='flamantM.gif')
    except:
        print ("No easygui module")
    
    return



def flamantQ_prs():
    
    try:
        import easygui
        msg = "Wedge under point load"
        title = "Enter the problem parameters"
        fieldNames = ["Semi-angle (Degrees)","Length","Point load"]
        fieldValues = []  
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
    

        phid = float(fieldValues[0])
        l    = float(fieldValues[1])
        P    = float(fieldValues[2])
    except:
        a1 = raw_input("Semi-angle")
        b1 = raw_input("Length")
        c1 = raw_input("Point load")
        phid = float(a1)
        l    = float(b1)
        P    = float(c1)
    
    
    return phid , l , P

def flamantQ_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Wedge under transverse load (Flamant sln)", 
        ok_button="Continuar",
        image='flamantQ.gif')
    except:
        print ("No easygui module")
    
    return



def canyon_prs():
    try:
        import easygui
        msg = "Semi-circular canyon under SH waves"
        title = "Enter the problem parameters"
        fieldNames = ["Radius (1.0)","Side length(10.0)","Height (10.0)","Number of increments (4097)" , "Angle of incidence (in rads)"]
        fieldValues = []  # we start with blanks for the values
        fieldValues = easygui.multenterbox(msg,title, fieldNames)
        
    
        r = float(fieldValues[0])
        l = float(fieldValues[1])
        h = float(fieldValues[2])
        Ninc = int(fieldValues[3])
        gamma = float(fieldValues[4])
    except:
        a1 = raw_input("Radius")
        b1 = raw_input("Side length")
        c1 = raw_input("Hight")
        d1 = raw_input("Number of increments")
        e1 = raw_input("Angle of incidence (in rads)")
        r = float(a1)
        l = float(b1)
        h = float(c1)
        Ninc = int(d1)
        gamma= float(e1)
    
    return r , l , h , Ninc , gamma

def canion_hlp():
    try:
        import easygui
        easygui.msgbox(msg="",
        title="Semi-circular canyon under incident SH waves (TRifunac sln)", 
        ok_button="Continuar",
        image='canion.gif')
    except:
        print ("No easygui module")
    
    return
