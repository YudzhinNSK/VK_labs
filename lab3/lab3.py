from numpy import loadtxt
from tol import tolsolvty
import numpy as np


def main():
    infA = np.array([[3, 6, 0], [7, 12, 4]])
    supA = np.array([[4, 7, 1], [8, 13, 5]])
    infb = np.array([[1.3], [5.3]])
    supb = np.array([[2.0], [6.0]])

    [tolmax, argmax, envs, ccode] = tolsolvty(infA, supA, infb, supb)
    print('tolmax = ', tolmax)
    print('argmax = ', argmax)
    print('envs = ', envs)
    print('ccode = ', ccode)


if __name__ == "__main__":
    main()