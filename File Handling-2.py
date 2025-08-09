file=open('codingal.txt','r')
Counter=0
Content=file.read()
CoList=Content.split("\n")
for i in CoList:
    if i:
        Counter+=1
print("This is the number of lines in the file_")
print(Counter)

#appending contents of 2 or more files 
file1=input("Enter the name of first file: ")
file2=input("Enter the name of second file: ")
f1=open('file1','a+')
f2=open('file2','r')
f1.write(f2.read())
f1=open('file1','r')
f2=open('file2','r')
print(f1)
print(f2)
f1.close()
f2.close()