# !/usr/local/bin/python3
# coding : utf-8

import pylab as pl
import numpy as np
import sys

# グラフに描画する
def drawing_graph(x,y):
    pl.plot(x, y, color="blue",linewidth=2.5, linestyle="-")

# グラフの表示
def view_graph():
    pl.show()

# 10進数を2進数に変換する関数(リストの順序は逆)
# (ウォルシュ関数における n_0, n_1, ... , n_m-1 を求める)
def decimal_to_binary(decimal_number):

    binary_number = []

    while decimal_number > 0:
        binary_number.append(decimal_number % 2)
        decimal_number = decimal_number // 2
    return binary_number

# ウォルシュ関数
def walsh_f(n):
    # n : 数値
    # 1. nを２進数にする
    # 自然数かどうかの判定も付け足さなくては
    w_n = 1

    if n == 0:
        #区間の指定
        X = np.arange(0, 1, 0.001)
        w_n = 1 +(X*0.0)
        drawing_graph(X, w_n)

    elif n > 0:
        # n = 3のとき
        binary_list = decimal_to_binary(n) # nを2進数に変換したリスト
        binary_list_len = len(binary_list) # 2進数の桁数
        x_range = {} # xの範囲のディクショナリ
        r_n = {} # r_n 関数のディクショナリ
        w_n = [] # W_n 関数の各範囲毎に乗算して描画する為のリスト

        for x in range(2**binary_list_len):
            w_n.append(1)


        for i in range(binary_list_len):

            x_range[i] = {}
            r_n[i] = {}

            for q in range(2**(binary_list_len - i)): # q = {0,1,2} binary_list_len = 2 # i = 0,1
                #区間の指定
                range_min = q / ( 2**(binary_list_len - i) )
                range_max = (q + 1) / ( 2**(binary_list_len - i) )
                x_range[i][q] = (range_min,range_max)

                # e_n の値が 1 or 0 の判定
                if (q % 2 == 0):
                    e_n = 1
                elif (q % 2 == 1):
                    e_n = 0

                r_n[i][q] = (2.0 * e_n - 1.0)**binary_list[-(i+1)]

        for i in range(binary_list_len):
            for q in range(2**(binary_list_len-1)):

                w_n[q] *= r_n[i][q//(2**i)]
                w_n[q+2**(binary_list_len-1)] *= r_n[i][ (q+2**(binary_list_len-1)) // (2**i) ]

        for q in range(2**(binary_list_len)):
            X = np.arange(x_range[0][q][0], x_range[0][q][1], 0.001)
            drawing_graph(X, w_n[q]+(X*0))

def main():
    n = int(sys.argv[1])

    for i in range(n+1):
        pl.subplot(n+1,1,i+1)
        walsh_f(i)
        pl.xlim(-0.1, 1.1)
        pl.ylim(-1.5, 1.5)

        ax = pl.gca()  # gca stands for 'get current axis'
        ax.spines['right'].set_color('none')
        ax.spines['top'].set_color('none')
        ax.xaxis.set_ticks_position('bottom')
        ax.spines['bottom'].set_position(('data',0))
        ax.yaxis.set_ticks_position('left')
        ax.spines['left'].set_position(('data',0))

    view_graph()

if __name__ == '__main__':
    main()