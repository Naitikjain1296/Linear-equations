import numpy as np
A=np.array([[9,3],[18,6]])
B = np.array([-12, -24])
X = np.linalg.solve(A,B)
print(X)