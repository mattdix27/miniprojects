'''
Find all prime numbers up to n
'''

def sieve(n):
    marked_numbers = []
    prime_numbers = []
    for num in range(2,n):
        if num not in marked_numbers:
            prime_numbers.append(num)
            for mult in range(num+1,n):
                if mult%num == 0 and mult not in marked_numbers:
                    marked_numbers.append(mult)
    return prime_numbers

print(sieve(1000))