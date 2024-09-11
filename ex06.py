#6. Simple Calculator
#Write a program that asks the user to input two numbers and an operator (+, -, *, /). The program should perform the correct calculation and display the result.

n1 = int(input("Number 1: "))

n2 = int(input("Number 2: "))

op = input("Operator(+, -, *, /) : ")

if op == "+" :
    print(n1, "+", n2, "=", n1+n2)
elif op == "-" :
    print(n1, "-", n2, "=", n1-n2)
elif op == "*" :
    print(n1, "*", n2, "=", n1*n2)
elif op == "/" :
    print(n1, "/", n2, "=", n1/n2)
else :
    print("Wrong operator, try again!")
    