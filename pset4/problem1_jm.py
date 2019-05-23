#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 18:25:55 2019

@author: wambo
"""
import numpy as np
###solve something  using gauß-jordan

def upper_diag(M):
    ##M: NxN+1 Matrix (numpy array), returns the matrix as solved equation
    if M[0,0]==0:
        if not any(M[:,0]):##check if every number is zero in this column
            raise ValueError("Linear Dependence!")
        else:
            for i in range(len(M[:,0])):
                if M[i,0]!=0:
                    M[[0,i]]=M[[i,0]]
                    return upper_diag(M)
    else:
        M[0]=M[0]/M[0,0]
        for i in range(1,len(M[:,0])):
            M[i]=M[i]-M[0]*M[i,0]
        if len(M[:,0])>1:
            M[1:, 1:]=upper_diag(M[1:, 1:])
        return M

N=np.array([[1e-6, 0.5,0.5],[0.5,0.,0.25]])

A=upper_diag(N)
def unit_from_upper_diag(M):
    for i in range(1,len(M[:,0])):
        print(M)
        M[-i-1]-=M[-i-1,-i-1]*M[-i]
    return M
print(unit_from_upper_diag(A))