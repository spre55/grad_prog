# !/usr/local/bin/python3
# coding: utf-8

from sympy.plotting import plot
from matplotlib import pyplot as pl
from sympy import *
import sys

# グラフに描画する
def plot_graph(phy):
    x = symbols("x")
    plot(phy[0],phy[1],phy[2],phy[3],(x, -10, 10),ylim=(-10,10))

# シュミットの手続きによる直交化
def schmidt(psi):
    '''
    シュミットの手続きで引数を直交関数系にする
    引数 : 関数系のリスト
    戻り値 : 引数を直交関数系にしたリスト
    '''

    phy = [] # psiを直交化
    x = symbols("x")

    # エルミート多項式における内積の定義
    def hermite_pol(a,b):
        '''エルミート多項式'''
        return( integrate(a*b*exp(-x**2), (x, -oo, oo) ) )

    def siguma(n):
        siguma = 0
        for k in range(n):
            siguma += (hermite_pol(phy[k],psi[n])/hermite_pol(phy[k],phy[k]))*phy[k]
        return siguma

    for n in range(len(psi)):
        if (n == 0):
            phy.append(psi[0])
        elif (n >= 1):
            phy.append((psi[n] - Siguma(n))

    return phy

def main():
    '''
    エルミート多項式
    '''
    x = symbols("x")
    psi = [1,x,x**2,x**3]
    print(schmidt(psi))
    plot_graph(schmidt(psi))

if __name__ == '__main__':
    main()
