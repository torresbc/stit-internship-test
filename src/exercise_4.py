"""Escreva um script que receba pontos de uma reta e imprima o ponto médio
Exemplo: r = [(1, 3), (-5,-6)] m =(-2,-1.5)
"""
def iterate_list():
    """
    Iterate list to get each number as a new item for a new list.

    :param list:
    :return: list:
    """
    return list(map(int, input("Digite os números da matriz separados por espaço: ").split(" ")))


def get_midpoints(points):
    """
    Get the midpoints between 2 differents points.

    :param integer:
    :return: list:
    """
    return [sum(point) / len(point) for point in zip(*points)]


def main():
    list = iterate_list()

    point_1 = (list[0], list[1])
    point_2 = (list[2], list[3])

    midpoint = get_midpoints([point_1, point_2])

    print(midpoint)


if __name__ == "__main__":
    main()

