import math


prime_numbers_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541]

def generate_prime_numbers(count):
    """
    :param count: how many prime numbers are needed
    :return: list of int (prime numbers)
    """
    numbers = list()
    be_tested = 2
    while len(numbers) < count:
        if prime(be_tested):
            numbers.append(be_tested)
        be_tested+=1
    return numbers

def prime(p):
    if p == 2:
        result = True
    else:
        result = True
        end = math.floor(math.sqrt(p))
        for x in range(2, end+1):
            if p % x == 0:
                result = False
                break
    return result


if __name__=='__main__':
    print(generate_prime_numbers(100))
