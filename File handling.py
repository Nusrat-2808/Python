file=open('codingal.txt','r')
print(file.read())
file.close()

file_write=open('codingal.txt','w')
file_write.write("File in write mode \n Hi! I'm Sayeema. I'm 17 years old.")
file_write.close()

file_append=open('codingal.txt','a')
file_append.write("File in append mode...\n I'm studying in science group.")
file_append.close()

