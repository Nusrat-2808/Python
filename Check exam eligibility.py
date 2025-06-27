presence=int(input("Enter no. of the days you were present=>"))
working_days=185
attendance=(presence*100)/working_days
print(f"Your attendance in percentage: {attendance}%")
if attendance>=75:
    print("You are eligible for giving exam!")
else:
    health=str(input("Did you have any health complications?"))
    if health=="Yes":
        print("You can attend the exam as you were sick.")
    else:
        print("You cannot sit in the exam!")