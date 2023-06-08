import numpy as np

A = np.array([[1, 2, 3], [0, 1, 4], [5, 6, 0]])

invA = np.linalg.inv(A)


print(f"A^-1: {np.linalg.inv(A)}")
print(f"A*A^-1 = {np.linalg.inv(A).dot(A).round(2)}")
print(f"A^-1*A = {A.dot(np.linalg.inv(A)).round(2)}")
