## TO COUNT AN ELEMENT OCCURS HOW MANY TIMES....

# Counting a number.
print("Enter Elements:")
A = list(map(int,input().split()))
k = int(input("Enter number to count::"))
print(A.count(k))

#Counting a word.
print("Enter String:\n")
str = list(map(str,input().split(' ')))
a = input("Enter a word to count::")
print(str.count(a))