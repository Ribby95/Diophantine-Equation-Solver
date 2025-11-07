# -*- coding: utf-8 -*-
"""
Created on Fri Jun 20 21:57:58 2025

@author: rwstu
"""
def projection(vector1,vector2):#peojection of vector 1 onto vector 2
    dot=sum([vector1[i]*vector2[i] for i in range(0,len(vector1)-1)])
    norm=sum(x**2 for x in vector2)
    return dot/norm
        
def GrahmSchmidtt(basis,normailize=False):
    newbasis=[]
    for i in basis:
        newbasis.append()


def LLL(basis,parameter=0.75):
    pass
