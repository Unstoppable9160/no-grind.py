# Big O Notation of Bubble Sort:
#   Best Case   : O(n)
#   Avrage Case : O(n^2)
#   Worst Case  : O(n^2)


def sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def Bubble_Sort(a):
    sort(a)
    print("Sorted array is:")
    for i in range(len(a)):
        print("% d" % a[i]),
