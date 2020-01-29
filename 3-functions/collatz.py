def collatz(number):
    if(number % 2 == 0):
        print(number // 2)
        return number // 2
    else:
        print(number * 3 + 1)
        return number * 3 + 1

try:
    print('Enter an integer:')
    integer = int(input())

    while integer != 1:
        integer = collatz(integer)
except:
    print('Error: Please enter an integer')



