#1
# A = {"Borys", "Sasha"}                          #мена должников за Сентябрь
# B = {"Borys", "Sasha", "Mila", "Oleg", "Alex"}  #мена должников за Октябрь
#
# print(A.intersection(B))  #имена людей которые должны за Сентябрь и Октябрь
# print(B.difference(A))    # имена должников за Октябрь у которых нет долга за Сентябрь

#2
# correct_actions = {"W": "write", "R": "read", "X": "execute"}
# command = {}
#
# for i in range(int(input())):
# 	x = input().split()
# 	command[x[0]] = [correct_actions[i] for i in x[1:]]
# for i in range(int(input())):
# 	comm, n = input().split()
# 	print("OK" if comm in command[n] else "Access denied")
