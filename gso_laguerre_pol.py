# !/usr/local/bin/python3
# coding: utf-8
from sympy.plotting import plot
from sympy import *

def schmidt(psi):
    '''
    シュミットの手続きで引数を直交関数系にする
    引数 : 関数系のリスト
    戻り値 : 引数を直交関数系にしたリスト
    '''

    phy = [] # psiを直交化したものを入れるリスト
    x = symbols("x")

    # ラゲル多項式における内積の定義
    def laguerre_pol(a,b):
        '''ラゲル多項式'''
        return( integrate(a*b, (x, 0, oo) ) )

    def siguma(n):
        siguma = 0
        for k in range(n):
            siguma += (laguerre_pol(phy[k],psi[n])/laguerre_pol(phy[k],phy[k]))*phy[k]
        return siguma

    for n in range(len(psi)):
        if (n == 0):
            phy.append(psi[0])
        elif (n >= 1):
            s = simplify(psi[n] - siguma(n))
            s_s = s/sqrt(laguerre_pol(s,s))
            phy.append(simplify(s_s))
    return phy

def main():
    '''
    ラゲル多項式を直交化する
    '''
    x = symbols("x")
    e = exp( -x/2 )
    psi = [e,e*x,e*x**2,e*x**3,e*x**4]
    phy = schmidt(psi)
    plot(phy[0],phy[1],phy[2],phy[3],phy[4],(x, 0, 5),ylim=(-0.7, 1),ylabel='',xlabel='')

if __name__ == '__main__':
    main()
