# # class demo:
# #     val=10

# # s=demo()
# # print(s.val)


# # class Person:
# #     def __init__(self,name,age):
# #         self.name=name
# #         self.age=age


# # p1=Person("Jonny",23)

# # print(p1.name)
# # print(p1.age)



# #create class employee
# class employee:
#     #create function & initialized value to object
#     def __init__(self,empid,empname):
#         self.empid=empid
#         self.empname=empname

#     def display(self):
#         print("Employee ID:",self.empid)
#         print("Employee name:",self.empname)


# #creating class employee object
# obj=employee(102,"Rahul")
# obj.display()
    
#create class books
class Books:
    def __init__(self,name,author):
        self.name=name
        self.author=author

    #use the Books class to create an object and then execute the print methods
    def print(self):
        print("Book Name:",self.name)
        print("Book Author:",self.author)


obj=Books("Making of new india","Mr.A")
obj.print()