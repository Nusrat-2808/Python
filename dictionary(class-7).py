#empty dictionary
my_dict={}
#Inputing values(mixed keys)
my_dict={"name":"Sayeema","age":16,"fav-subjects":["Math","Physics","Higher math"],"Profession":"Student","class":"X"}
print(my_dict["name"])
print(my_dict.get("fav-subjects"))
#Update value
my_dict["age"]=17
print(my_dict)
#add value
my_dict["Address"]="Dhaka"
print(my_dict)
#remove element
my_dict.pop("class")
print(my_dict)
#access a particular element
print("Address: ",my_dict.get("Address"))
my_dict.clear()
print(my_dict)