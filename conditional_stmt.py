# w=input("Enter a word:")
# rev=w[::-1]
# print(rev)

# i = 3
# j = 6
# while True:
#     if i < 5:
#         while j < 5:
#             print("inner loop",j)
#             j = j+1
#         # else:
#         #     print("inner loop")
        
#         print("outer loop",i)
#         i = i+1
#     else:
#         break




# x=1
# while x<=2:
#     print(x,"Outer loop")
#     y=6
#     while y<=2:
#         print(y,"inner loop")
#         y=y+1
#     x=x+1


# for i in range(1,10):
#     if i%2==0:
#         print(i,"number is even")
#     elif i%2!=0:
#         print(i,"number is prime")
#     else:
#         print("display")



def fact(ls):
    for i in range(ls):
        if i==0:
            return 
        else:
            return i*fact(i-1)


ls=[5,4,3,6,7]
fact(ls)







