# Python program to find the factorial of a number provided by the user

# 5! -> 5 * 4 * 3 * 2 * 1 => 120

# get user input
num = int(input('Enter number: '))

# create a variable to save the product
factorial = 1
# loop number to 1 range(1, 5 + 1) -> 1,5
for i in range(1, num + 1):
  # save the number multiply with the next number
  factorial *= i

# print results
print(f'number {num} factorial is {factorial}!')
