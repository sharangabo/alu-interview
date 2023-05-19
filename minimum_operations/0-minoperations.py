#!/usr/bin/python3

def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly n H characters.

    Args:
        n (int): The desired number of H characters.

    Returns:
        int: The minimum number of operations required. Returns 0 if n is impossible to achieve.

    Examples:
        >>> minOperations(9)
        6
        >>> minOperations(4)
        4
        >>> minOperations(12)
        7
    """
    if n <= 1:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        if n % divisor == 0:
            operations += divisor
            n //= divisor
        else:
            divisor += 1

    return operations


if __name__ == '__main__':
    n = 4
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

    n = 12
    print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))


