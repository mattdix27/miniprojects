'''
Program to find the next prime number until the user stops asking for it:

Program starts at 2

for loop to increase number by 1 with a nested for loop to check if that's a prime
'''

def user_input(n=1):
    user = input("Would you like another prime number? y/n ")
    while user[0] != 'y' and user[0] != 'n':
        user = input("Would you like another prime number? y/n ")
    if user[0] == 'y' or user[0] == 'n':
        if user[0] == 'y':
            print("The next prime number is: ", next_prime(n))
            n=next_prime(n)
            return user_input(n)
        if user[0] == 'n':
            print("Okbyeeee")
            
        

            
def next_prime(n=1):
    if n < 2:
        return 2
    else:
        while True:
            n+=1
            for i in range(2,n):
                if n%i==0:
                    break
                elif i==n-1:
                    return n
user_input()