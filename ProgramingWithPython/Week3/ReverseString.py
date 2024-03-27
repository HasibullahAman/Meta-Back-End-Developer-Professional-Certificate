# word ="Hasib"
# # newWord = word[::-1]
# # print(newWord)



# def Reverse(word):
#     if len(word) == 0:
#         return word
#     else:
#         return Reverse(word[1:]) + word[0]
    
    
# print(Reverse(word))
 
# a = [[96], [69]]

# print(''.join(list(map(str, a))))


# some = ["aaa", "bbb"]

# # #1
# # def aa(some):
# #    return


# #3
# def aa():
#    return

# # #4
# # def aa():
# #    return "aaa"
# # aa(6)
# aa()

numbers = [15, 30, 47, 82, 95]
def lesser(numbers):
   return numbers < 50

small = list(filter(lesser, numbers))
print(small)