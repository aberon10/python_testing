def fibonacci(num):
    """Retorna el numero Fibonnaci

    num -- int
    >>> fibonacci(12)
    144
    """
    if num == 0: return 0
    if num == 1: return 1
    else: return fibonacci(num - 1) + fibonacci(num -2)

if __name__ == "__main__":
    import doctest
    doctest.testmod()