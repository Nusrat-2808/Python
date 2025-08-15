file=open('code.txt','r')
print("\nRead in parts\n")
print(file.read(54))
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readlines())
file.close()
file1=open('code.txt','r')
for line in file1.readlines():
    if not (line.startswith('T')):
        print(line)
cont=file1.readlines()
type(cont)
for i in range(1,len(cont)+1):
    if(i%2==0):
        print(cont[i-1])
    else:
        pass
file1.close()