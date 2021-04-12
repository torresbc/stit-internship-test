"""Escreva um script que receba um inteiro n como número de linhas e colunas
de uma matrix e receba uma lista com os elementos da matrix.
Exemplo: n = 3        m = [[11    2    4 ]
                           [4     5    6 ]
                           [10    8   -12]  output = 15
E imprima o determinante absoluto da matrix
para -100 <= m[i][j] <= 100
"""
import numpy as np


def generate_list():
    """
    Iterate the input() to generate a new list with only integers.

    :return: list:
    """
    return list(map(int, input("Digite os números da matriz separados por espaço: ").split(" ")))


def create_matrix(ij, list):
    """
    Generate a matrix with the same number of columns and rows.

    :param ij:
    :param list:
    :return: matrix:
    """
    return np.array(list).reshape(ij, ij)


def calculate_determinant(matrix):
    """
    Calculate the absolute determinant from a matrix.

    :param matrix:
    :return:
    """
    return np.linalg.det(matrix)


def main():
    ij = int(input("Digite o número de linhas e colunas: "))

    list = generate_list()

    matrix = create_matrix(ij, list)

    determinant = calculate_determinant(matrix)

    print(determinant)


if __name__ == "__main__":
    main()



