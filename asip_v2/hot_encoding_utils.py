# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 15:08:35 2021

@author: Alissa Kouraeva
"""

import glob
import os

import matplotlib.pyplot as plt
import matplotlib as mpl
import netCDF4 as nc
import numpy as np

def form_of_ice(stage):
    """
    Gives back the index the concentration or 1 should be on. Each index corresponds to a particular ice type 
    (0: Young ice; 1: First Year ice; 2: Multi year ice ; 3: Ice free)
    --- 
    input : stage : stage of development : integer
    ---
    output : index : integer
    """
    index_=0
    #if stage ==0:
        #index_ = 0
        #print('ice_free')
    if stage!=-9:
        if stage in range(81,86):
            #print('Young ice')
            index_=1
        if stage in range(86,94):
            #print('First year ice')
            index_=2
        if stage in range(95,98):
            #print('multiyear ice')
            index_=3
    return index_
    

def one_hot_m1(ct,ca,sa,cb,sb,fb,cc,sc):
    L=[ct,ca,sa,cb,sb,fb,cc,sc]
    index = np.argmax(L)
    #print(index)
    if index ==0:
        result = [1,0,0,0]
    else :
        #print([sa,sb,sc])
        #print('bibi',[sa,sb,sc][index])
        index2 = form_of_ice([sa,sb,sc][index])
        #print(index2)
        result = [0,0,0,0]
        result[index2]=1
    return result

def one_hot_m2(ct,ca,sa,cb,sb,fb,cc,sc):
    result = [0,0,0,0]
    result[0] = int(ct)/100
    for si, ci in zip([sa,sb,sc], [ca,cb,cc]):
        #print(si)
        index_2 = form_of_ice(si)
        result[index_2] += ci/100
    return result