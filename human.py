class Human:
    isAlive = True
    heartBPM = 120
    class Personal:
        name = "Joe"
        age = 20
        gender = "Male"
        birthday = "1 April"
    def happy(self):
        print("HAPPY BIRTHDAY!!")
human = Human()
personal = Human().Personal()
print(human.isAlive)
print(human.heartBPM)
print(personal.name)
print(personal.age)
print(personal.birthday)
human.happy()
