#Method overiding
#create class cmp
# class cmp:
#     def info(self):
#         print("cmp method")


# class emp(cmp):
#     def info(self):
#         print("emp method")


# p=emp()
# p.info()


# class A:
#     def cal(self):
#         print("A method")

# class B(A):
#     def cal(self):
#         super().cal()
#         print("B method")

# d=B()
# d.cal()


class books:
    def cal(self):
        print("Books method")

class books2(books):
    def cal(self):
        super().cal()
        print("Books2 method")


g=books2()
g.cal()