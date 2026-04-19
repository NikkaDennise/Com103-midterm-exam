Student_name=input("Please enter name: ")
while Student_name == "":
    print("Invalid")
    Student_name=input("Please enter name: ")

Weekly_budget=input("Please Enter your Weekly Budget:  ")
while not Weekly_budget.isdigit():
    print("Invalid")
    Weekly_budget=input("Please Enter your Weekly Budget:  ")
   
Weekly_budget=float(Weekly_budget)
categories = [
    ["Food & Drinks", "Lunch, snacks, coffee"],
    ["Transportation", "Bus, jeepney, ride-share"],
    ["Mobile / Internet", "Load, data plan, WiFi top-up"],
    ["School Supplies", "Notebook, pen, bond paper"],
    ["Entertainment", "Games, movies, hangout"]
]


print("="* 30)
print("WEEKLY EXPENSE -- CATEGORIES")
print("="* 30)
for item in range(len(categories)):
    print(str(item + 1) + ". " + str(categories[item][0]) + str(categories[item][1]))
print("="*30)

expense_list=[]
total_expense=0

for item in range(4):
    print("\n-- EXPENSE" + str(item + 1))
    category_choice=input("Enter your Category (1-5) and 0 to skipped: ")
    while category_choice == "" or not category_choice.isdigit():
        print("Invalid")
        category_choice=input("Enter your Category (1-5) and 0 to skipped: ")
   
    category_choice=int(category_choice)
   
    if category_choice == 0:
        continue
    elif category_choice >=1 and category_choice <=4:
        description=input("Enter Description: ")
        amount=input("Enter amount: ")
        while not amount.isdigit():
            print("Invalid")
            amount=input("Enter amount")
        amount=float(amount)
        total=(amount/Weekly_budget)*100
        category_choice=int(category_choice)
        if total > 25:
            print("High Expense Alert!")
            total_expense+=amount
            label="High Expense Alert!"
           
        else:
            total_expense+=amount
            label=""
           
        expense_list.append([categories[category_choice -1][0], description,amount,label])
       
    else:
        print("Invalid")
   
remaining_money= float(Weekly_budget) - float(total_expense)

print()
print("=" * 30)
print(Student_name + " -- WEEKLY EXPENSES LOG")
print("=" * 30)
print("Weekly Budget: " + "P" + str(Weekly_budget))
for item in range(len(expense_list)):
    print(str(item+1) + ". " + str(expense_list[item][0]))
    print(str(expense_list[item][1]) + " " + str(expense_list[item][2]) + " " +str(expense_list[item][3]))
print("="* 30)
print("Total spend: " + "P" + str(total_expense))
print("Remaining: " + "P" + str(remaining_money))

if remaining_money >= 0:
    print("Status: Budget OK! Keep it up.")
else:
    print("Status: Overspent! Reduce spending.")
