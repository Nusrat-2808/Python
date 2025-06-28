num=int(input("Enter the number that is to be checked==>"))
word=str(num)
length=len(word)
print(length)
i=0
sum=0
while(i<length):
    a=int(word[i])
    x=a**length
    sum=sum+x
    i=i+1
if sum==num:
    print("Voila! It is an armstrong number!")
else:
    print("Oops!The number is not an armstrong number!")