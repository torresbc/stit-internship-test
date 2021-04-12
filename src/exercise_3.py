"""Escreva um script que receba um inteiro n e imprima quantos divisores são
divisíveis por 2.
Para 1 <= n <= 100
Exemplo:  n = 8 divisores = 1, 2, 4, 8  output = 3
"""
def get_divisors(integer):
    """
    Get all divisors of a input number, being that each divisor must be divisible by 2 also.

    :param integer:
    :return: list:
    """
    divisors = []
    for number in range(1, 9):
        if 8 % number == 0 and number % 2 == 0:
            divisors.append(number)

    return divisors


def main():
    integer = input(f"Digite um número inteiro: ")

    divisors = len(get_divisors(integer))

    print(divisors)


if __name__ == "__main__":
    main()