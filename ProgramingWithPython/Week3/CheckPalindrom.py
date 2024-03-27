

def Palindrome(word):
    wordList = []
    reverseList = []
    for i in range(len(word)):
        wordList.append(word[i]) 
    reverseList.extend(wordList.reverse())
    for x in range(len(wordList)):
        if wordList[x] == reverseList[x]:
            print("it's a plaindrom number")
        else:
            print("not plaindrome!")
    print(wordList)
    print(reverseList)
      
Palindrome('book')
  