#!/usr/bin/python3
# Python program to display all the prime numbers within an interval

lower = 1
upper = 500

print("Prime numbers between", lower, "and", upper, "are:") # display the prime numbers between lower and upper

for num in range(lower, upper + 1): # iterate through the numbers in the specified range
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):  # check for factors from 2 to num-1
           if (num % i) == 0:  # if num is divisible by any number other than 1 and itself, it is not prime
               break
       else:
           print(num)
