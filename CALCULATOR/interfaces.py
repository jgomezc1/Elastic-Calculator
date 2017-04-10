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
        fieldNames = ["Element size","Element type","Intrpolation order"]
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