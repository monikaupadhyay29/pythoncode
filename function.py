def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

p=fact(5)
print(p)


def func(name):
    f=name.upper()
    print(f)

# print(func("rani"))
#Default Arguments
def myfunc(x,y=18):
    print("x is:",x)
    print("y is:",y)
    

# d=myfunc(7)
# print(d)


#keyword Arguments
# def myfun(n1,n2):
#     empls=[]
#     empls.append(n1)
#     empls.append(n2)
#     return empls

# print(myfun(1,22))


def fun(*num):
    empls=[]
    for i in num:
        print(i)
        
fun(11,22,68,65,34)
