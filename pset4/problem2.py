#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import numpy as np

def gauss_upper_diag_tridiag(M):
    """Take a tridiagonal LGS (Matrix N+1xN) M and returns the upper triangle matrix"""
    M[0]/=M[0][0]
    for i in range(1,len(M[:,0])):
        M[i]-=M[i-1]*M[i,i-1]
        M[i]/=M[i][i]
    return M
        
def unit_from_upper_diag_backwards_sub(M):
    for i in range(0,len(M[:,0])):
        for j in range(1, i+1):##for compatibility with non-tridiag matrices
            M[-i-1]-=M[-i-1,-j-1]*M[-j]
    return M

M=np.identity(10)*2+np.pad(np.identity(9),((1,0),(0,1)), "constant")*-1+np.pad(np.identity(9),((0,1),(1,0)), "constant")*-1


def make_tridiag(a,b,c, y=None, dim=None):
    """makes tridiagonal matrix M from either numbers or vectors a,b,c,. If numbers are given put dimension else u get error"""
    if not dim:
        dim=len(b)
    M=np.identity(dim)*b+np.pad(np.identity(dim-1)*a,((1,0),(0,1)), "constant")+np.pad(np.identity(dim-1)*c,((0,1),(1,0)), "constant")
    if y:
        return np.hstack((M,np.array(10*[[1]])*y))
    else:
        return M

def solution_tridiag(a,b,c,y, dim):
    return unit_from_upper_diag_backwards_sub(gauss_upper_diag_tridiag(make_tridiag(a,b,c,y, dim)))[:,-1]
s=solution_tridiag(-1,2,-1, 0.1, 10)
print("Solution for x:",s)
print("Error for M dot s:", make_tridiag(-1,2,-1, dim=10).dot(s)-0.1)