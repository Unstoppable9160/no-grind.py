# Big O Notation of Bogosort:
#   Best Case   : O(n)
#   Avrage Case : O((n+1)!)
#   Worst Case  : O(1)

import random


def sort(a):
    n = len(a)
    while (is_sorted(a) == False):
        shuffle(a)


def is_sorted(a):
    n = len(a)
    for i in range(0, n-1):
        if (a[i] > a[i+1]):
            return False
    return True


def shuffle(a):
    n = len(a)
    for i in range(0, n):
        r = random.randint(0, n-1)
        a[i], a[r] = a[r], a[i]


def Bogosort(a):
    sort(a)
    print("Sorted array :")
    for i in range(len(a)):
        print("%d" % a[i]),
