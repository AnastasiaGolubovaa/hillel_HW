#1
file = open('numbers1.txt', 'r')
content = file.readlines()
numbers = []
for line in content:
	for i in line:
		if i.isdigit() == True:
			numbers.append(i)
print(numbers)

#2
text = input("Enter your text: ")
open("text2.txt", "w").write(text)

#3
n_number = input("Enter number of digits:")
if not n_number.isdigit():
    raise ValueError("It is not a number!")
file = open("numbers.txt", "a")

for i in range(int(n_number)):
    line = input("Enter number:")
    file .write(line + ",")


#4
import random
file = open("random_numbers.txt", "w" )

for i in range(100):
    line = str(random.randint(1, 100))
    file.write(line + "\n")
    print(line)

file.close()
file = open("random_numbers.txt", "r")
print(file.read())
file.close()

#5
import re
with open("text1.txt", "r") as data:
    data = data.read()

all_words = r"[a-zA-Z]+\'?[a-zA-Z]*"
words = re.findall(all_words, data)
letters = re.findall(r'[a-zA-Z]', data)
pattern = "[~`@#$%^&*(_)+{}|/\.,<>?-]"
spl_symbols = re.findall(pattern, data)
summa = len(words)
print(summa)

#6
sum = 0
with open("numbers2.txt") as line:
	for i in line:
		i = i.strip()
		space = i.split(" ")
		for ns in space:
			sum = sum + int(ns)
print(sum)


#7
file = open("text2.txt").read().lower().split()

top = []
for word in file:
  if word not in top:
    top.append(word)

counts = []
for unique in top:
  count = 0
  for word in file:
    if word == unique:
      count += 1
  counts.append((count, unique))

counts.sort()
counts.reverse()

for i in range(min(5, len(counts))):
  count, word = counts[i]
  print("%s %d" % (word, count))
