numToCheck = input("Enter a number to check if it is armstrong or not: ")

if numToCheck.isdigit() == False:
    print("Please enter a valid number")
    exit()

numToCheck = int(numToCheck)

sum = 0

numLength = len(str(numToCheck))

temporary = numToCheck

while temporary > 0:
    digit = temporary % 10
    sum += digit ** numLength
    temporary //= 10

if numToCheck == sum:
    print("The number is an Armstrong number")
else: 
    print("The number is not an Armstrong number")