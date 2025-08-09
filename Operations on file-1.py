# #project 1
# #open file & read its content
# file=open('code.txt','r')
# print(file.read())
# file.close()
# #open file & read its beginning characters
# file=open('code.txt','r')
# print("\nRead in parts\n")
# print(file.read(8))
# #reading lines
# print(file.readline())
# print(file.readline())
# print(file.readline())
# #read all lines
# print(file.readlines())
# file.close()
# #append your name & age 
# file=open('code.txt','a')
# file.write("Hi! I am Sayeema & I am 17 years old.")
# file.close()
# #project2
# file1=open('code.txt')
# file2=open('CodingalUpdated.txt','w')
# for line in file1.readlines():
#     if not (line.startswith('Coding')):
#         print(line)
#         file2.write(line)
# file1.close()
# file2.close()
#project3
fn=open('code.txt','r')
fn1=open('CodingalUpdated.txt','w')
cont=fn.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if(i%2!=0):
        fn1.write(cont[i-1])
    else:
        pass
fn1.close()
fn1=open('CodingalUpdated.txt','r')
cont1=fn1.read()
print(cont1)
fn.close()
fn1.close()