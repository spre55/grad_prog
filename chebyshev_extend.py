# !/usr/local/bin/python3
# coding: utf-8

from sympy.plotting import plot
from sympy import symbols,factorial,diff,simplify,Rational

# ロドリーグの公式により与えられた関数系の直交化を行う.
def rodrigues_formula(rho,m,k):
    '''チェビシェフ多項式のロドリーグ(ロドリゲス)の公式'''

    x = symbols("x")
    p = []

    def set_c(n,m,k):
        def function(n,m):
            s = 1
            for i in range(1, n+1):
                s = s*(i-m)
            return s

        k_n = (-2*k)**n
        c = Rational(1 , (function(n,m) * k_n))
        return c

    def set_v(n,m,k):
        v = (1 - (k**2) * (x**2) )**(n)
        return v

    def rodrigues(m,k):
        for n in range(7):
            rodrigues_f = set_c(n,m,k) * (1/rho) * diff( (set_v(n,m,k) * rho) , x, n)
            p.append( rodrigues_f )

    rodrigues(m, k)
    return p

def main():
    x = symbols("x")

    m = Rational(1,3) #1/3
    k = 2 #Rational(1,2)
    rho = (1 - (k**2) * (x**2) )**(-m)
    color = ["b","r","g","k","c","m","y"]

    T = rodrigues_formula(rho,m,k)
    p = []


    for i in range(7):
        t = simplify(T[i])
        print ("T(",i,") = ", t)
        if i > 0 :
            p.append( plot(T[i],(x,-0.52,0.52),ylim=(-1.1,1.1),show=False,line_color=color[i]) )
            p[0].extend(p[i])
        else:
            p.append( plot((T[i],(x,-0.52,0.52)),ylim=(-1.1,1.1),show=False,line_color=color[i]) )
    p[0].show()

if __name__ == '__main__':
    main()
