import os
import sys
import traceback


def rotatearray(arr, d):
    try:
        for index in range(0, d):
            rotateonebyone(arr)
    except Exception:
        print(traceback.format_exc())


def rotateonebyone(arr):
    try:
        temp = arr[0]
        for index in range(0, len(arr) - 1):
            arr[index] = arr[index + 1]

        arr[index + 1] = temp
    except Exception:
        print(traceback.format_exc())


def reversearray(arr, start, end):
    try:
        while start < end:
            temp = arr[start]
            arr[start] = arr[end]
            arr[end] = temp
            start = start + 1
            end = end - 1
    except Exception:
        print(traceback.format_exc())


def rotatearray(arr, d):
    try:
        reversearray(arr, 0, d - 1)
        reversearray(arr, d, len(arr) - 1)
        reversearray(arr, 0, len(arr) - 1)
    except Exception:
        print(traceback.format_exc())


if __name__ == "__main__":
    arr = [2, 6, 1, 8, 9]
    rotatearray(arr, 2)

    print arr
