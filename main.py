##Simple Program
#Name: ____

## Create a Simple Program that does the following.

#1. Asks the user a skill question and compares their guess to the answer.   Use a loop to get the user to guess until correct.


#2. Write a function that takes a word and a number 'n'. Print the word out 'n' times. 
#ex. "Hello"  3 = "HelloHelloHello"


'''while True:
  s = input('What is my favourie color?')
  if s == "blue":
    print("Yes")
    break'''

s,n = input().split(' ')
n = int(n)
print(3*s)
