
# exercise 3

def tripling_value(single_digit):
    """ (int) -> int

    Return the parameter value single_digit
    back to the user three times in succession
    
    Value entered must be single integer value between 1-9.

    >>> tripling_value (4)
    444

    >>> tripling_value (8)
    888

    >>> tripling_value (1)
    111

    """
    return (single_digit*100) + (single_digit*10) + (single_digit)


# exercise 3

def times_three(num):
    """ (int) -> int

    Return a value entered multipled by 3

    >>> times_three(3)
    9

    >>> times_three(82)
    246

    >>> time_three(11)
    33

    """

    return num*3


# exercise 4

def absolute_difference(num1, num2):
    """ (int, int) -> int

    Return a value that is the difference of the value in absolute terms

    >>> absolute_difference(9, 14)
    5

    >>> absolute_difference(19, 1)
    18

    >>> absolute_difference(-70, 0)
    70

    """

    return abs(num2 - num1)



