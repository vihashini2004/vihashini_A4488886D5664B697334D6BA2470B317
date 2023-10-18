def factorial_iterative(n):
  result = 1
  for i in range(1, n + 1):
      result *= i
  return result

# Input the number for which you want to calculate the factorial
num = int(input("Enter a number: "))

if num < 0:
  print("Factorial is not defined for negative numbers.")
else:
  result = factorial_iterative(num)
  print(f"The factorial of {num} is {result}")
