#coding:utf-8

from matplotlib import pyplot as pl
import numpy as np
import sys

def rademacher_f(natural_number):
    # { q == 0, 1, 2, 3, ... , 2^n - 1 }

    for q in range(2**natural_number):
        x_range_min = q / (2**natural_number)
        x_range_max = (q + 1) / (2**natural_number)

        # e_n の値が 1 or 0 の判定
        if (q % 2 == 0):
            e_n = 1
        elif (q % 2 == 1):
            e_n = 0

        X = np.arange(x_range_min, x_range_max, 0.0001)
        r_n = 2.0 * e_n - 1.0 + (X * 0.0)

        pl.plot(X, r_n, color="blue", linewidth=2.5, linestyle="-")


def main():
    n = int(sys.argv[1])
    for i in range(n):

        pl.subplot(n,1,i+1)
        rademacher_f(i+1)
        pl.xlim(-0.1, 1.1)
        pl.ylim(-1.5, 1.5)

        ax = pl.gca()
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data',0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))

    pl.show()

if __name__ == '__main__':
    main()
