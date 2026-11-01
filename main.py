#add two numbers
def add(a,b):
    return a+b
print(add(int(input("enter 1st number:")),int(input("enter 2nd number:"))))
def even_odd(num):
    if num%2==0:
        return "it is even"
    else:
        return "it is odd"
print(even_odd(13)) 
############   
def leap_year(year):
    if (year%4==0 and year%100!=0) or year%400==0:
        return "it is leap year"
    else:
        return "it is not leap year" 
print(leap_year(2004))    
#############
def is_prime(num):
    if num<2:
        return "it is  not prime number"
    else:
        for i in range(2,num):
            if num%i==0:
                return " it is not prime number"
        return "it is prime number"     
print(is_prime(2)) 
######   
def armstrong(num1,num2):
    n=len(str(num1))
    ans=[]
    for i in range(num1,num2+1):
        
        temp=i
        sum=0
        while temp>0:
            k=temp%10
            sum+=k**n
            temp=temp//10
        if sum==i:
            ans.append(i)  
    return ans          
print(armstrong(100,500))            
####factorial using recursion
def factorial(num):
    if num==1:
        return 1
    return num*factorial(num-1)
print(factorial(4))
####sum of digits
def sum_of_digits(num):
    if num==0:
        return 0
    
    sum=num%10+sum_of_digits(num//10)
    return sum
print(sum_of_digits(253))
###chech_pallindrome
def is_palindrome(text):
    if len(text)==1 or len(text)==0:
        return "The string is pallindrome"
    if text[0]==text[-1]:
        return is_palindrome(text[1:-1])
    return "The string is not palindrome"
print(is_palindrome("cat"))
#reverse a number 
def reverse_num(num,rev=0):
    if num==0:
        return rev
    k=num%10
    rev=rev*10+k
    return reverse_num(num//10,rev)
    
    
print(reverse_num(521))
####fibonacci series

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

for i in range(10):
    print(fib(i), end=" ")
##0 1 1 2 3 5 8 13 21 34