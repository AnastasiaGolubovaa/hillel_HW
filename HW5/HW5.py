# 1)
N =5
for i in range(N + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")

#2
N = 5
myList = []
for i in range(1, N + 1):
    myList.append("*" * i)
print("\n".join(myList))


#OR

N = 5
for i in range(0, N):
    for j in range(0, i + 1):
        print("* ", end="")
    print()

# Задание со звездочкой:

#3
N = 5
for i in range(0, N):
    for j in range(0, i):
        print(' ', end=' ')
    for j in range(0, N - i):
        print('*', end=' ')
    print('')
print()

# 4

N = 5
for i in range(1, N + 1):
	print(" " * (N - i) +"*" * i)

