math = int(input("Enter your marks in math: "))
science = int(input("Enter your marks in science: "))
English = int(input("Enter your marks in English: "))
Hindi = int(input("Enter your marks in hindi: "))
Infotech = int(input("Enter your marks in IT: "))

sum = (math + science + English + Hindi + Infotech)
perc = (sum/500)*100

print("Your percentage is ", perc)

