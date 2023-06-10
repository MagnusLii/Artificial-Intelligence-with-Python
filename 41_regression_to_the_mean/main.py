import numpy as np
import matplotlib.pyplot as plt

n = [500,1000,2000,5000,10000, 15000, 20000, 50000, 100000]

def throw_dice(num):
    dices = np.random.randint(1, 7, size=(num, 2))
    s = dices.sum(axis=1)
    h,h2 = np.histogram(s, range(2,14))

    plt.bar(h2[:-1],h/num)
    plt.title(f"{num} throws")
    plt.show()


for i in range(len(n)):
    throw_dice(n[i])

