import numpy as np
from scipy import stats


def median(a):
    print(np.median(a))


def mean(a):
    print(np.mean(a))


def mode(a):
    print(stats.mode(a))
