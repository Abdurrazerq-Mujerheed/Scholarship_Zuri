#addition, subtraction, division, multiplication and modulus operations

print(".............Welcome to Simple Zuri Calculator............. \n")

#user_selection = int(input())

#Addition
def add(a, b):
  return a + b

#Subtraction
def sub(a, b):
  return a - b

#Multiplication
def mul(a, b):
  return a * b

#Division
def div(a, b):
  if b != 0 :
    return a / b
  else:
    return "Cannot be divisible"

#Modulus
def mod(a, b):
  return a % b

always = True 

while always:
  print("Choose operation you want to perform by type: \n 1 for addition,\n 2 for subtraction,\n 3 for division,\n 4 for multiplication and\n 5 for modulus.")
  user_selection = int(input())
  
  a = float(input("Enter the first number: "))
  b = float(input("Enter the second number: "))
  
  if user_selection == 1 :
    print(add(a, b))
  elif user_selection == 2 :
    print(sub(a, b))
  elif user_selection == 3 :
    print(mul(a, b))
  elif user_selection == 4 :
    print(div(a, b))
  elif user_selection == 5 :
    print(mod(a, b))
  else:
    print("Out of selections")
    always = False