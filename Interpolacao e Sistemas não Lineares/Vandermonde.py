import numpy as np

vander = np.array([[1,1,1,1],[1,3,9,27],[1,4,16,64],[1,5,25,125]])
solucao = np.array([0,6,24,60])

solution = np.linalg.solve(vander, solucao)

for i in solution:
    print(i)
