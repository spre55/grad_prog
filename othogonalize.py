# !/usr/local/bin/python3
# coding: utf-8
from sympy import *

# グラフに描画する
def plot_graph(phy):
    x = symbols("x")
    plot(phy[0],phy[1],phy[2],phy[3],phy[4],phy[5],phy[6],(x, -1, 15),ylim=(-100,100),ylabel='',xlabel='')

def lanczos(psi):

    x = symbols("x")
    p = [0]

    def inner_priduct(a,b):
        '''ラゲル多項式'''
        return( integrate(a*b, (x, 0, oo) ) )

    def recursion(a):
        p.append(psi[0])
        p.append(psi[1])

        for i in range(3,len(psi)+1):
            b = inner_priduct(x*p[i-1],p[i-1])/inner_priduct(p[i-1],p[i-1])
            r = inner_priduct(p[i-1],p[i-1])/inner_priduct(p[i-2],p[i-2])
            p.append( (a*x - b)*p[i-1] - r*p[i-2] )

    recursion(1)
    p.pop(0)
    return p

def main():
    x = symbols("x")
    e = exp( -x/2 )
    psi = [e,e*x,e*x**2,e*x**3,e*x**4,e*x**5,e*x**6]

    p = lanczos(psi)
    plot_graph(p)

if __name__ == '__main__':
    main()
