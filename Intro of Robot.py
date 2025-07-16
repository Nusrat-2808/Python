class robot:
    def __init__(self,name,robot_type,function):
        self.name=name
        self.type=robot_type
        self.function=function
        print("Hello! I am a robot")
    def intro(self):
        print(f"🤖My name is {self.name}.")
        print(f"🛠️Type: {self.type}")
        print(f"📌Usability: {self.function}")
        print('*/*'*45)
# Creating different robot instances
robot1 = robot("RoboHelper", "Service Robot", "Assist humans in daily household tasks")
robot2 = robot("MediBot", "Medical Robot", "Help doctors in surgeries and patient monitoring")
robot3 = robot("EduBot", "Educational Robot", "Teach programming and STEM subjects to students")
robot4 = robot("AgriDroid", "Agricultural Robot", "Monitor crops and assist in smart farming")

# Introducing all robots
robot1.intro()
robot2.intro()
robot3.intro()
robot4.intro()
