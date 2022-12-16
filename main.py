#If the bill was $150.00, split between 5 people, with 12% tip. 

print ("Welcome to the tip calculator.")
total = int(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total_people = int(input("How many people to split the bill? "))
pay = (total/total_people) * ( (percentage/100) + 1)
# pay = round(pay, 2) --> can use round function
#print("Each person should pay: $%.2f" %pay) --> another way to print 2 decimal places
pay = "{:.2f}".format(pay)
print(f"Each person should pay: ${pay}")



