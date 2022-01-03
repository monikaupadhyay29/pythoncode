# Create dictionary\

dict={
    "name":"Rahul",
    "contact":9864536721,
    "address":"Kalyan"
}

print(dict)

# printing keys of dict
print(dict.keys())

#printing values of dict
print(dict.values())

#printing specific keys value
print(dict["address"])

#get method
p=dict.get("name")
# print(p)

#print items with key & value
# print(dict.items())


#updating dictionary
update_dict={
    "Position":"Student",
    "Friend":"Ram"
}

#updating dict
dict.update(update_dict)
# print(dict)

#updating keys & values
update_dict["Subject"]="Mathmatics"
# print(update_dict)

# print(dict)

#change the value of a specific item by referring to its key name
dict["contact"]=8754336573
print(dict)


#use loop
# for i in dict:
#     print(dict[i])

# for i in dict.values():
#     print(i)

for i in dict.keys():
    print(i)

for i in dict.items():
    print(i)