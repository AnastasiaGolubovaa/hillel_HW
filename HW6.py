#1)
# word = str(input("Enter a word: "))
# if word == word[::-1]:
#  print("+")
# else:
#     print("-")

#2
#
# def WordPresent(sentence, word):
#     text = sentence.split(" ")
#     for i in text:
#         if (i == word):
#             return True
#     return False
# text = str(input("Enter a text: "))
# word = str(input("Enter a word: "))
# if (WordPresent(text, word)):
#     print("YES")
# else:
#     print("NO")

#3)
# text = str(input("Enter a text: "))
# if text.startswith("abc"):
#     print(text.replace("abc", "www"))
# else:
#     print(text + "zzz")

#4
# text = str(input("Enter a text: "))
# changed = ''.join([x for x in text if not x.isdigit()])
# print(changed)


#5)
# mail = input("Enter a mail: ")
# if mail.find("@") and mail.find(".") == -1:
#     print("NO")
# else:print("YES")
