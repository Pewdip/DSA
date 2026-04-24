#square pattern 
#12345
#12345
#12345
#12345
#12345
# input= int(input("Enter a number: "))
# for j in range(input):
#     for i in range(1,input+1):
#          print(i,end=" ")
#     print()

#square pattern 
#123
#456
#789
#num is used to print numbers in row and incremented by 1 
# input = int(input("Enter a number: "))
# num=1
# for i in range(input):
#     for h in range(input):
#         print(num,end="")
#         num+=1
#     print()

# triangle pattern 
# *
# **
# ***
# ****
# input = int(input("Enter a number: "))
# for i in range(input):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

#traingle patttern 
#1
#12
#123
#1234
# input = int(input("Enter a number: "))
# for i in range(input):
#     for j in range(i+1):
#         print(j+1,end=" ")
#     print()

#traingle patttern 
#1
#22
#333
#4444
# inputnum = int(input("Enter a number: "))
# for i in range(inputnum):
#     for j in range(i+1):
#         print(i+1,end="")
#     print()

#Reverse triangle pattern 
#*****
#****
#***
#**
#*
# inp = int(input("Enter a number: "))
# for i in range(inp):
#     for j in range(inp-i):
#         print("*",end="")
#     print()

#Reverse triangle pattern 
#1
#21
#321
#4321
# inp = int(input("Enter a number: "))
# for i in range(inp):
#     for j in range(i+1):
#         print(i-j+1,end="")
#     print()

#Floyd's Triangle pattern
#1
#23
#456
# num=1
# input1= int(input("Enter a number: "))
# for i in range(input1):
#     for j in range(i+1):
#         print(num,end=" ")
#         num+=1
#     print()

#Floyd's Triangle pattern for alphabets 
#a
#bc
# input1= int(input("Enter a number: "))
# num=97
# for i in range(input1):
#     for j in range(i+1):
#         print(chr(num),end=" ")
#         num+=1
#     print()

#inverted triangle pattern 
#1111
# 222
#  33
#   4
# n=int(input("Enter a number: "))
# for i in range(n):
#     for j in range(i):
#         print(" ",end="")
#     for k in range(n-i):
#         print(i+1,end="")
#     print()

# for i in range(n):
#     print(" " * (n-i-1) + str(i+1) * (i+1))
# for i in range(n):
#     print(str(i+1) * (n-i))

# n=int(input("Enter a number: "))
# for i in range(n):
#     print(str(i+1) * (n-i))
# for i in range(n):
#     print(" " * (n-i-1)+ str(i+1)*(i+1))
#last statement 