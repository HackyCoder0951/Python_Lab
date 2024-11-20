# checking for type of data
a = 5;
print("the type of a",type(a));

b = 40.5;
print("the type of b",type(b));

c = 1+3.5j;
print("the type of c",type(c));

print(" c is a complex number : ", isinstance(c,complex))  


per = 85.75
print("score:{:.2f}%".format(per))


str = "string using double quotes"
print(str)
s = '''A multiline
string'''
print(s)


n = int(input("enter the number of rows"))
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    print()
