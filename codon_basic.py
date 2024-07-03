import random
import time
# import codon

from typing import List


# note that numba throws a reflection error if we return a list of lists instead of a numpy array
def gen_sq_matrix(n):
    return [[random.random() for i in range(n)] for _ in range(n)]


# @codon.jit
def multiply_matrices(matrix1, matrix2):
    multiplied_matrix = [[0 for _ in range(len(matrix2[0]))]
                         for _ in range(len(matrix1))]

    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                multiplied_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return multiplied_matrix


def main():
    a = gen_sq_matrix(500)
    b = gen_sq_matrix(500)

    start = time.time()
    c = multiply_matrices(a, b)
    end = time.time()
    print(f"Time taken: {end - start} seconds")


if __name__ == "__main__":
    main()
