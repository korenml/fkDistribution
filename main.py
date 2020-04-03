import numpy as np
from scipy.interpolate import UnivariateSpline
from matplotlib import pyplot as plt

import readFK, hist

def Main():

    #paths = ["/home/tom/OpenFOAM/tom-4.1/run/hranol/oscilace/0hz/Re90000_m11_fk0.25_ico/1/fkFY"]
    paths = ["/home/tom/OpenFOAM/tom-6/run/backwardFacingStep/Re37500/TNT_bfs_channel_mesh1_3D/3325/fkFY"]
    #mesh = ["grid 2.8 mil. cells", "grid 4.3 mil. cells", "grid 7.2 mil. cells"]
    mesh = ["m01"]
    c = 0

    n = 21
    plt.figure(figsize=(9, 5))
    for i in range(len(paths)):
        data = readFK.Read(paths[i], 0.95)
        len(data.fk)
        a = hist.Hist(data.fk, n)
        a2 = hist.Hist(data.fk2, n)
        #print(a.x, a.p)

        a.x = a.x[:-1] + (a.x[1] - a.x[0]) / 2  # convert bin edges to centers
        a2.x = a2.x[:-1] + (a2.x[1] - a2.x[0]) / 2  # convert bin edges to centers
        #print(a.x, a.p)
        [print(a.x[i], a.p[i], a2.p[i]) for i in range(0, len(a.x))]
        count = len(data.fk)
        count2 = len(data.fk2)
        plt.bar(a.x + c, a.p/count, width=1/(2*n), label=mesh[i])

        c += 1/(2*n)
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel(r"$f_k$", fontsize=20)
    plt.ylabel("cells/total cells", fontsize=20)
    plt.xticks(np.arange(0.0, 1.1, 0.1), fontsize=15)
    plt.yticks(fontsize=15)
    plt.legend(fontsize=15)
    plt.show()

    '''
    N = 1000
    n = N // 10
    print("N ", N, " n ", n)
    s = np.random.normal(size=N)  # generate your data sample with N elements
    p, x = np.histogram(s, bins=n)  # bin it into n = N//10 bins
    x = x[:-1] + (x[1] - x[0]) / 2  # convert bin edges to centers
    f = UnivariateSpline(x, p, s=N)
    plt.plot(x, f(x))
    f = UnivariateSpline(x, p, s=n)
    plt.plot(x, f(x))
    plt.show()
    '''

if __name__ == "__main__":
    Main()