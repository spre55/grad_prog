# !/usr/local/bin/python3
# coding: utf-8

from sympy.plotting import plot
from sympy import symbols,integrate

# シュミットの手続きによる直交化
def schmidt(psi):
    '''
    シェミットの手続きで引数を直交関数系にする
    引数 : 関数系のリスト
    戻り値 : 引数を直交関数系にしたリスト
    '''

    phy = [] # psiを直交化
    x = symbols("x")

    # ルジャンドルの多項式における内積の定義
    def legendre_pol(a,b):
        '''ルジャンドルの多項式'''
        return( integrate(a*b, (x, -1, 1) ) )

    def siguma(n):
        siguma = 0
        for k in range(n):
            siguma += (legendre_pol(phy[k],psi[n])/legendre_pol(phy[k],phy[k]))*phy[k]
        return siguma

    for n in range(len(psi)):
        if (n == 0):
            phy.append(psi[0])
        elif (n >= 1):
            phy.append(psi[n] - siguma(n))

    return phy

def main():
    '''
    legendre_polynomial.py : ルジャンドルの多項式
    '''
    x = symbols("x")
    psi = [1,x,x**2,x**3,x**100]
    phy = schmidt(psi)
    plot(phy[0],phy[1],phy[2],phy[3],phy[4],(x, -1.5, 1.5),ylim=(-1.5,1.5),ylabel='',xlabel='')


if __name__ == '__main__':
    main()
