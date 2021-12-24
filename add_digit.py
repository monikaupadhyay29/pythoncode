#usage: Program to add the digits of a number

#taking users input num
num=int(input("Enter a number"))

#initialize add
add=0

#use while loop to execute block of code repeatedly until condition statisfied
while(num>0):
    rem=num%10
    add=add+rem
    num=num//10

# display result add
print("Add the digits of the number:",add)





















# while (num!=0):
#     rem=num%10
#     add=add+rem
#     num=num/10
# print("Add digits of a number:",add)