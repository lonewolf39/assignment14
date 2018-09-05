#Q.1- print the cube of each value of a list

l1 = [1,2,3,4]
a = [a**3 for a in l1]
print("After cube all elements in list")
print(a)

#Q.2- Get all the prime numbers in a specific range

n = int(input("Enter the range"))
print("Prime numbers are: ")
a = [p for p in range(2,n) if 0 not in [p%d for d in range(2,p)]]
print(a)

#Q.3- Difference between list comprehension and generator expression

"""In terms of syntax, the only difference is that you use parenthesis instead of square brackets.
The main advantage of generator over a list is that it take much less memory."""

#LAMBDA & MAP


#Q.1- convert the python list of fahrenheit 

C = [39.2, 36.5, 37.3, 37.8]
print("Temp Farenhite")
y=list(map(lambda x:(x * 1.8) + 32,C))
print(y)

#Q.2- Square all the elements of a list

l = [1,2,3,4,5]
x = list(map(lambda x:x**2,l))
print(x)

#FILTER & REDUCE

#Q.1- Filter out all the primes from a list

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
for i in range(2, 8): 
     n = list(filter(lambda x: x == i or x % i and x > 1, nums))
print("Filtered Elements")
print(n)

#Q.2- Multiply all the elements of a list

from functools import reduce
l1 = [1,2,3,4,5,6]
a = reduce(lambda x, y: x*y,l1)
print(a)
