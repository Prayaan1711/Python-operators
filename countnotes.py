amount = int(input("Enter a 4 digit number: "))

note1 = amount//500
note2 = (amount%500)//100
note3 = ((amount%500)%100)//50
note4 = (((amount%500)%100)%50)//10
note5 = ((((amount%500)%100)%50)%10)//1

print("Notes of Rs.500 :", note1)
print("Notes of Rs.100 :", note2)
print("Notes of Rs.50 :", note3)
print("Notes of Rs.10 :", note4)
print("Notes of Rs.1 :", note5)
