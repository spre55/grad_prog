# !/usr/local/bin/python3
# coding : utf-8

from matplotlib import pyplot as pl

# グラフに描画する
def drawing_graph(x,y):
    pl.plot(x, y, color="blue",linewidth=2.5, linestyle="-")

# グラフの表示
def view_graph(y):
    pl.xlim(-0.1, 1.1)
    pl.ylim(-1.5 * y, 1.5 * y)

    ax = pl.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data',0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data',0))

    pl.show()


# ハール関数
def haar_f(natural_number,k):
    '''
    0 ≤ x ≤ 1
    k : 1 ≤ k ≤ 2**n
    n : 0 or natural number
    区間[0,1]をn等分し,順次I_k
    '''
    # { q == 0, 1, 2, 3, ... , 2^n - 1 }
    roop_count = 0
    for q in range(2**(natural_number+1)):
        roop_count += 1
        x_range_min = q / (2**(natural_number+1))
        x_range_max = (q + 1) / (2**(natural_number+1))

        X = np.arange(x_range_min, x_range_max, 0.0001)

        if (natural_number == 0) and (k == 0):
            kai = 1 + (X * 0)
            drawing_graph(X,kai)

        elif (roop_count <= k*2)and(roop_count >= (k*2 -1)):
            # e_n の値が 1 or 0 の判定
            if (q % 2 == 0):
                e_n = 1
            elif (q % 2 == 1):
                e_n = 0

            kai = (2.0 * e_n - 1.0 + (X * 0.0)) * (np.sqrt(2**natural_number))

            drawing_graph(X,kai)
        else:
            kai = X*0.0
            drawing_graph(X,kai)


def main():
    argvs = sys.argv
    argc = len(argvs)

    if (argc != 3):
        print('Usage: # python %s n k ' % argvs[0])
        print('n: natural number or 0')
        print('k: 1 ≤ k ≤ 2**n')
        quit()
    elif(argc > 3):
        print('Usage: # python %s n k ' % argvs[0])
        print('n: natural number or 0')
        print('k: 1 ≤ k ≤ 2**n')
        quit()

    haar_f(int(argvs[1]),int(argvs[2]))
    view_graph(np.sqrt(2**(int(argvs[1]))))


if __name__ == '__main__':
    main()