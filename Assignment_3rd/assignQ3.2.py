with open("python.txt","r") as pt:
    content = pt.read()
    print(content)

'''fileptr = open("./Assignment_3rd/file.txt","w")
fileptr.write("pythons is a programming langauge. that is a open source language also")
fileptr.close()'''

'''with open("./Assignment_3rd/file.txt","r") as pt:
    content = pt.read(10)
    print(type(content))
    print(content)'''

def file_Written():
    global fs
    with open("file.txt","r") as file2, open("file1.txt","w") as file3:
        if (file2 , file3):
            for i in file2:
                for char in i:
                    if not char.isnumeric():
                        file3.write(char)
        else:
            file2.read()
    return 

def print_file():
    file = open("file1.txt","r")
    return print(file)

'''file1 = open("./Assignment_3rd/file1.txt","x")
print(file1)
if file1:
    print("Files is created succetfully")'''
    

'''try:
    with open('./Assignment_3rd/.txt','w') as fl:
        fl.write("here we create new file")
except FileNotFoundError:
    print("the files doesn't exist")'''
    
'''file1 = open("./Assignment_3rd/file1.txt","r")
print("the filepointer is at byte :",file1.tell())
#content2 = file1.read()
#print("the filepointer is at byte :",file1.tell())'''

#import os
#os.rename("file_1.txt","file1.txt")

if __name__== "__main__":
    print(file_Written())