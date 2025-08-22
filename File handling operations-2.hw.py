with open('sample_doc.txt','w') as file:
    file.write("Hi! I am Nusrat Tasnim Sayeema.\n I am 16 yrs old.\n I am a student & I read in class 10.\n I am studying from science group." \
    "\nMy favourite hobby is reading books.")
file.close()
#split file into words
with open('sample_doc.txt','r') as file:
    data=file.readlines()
    print("Words in this file are.....")
    for line in data:
        word=line.split()
        print(word)
file.close()
import os
print("Checking if My_file exists or not")
if os.path.exists("My_file.txt"):
    print("The file already exists.Deleting the file........")
    os.remove('My_file.txt')
else:
    print('The file does not exist.Creating the file........')
    my_file=open('My_file.txt','w')
    my_file.write("sample_doc.txt")
    my_file.close()
os.remove('sample_doc.txt')