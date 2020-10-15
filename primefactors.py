'''
Find factors of a number, check if those factors are prime numbers, create a list of the factors that are prime
'''

def find_prime_factors(num):
    factors = []
    for i in range(2,num):
        if num%i == 0:
            factors.append(i)
    print(factors)
    
    prime_factors = []
    if factors[0]==2:
        prime_factors.append(2)
    for factor in factors:
        for i in range(2,factor):
            if factor%i==0:
                break
            elif i == factor-1:
                prime_factors.append(factor)
    return prime_factors

print(find_prime_factors(56881118))