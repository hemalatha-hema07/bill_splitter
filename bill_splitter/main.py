print("=== Bill Splitting Calculator ===")

bill = float(input("Enter the bill amount: ₹"))
tip_percent = float(input("Enter tip percentage: "))
people = int(input("Enter number of people: "))

if bill < 0:
    print("Bill amount cannot be negative.")

elif tip_percent < 0:
    print("Tip percentage cannot be negative.")

elif people <= 0:
    print("Number of people must be greater than 0.")

else:
    tip = bill * tip_percent / 100
    total_bill = bill + tip
    amount_per_person = total_bill / people

    print()
    print("----- Bill Summary -----")
    print(f"Original bill: ₹{bill:.2f}")
    print(f"Tip: ₹{tip:.2f}")
    print(f"Total bill: ₹{total_bill:.2f}")
    print(f"People: {people}")
    print(f"Each person pays: ₹{amount_per_person:.2f}")
    print("------------------------")
    print("Thank you for using the Bill Splitting Calculator!")