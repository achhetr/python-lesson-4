# Program to check if a number is prime or not
# 5 -> 5, 1

# get number from the user
num = 1

# define is_prime_number function with parameter num
def is_prime_number(n):
  if n == 1:
    return False

  # loop number - 1 to 2
  for i in range(2, n // 2):
    # if number can be divided
    if n % i == 0:
      # return false
      return False

  # after the loop return true
  return True

# display result
result = is_prime_number(num)
print(f'Is this {num} a Prime?: {str(result)}')
