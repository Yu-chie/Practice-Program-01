#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)

#Define the range, Loop through numbers 0 to 100
for num in range(0, 101):
    if num % 2 != 0:            #Check if number is even
        print(num)              #Print all even numbers
        