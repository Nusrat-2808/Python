doc=open("Student_record.txt","w")
doc.write("**This is the Student record of CLASS X**\n")
doc.write("Student-1:\n" \
"Name:Zawata Afnan Zenith\nClass:X-B1\nRoll:01\nBrief Introduction:She is a very good student with good manners,zeal,attentiveness & result.But she is often absent & is involved in most events like debate,anchoring,poetry recitation.\n" \
"Favourite subject:English-2\n")
doc.write("Student-2:\n" \
"Name:Nusrat Tasnim Sayeema\nClass:X-B1\nRoll:02\nBrief Introduction:She is a very good student with good manners,zeal,attitude & result.She has complete attendance& never inattentive in class. She is involved in most events like volunteering,dance,poetry recitation.\n" \
"Favourite subject:Physics,Higher Mathematics\n")
doc.write("Student-3:\n" \
"Name:Tathoi Bishwas\nClass:X-B1\nRoll:09\nBrief Introduction:She is a good student with good manners,zeal & result.She mostly slacks off classes and remain absent & is involved in most events like dancing,drama & poetry recitation.She is never attentive in class & disturbs others a lot.\n" \
"Favourite subject:None except Dancing & sleeping\n")
doc.close()
Motive=input("What do you want to do today?")
if Motive=="Read":
    doc=open("Student_record.txt","r")
    print(doc.read())
elif Motive=="Overwrite":
    doc=open("Student_record.txt","w")
    text=input("Enter the whole rewritten record:")
    doc.write(text)
elif Motive=="Add":
    doc=open("Student_record.txt","a")
    text=input("Enter the part you want to add")
    doc.write(text)
else:
    print("Invalid Command!")