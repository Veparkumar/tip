#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("welcome to the tip calaulator")
bill = float(input("What was the total bill :"))
tip = int(input("what persentage tip wold you like to give. 10, 12, or  15"))
people = int(input("how many people to split the bill :"))
tip_as_paersun = tip / 100
total_tip_amount = bill * tip_as_paersun
total_bill = bill + total_tip_amount
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
print(f"each person should pay  : {final_amount}")
