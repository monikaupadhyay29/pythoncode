str="My Journey"
print(str[0]) #print chr index wise
print(str[0:3]) #print chr 0,1,2 index
print(str[1:4:1]) #print chr skip by 1
print(str[::])  #print whole string

#Loop through str
for i in str:
    print(i)

#Length of string
print(len(str))

#check My present in the str
print("My" in str)


#Negative indexing
print(str[-7:-2])

#modify string
print(str.upper())
print(str.lower())
print(str.replace("Journey","Ambitions"))
print(str.split(" "))

print(str.count("y"))