name = input("Please enter Your name: ")  #input read only string

print(name);

#=================================================
num1=input("Please enter the first number:")
num2=input("Please enter the second number:")
print((int(num1)+int(num2)))

#=================================================
message =""

while message != "valera":
    message = input("Enter my name:)  ")
    if message == "valera":
        print( " yes, "+message+" is my name")
        break

print(message + " is not my name")

#====================================================

mytext= []
msg = ""

while msg != "stop".upper():
    msg = input("Enter new item, and STOP to finish")
    mytext.append(msg)

print(mytext)