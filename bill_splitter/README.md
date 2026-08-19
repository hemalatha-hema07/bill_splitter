Bill Splitting Calculator
Overview

Bill Splitting Calculator is a simple Python command-line application that calculates the total bill, tip amount, and the amount each person needs to pay when a bill is shared among multiple people.

The program also validates the user's input to prevent negative bill amounts, negative tip percentages, and invalid numbers of people.

Features
Enter the bill amount
Enter the tip percentage
Enter the number of people
Calculate the tip amount
Calculate the total bill including tip
Calculate the amount each person should pay
Validate user input
Display a formatted bill summary
Technologies Used
Python 3
Command Line / Terminal
Concepts Practiced

This project helps practice:

input() and print()
Variables
Data types (float, int)
Type conversion
if, elif, and else
Arithmetic operations
Input validation
f-strings
Number formatting
Project Structure
bill-splitting-calculator/
│
├── main.py
└── README.md
How to Run

Make sure Python is installed on your system.

Open the terminal in the project directory and run:

python main.py
Example
=== Bill Splitting Calculator ===

Enter the bill amount: ₹1000
Enter tip percentage: 10
Enter number of people: 4

----- Bill Summary -----
Original bill: ₹1000.00
Tip: ₹100.00
Total bill: ₹1100.00
People: 4
Each person pays: ₹275.00
Input Validation

The program checks for invalid values:

Bill amount cannot be negative.
Tip percentage cannot be negative.
Number of people must be greater than 0.

Example:

Enter the bill amount: ₹-500

Bill amount cannot be negative.
Calculation

The program uses the following formulas:

Tip = Bill × Tip Percentage / 100

Total Bill = Bill + Tip

Amount Per Person = Total Bill / Number of People
Future Improvements

Possible improvements include:

Add currency selection
Allow different tip amounts for each person
Add a graphical user interface
Handle invalid text input using try-except
Add an option to calculate another bill without restarting the program