


import matplotlib as mpl

mpl.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np


def demo():
    
    t = np.arange(1.0, 2.0, 0.1)    
    s = 1 + np.tan(2 * np.pi * t**2)
    
    plt.plot(t, s)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (mV)')
    plt.title('About as simple as it gets, folks')
    plt.grid(True)
    plt.savefig("test.png")
    plt.show()

if __name__ == '__main__':
    demo()