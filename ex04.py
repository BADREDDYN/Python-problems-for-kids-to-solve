#4. Multiplication Table
#Write a program that asks for a number and prints the multiplication table for that number.


number = int(input("Give a number: "))


for i in range(1, 11) :
    print(number, "*", i, "=", number * i)

