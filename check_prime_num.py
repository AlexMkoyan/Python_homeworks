import math

def is_prime(num):

    # raise TypeError for invalid input type
    if type(num) != int:
        raise TypeError('The input is of invalid type.')
    
    # raise ValueError for invalid input value
    if num < 0:
        raise ValueError('The input can not be negative integer.')
    
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            return False
    return True
    


# print(is_prime(3))
# print(is_prime(5))
# print(is_prime(12))
# assert is_prime(7) == True