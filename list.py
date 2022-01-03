#create a list
ls=["apple","banana","grapes","pineapple","cherry"]
# print(ls)

#get elements of the list 
# for i in ls:
#     print(i)


#List allow duplicates
# ls=["apple","banana","grapes","pineapple","cherry","apple"]
# print(ls)

#length of list
# print(len(ls))

#List items are indexed and you can access them by referring to the index number
# print(ls[4])

#Negative indexing
# print(ls[-4])

#range of indexes
# print(ls[2:4])
# print(ls[-4:-2])

#change item value
# ls[4]="Strawberry"
# print(ls)

#insert items index wise
# ls.insert(5,"Strawberry")
# print(ls)

#To add an item to the end of the list, use the append() method
# ls.append("watermelon")
# print(ls)

#To append elements from another list to the current list, use the extend() method
newls=["Mango","Jamun"]
ls.extend(newls)
# print(ls)

#Loop through the index number
# for i in range(len(ls)):
#     print(ls[i])


# j=0
# while j<len(ls):
#     print(ls[j])
#     j=j+1

#sorting list
# ls.sort()
# print(ls)

#reverse the list
# ls.reverse()
# print(ls)

#copy list
# copy=ls.copy()
# print(copy)

#methods
#insert new items index wise
ls.insert(2,"watermelon")
# print(ls)

#get index 
# op=ls.index("cherry")
# print(op)

# print(ls.count("apple"))
ls.remove("cherry")
# print(ls)

print(ls.count("cherry"))
