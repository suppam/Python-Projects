def convert_to_celsius(fahrenheit):

    """ (number) -> float

    Return the number of Celsius degrees equivalent to fahrenheit degrees.
    
    >>> convert_to_celsius(75)
    23.88888888888889
    
    """
    
    return (fahrenheit - 32.0) * 5.0 / 9.0


def above_freezing(celsius):

    """ (celcius) -> float

    Return True if value entered in celsius is above zero
    
    >>> above_freezing(75)
    True

    >>> above_freezing(-10)
    False
    
    """
    
    return celsius > 0
        
