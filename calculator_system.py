########################### Calculator System ####################### 

############################ by -  Payakan #########################
logo = '''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
'''


print(logo)



def sum(num1, num2):
  return num1 + num2


def sub(num1, num2):
  return num1 - num2


def multiply(num1, num2):
  return num1 * num2


def divide(num1, num2):
  return num1 / num2


operators = {'+': sum, '-': sub, '*': multiply, '/': divide}


def calculator():
  f_num = float(input("Enter the number : "))
  while True:
    for sig in operators:
      print(sig)

    oper = input("pick the operators ")
    if oper not in operators:
      print('\nSyntax error')
      exit()
    s_num = float(input('\nEnter the second number : '))

    calc = operators[oper]
    answer = calc(f_num, s_num)
    print(answer)
    if input('\nWant to continue type y or want to quit type n : ') == 'y':
      f_num = answer
    else:
      print(f"\nThe answer is {answer}")
      break


calculator()
