#1
# digits = []
# for i in range(5):
#     digit = input(f"Enter a digit:{ i }")
#     digits.append(digit)
# print(digits)

#2
# A = [1, 2, 3, 4, 5]
# A.remove(5)
# print(A)

#3
# A = []
# for i in range(10):
#     digit = input(f"Enter a digit:{ i }")
#     A.append(digit)
# N = []
# for i in range(1):
#     digit = input(f"Enter a digit:{ i }")
#     N.append(digit)
# Res = [x for x in A if x in N]
# Count = {Res.count(i) for i in Res}
# print(Count)

#4
# A = []
# for i in range(10):
#     digit = input(f"Enter a digit:{ i }")
#     A.append(digit)
# print(A[::-1])

#5
# A = []
# C = []
# for i in range(5):
#     digit = int(input(f"Enter a digit:{ i }"))
#     A.append(digit)
# for i in A:
#     if i > 5:
#         C.append(i)
# print(C)

#6
#
# A = float(input("Enter a digit"))
# minimum = A
# maximum = A
# for i in range(5):
#     A = float(input("Enter a digit"))
#     if A > maximum:
#         maximum = A
#     if A < maximum and A < minimum:
#         minimum = A
# print("minimum:",round(minimum,2),"maximum:",round(maximum,2))


#7
# text = str(input("Enter a text: "))
# num = [int(i) for i in text.split() if i.isdigit()]
# print(len(num))






