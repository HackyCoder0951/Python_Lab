# Q.2 A text file “PYTHON.TXT” contains alphanumeric text. 
# Write a program that reads this text file and writes to another file “PYTHON1.TXT” entire file 
# except the numbers or digits in the file.

def file_Written():
    with open("python.txt","r") as file2, open("python1.txt","w") as file3:
            for i in file2:
                for char in i:
                    if not char.isnumeric():
                        file3.write(char)

with open("python1.txt", "r") as file:
    print(file.read())