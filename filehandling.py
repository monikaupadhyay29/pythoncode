#creating file sample.txt write the some content into the file
# file=open("sample.txt","w")
# content="hello world\nvisual studio code\npython programming\nsoftware developer"
# print(file.write(content))
# file.close()


# file=open("sample.txt","r")
# # print(file.read(3)) #file reading upto 3rd index
# print(file.readlines()) #read files content


#open file and apppend some data into file
# file=open("sample.txt","a")
# print(file.write("i am appending"))


#copy data from one file to another
# file=open("oldfile.txt","r")
# data=file.read()
# # print(data)
# file.close()


# file=open("copy.txt","w")
# print(file.write(data))
# file.close()


#rename old file name to new file name\
import os
oldname="oldfile.txt"
newname="rename_old.txt"

with open(oldname) as f:
    content=f.read()

with open(newname,"w") as f:
    print(f.write(content))

os.remove(oldname)
