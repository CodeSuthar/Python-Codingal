num = 1
sum = 0
till = int(input("Enter a number: "))

while num <= till:
    sum += num
    num += 1
    
print(f"The sum of numbers from 1 to {till} is {sum}")