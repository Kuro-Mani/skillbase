num = input('for::') 
number = int(num)
def prime_f_list(number):
    divisors = []
    for prime in range(2, number+1):
        while (number % prime) == 0:
            divisors.append(prime)
            number //= prime
    return divisors
print(prime_f_list(number))