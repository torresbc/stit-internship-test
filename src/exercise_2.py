"""Escreva um script que receba duas listas com frases e retorne um
dicionário com as palavras iguais e diferentes agrupadas.
Exemplo:
         lista_1 = ['Abacate é muito bom']
         lista_2 = ['Gosto muito de Abacate']
Output:
        dict_1 = {'Iguais':['Abacate', 'muito'],
                   'Diferentes':['Gosto', 'é', 'de', 'bom']}
"""
def iterate_list(list):
    """
    Split list first item by space.

    :param list:
    :return: list:
    """
    return list[0].split(" ")


def get_difference(set_1, set_2):
    """
    Return only the different items between set_1 and set_2.

    :param set_1:
    :param set_2:
    :return: set:
    """
    return set_1.difference(set_2)


def get_union(difference_1, difference_2):
    """
    Return the union between difference_1 and difference_2 sets.

    :param difference_1:
    :param difference_2:
    :return: set:
    """
    return difference_1.union(difference_2)


def get_intersection(set_1, set_2):
    """
    Get the intersection between set_1 and set_2.

    :param list_1:
    :param list_2:
    :return: set:
    """
    return set_1.intersection(set_2)


def create_dict(difference, intersection):
    """
    Create a dictionary with two fixed keys.

    :param difference:
    :param intersection:
    :return: Dict:
    """
    return {'Iguais': difference,
            'Diferentes': intersection
            }


def main():
    lista_1 = ['Abacate é muito bom']
    lista_2 = ['Gosto muito de Abacate']

    set_1 = set(iterate_list(lista_1))
    set_2 = set(iterate_list(lista_2))

    difference_1 = get_difference(set_1, set_2)
    difference_2 = get_difference(set_2, set_1)

    total_difference = list(get_union(difference_1, difference_2))

    intersection = list(get_intersection(set_1, set_2))

    dict_1 = create_dict(total_difference, intersection)

    print(dict_1)


if __name__ == "__main__":
    main()