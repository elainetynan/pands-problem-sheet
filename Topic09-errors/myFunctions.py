# myFunctions.py
#
# Fibonacci to practice testing
#
# Author: Andrew Beatty

import logging
#logging.basicConfig(level=logging.DEBUG)

def fibonacci(number):
    if number < 0:
        raise ValueError('number must be > 0')

    if number == 0:
        return []

    a = 0
    b = 1
    fibonacciSequence = [0]
    
    # we have one in the list already so number - 1 times this is not the
    # most efficient code could have used yield
    for i in range(1,number):
        fibonacciSequence.append(b)
        # this is funky code make a = b and b = a + b
        a , b = b, a + b

    logging.debug("%d: %s",number, fibonacciSequence)
    return fibonacciSequence



if __name__ == '__main__':
    # tests
    return7 = [0, 1, 1, 2, 3, 5, 8]
    return11 = [0,1,1,2,3,5,8,13,21,34,55]
    actual7 = fibonacci(7)
    actual11 = fibonacci(11)
    actual0 = fibonacci(0)
    actual1 = fibonacci(1)
    assert fibonacci(7) == return7, 'incorrect return for 7 '+ str(actual7)
    assert fibonacci(11) == return11, 'incorrect return for 11' + str(actual11)
    assert fibonacci(0) == [], 'incorrect return value for 0' + str(actual0)
    assert fibonacci(1) == [0], 'incorrect return value for 1' + str(actual1)

    try:
        fibonacci(-1)
    except ValueError:
        # we want this exception to be thrown
        # so this is an example where we want to do nothing
        pass
    else:
        # if the exception was not thrown we should throw
        # Assertion error
        assert False, 'fibonacci missing ValueError'
        # or
        #raise AssertionError("fibonacci no valueError ")

    print("all good")