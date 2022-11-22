# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

num1 = 10
num2 = 20

def smallest_positive_multiples(num):
  product = 1
  for i in range(2, num + 1):
    # check remainder is zero
    if num % i == 0:
      product *= i
    else:
      product = 1
    # return product

    # continue as a home work


# test cases

print(smallest_positive_multiples(num1) == 2520)
print(smallest_positive_multiples(num2) == 2520)
