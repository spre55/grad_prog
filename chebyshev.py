# !/usr/local/bin/python3
# coding: utf-8

from sympy.plotting import plot
from sympy import symbols,factorial,diff,simplify

# ロドリーグの公式により与えられた関数系の直交化を行う.
def rodrigues_formula(rho):
    '''チェビシェフ多項式のロドリーグ(ロドリゲス)の公式'''
    def set_c(n):
        n2 = 2 * n
        return( ((-1)**n) * ((2**n) * factorial(n) ) / factorial(n2) )

    def set_v(n):
        return( (1 - x**2)**n )

    x = symbols("x")
    p = []

    def rodrigues():
        for n in range(7):
            rodrigues_f = set_c(n) * (1/rho) * diff( (set_v(n) * rho) , x, n)
            p.append( rodrigues_f )

    rodrigues()
    return p

def main():
    x = symbols("x")
    rho = (1 - x**2)**(-1/2)
    color = ["b","r","g","k","c","m","y"]

    T = rodrigues_formula(rho)
    p = []


    for i in range(7):
        t = simplify(T[i])
        print ("T(",i,") = ", t)
        if i > 0 :
            p.append( plot(T[i],(x,-1.1,1.1),ylim=(-1.1,1.1),show=False,line_color=color[i]) )
            p[0].extend(p[i])
        else:
            p.append( plot((T[i],(x,-1.1,1.1)),ylim=(-1.1,1.1),show=False,line_color=color[i]) )
    p[0].show()


if __name__ == '__main__':
    main()
