# print("hello world")

# create Base class company
class company:
    cmp_name="XYZ"
    # create function info
    def info(self):
        print("Company name:",self.cmp_name)

# create derived class employee
class employee(company):
    emp_name="Rahul"
    def detail(self):
        print("Employee name:",self.emp_name)

    

# obj=employee()
# obj.info()
# obj.detail()



class student:
    def __init__(self,id,name):
        self.id=id
        self.name=name

    def stud_info(self):
        print("student id:",self.id)
        print("student name:",self.name)

# s=student(23,"Ram")
# print(s)



class calculation1:
    def addition(self,x,y):
        print("Addition")
        return x+y
    
class calculation2:
    def subtraction(self,p,q):
        print("Subtraction")
        return p-q

class calculation3(calculation1,calculation2):
    def multiplication(self,h,j):
        print("Multiplication")
        return h*j

    def simple_interest(self,j,k,l):
        print("Simple Interest")
        SI=(j*k*l/100)
        return SI


# obj=calculation3()
# print(obj.addition(22,33))
# print(obj.subtraction(50,24))
# print(obj.multiplication(12,2))
# print(obj.simple_interest(100,5,6))
