import numpy as np

a, b, c = map(int, input().split())
arr = np.array([input().split() for _ in range(a)], int)
arr1 = np.array([input().split() for _ in range(b)], int)
print(np.concatenate((arr, arr1), axis = 0))