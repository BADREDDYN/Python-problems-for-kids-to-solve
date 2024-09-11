#2. Even or Odd
#Write a program that takes a number as input and prints whether the number is even or odd.


number = int(input("Number : "))


if(number%2 == 0) :
    print(number, "is even.")
else :
    print(number, "is odd.")