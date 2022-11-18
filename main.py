#1

a = int(input("Enter first number a: "))
b = int(input("Enter second number b:"))
c = int(input("Enter third number c:"))

if a > 10 and b > 10 and c > 10 and a%3 ==0 and b%3 ==0:
    print("yes")
else:
    print("no")

#2

a = int(input("Enter first number a: "))
b = int(input("Enter second number b:"))
c = int(input("Enter third number c:"))
x = int(max(a, b, c))
print(x)

#Задания со звездочкой:

number = int(input("Enter a three-digit number:"))
a = str(number // 100)
b = str(number % 100 // 10)
c = str(number % 10)
print(c + b + a)
reversed_number = (c + b + a)




