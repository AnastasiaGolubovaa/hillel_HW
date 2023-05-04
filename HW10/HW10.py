#1
def change(lst):
   n = len(lst)
   temp = lst[0]
   lst[0] = lst[n - 1]
   lst[n - 1] = temp
   return lst
list = [1, 102, 5, 9, 5, 2]

print(list)
print(change(list))
#
#2
def to_dict(lst):
   return {elem: elem for elem in lst}
print(to_dict([1, 2, 3, 4, 5]))
print(to_dict(['sun', (1, 2), 99.9, -100]))
#

#3

def sum_range(start, end):
   if start < end:
      return sum(range(start, end + 1))
   else:
      return sum(range(end, start + 1))

print(sum_range(1, 2))
print(sum_range(3, 2))


#4
def read_last(lines, file):
   if lines > 0:
      with open(file, encoding='utf-8') as text:
         file_lines = text.readlines()[-lines:]
      for line in file_lines:
         print(line.strip())


read_last(3, 'hw10.txt')
read_last(2, 'hw10.txt')
read_last(1, 'hw10.txt')