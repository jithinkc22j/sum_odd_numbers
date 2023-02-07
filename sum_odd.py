#Program to find the sum of odd numbers upto n using user defined function
def su(n):
    if n==1:
        return(n)
    else:
        if n%2==0:
             return(su(n-1))
        else:
           return(n)+su(n-1)
n=int(input('Enter your number: '))
print('\n The sum of',n,' odd number is',su(n))
