import numpy as np


def is_diagonally_dominant(A):

    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= row_sum:
            return False
    return True


def modify_to_diagonally_dominant(A, b):
    n = len(A)
    for i in range(n):
        diag = abs(A[i][i])
        row_sum = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= row_sum:
            A[i][i] = row_sum + 1
            b[i] = row_sum


def gauss_seidel(A, b, tol=0.000001, max_iter=100):
    if not is_diagonally_dominant(A):
        print("The matrix is not diagonally dominant. Modifying the equations.")
        modify_to_diagonally_dominant(A, b)

    n = len(A)
    x = np.zeros(n)
    for iteration in range(max_iter):
        x_new = np.zeros(n)
        for i in range(n):
            s1 = np.dot(A[i, :i], x_new[:i])
            s2 = np.dot(A[i, i + 1:], x[i + 1:])
            x_new[i] = (b[i] - s1 - s2) / A[i, i]
        if np.allclose(x, x_new, atol=tol):
            print(f"Converged after {iteration + 1} iterations.")
            return x_new
        x = x_new
    print(f"Gauss-Seidel did not converge within {max_iter} iterations.")
    return x


A = np.array([[11, 2, 11], [3, 100, 100], [36, 36, 122]], dtype=float)
b = np.array([7, 8, 8], dtype=float)

result = gauss_seidel(A, b, 0.0001, 10)
print(A)
print("Solution:", result)

