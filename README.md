Simple Python Calculator 🖩
Overview
This is a basic Python calculator that allows users to perform four arithmetic operations:
➕ Addition (+)
➖ Subtraction (-)
✖️ Multiplication (*)
➗ Division (/)

The program ensures valid operator input, prevents division by zero, and organizes functions modularly for clean and reusable code.

How It Works
1️⃣ The user enters the first number.
2️⃣ The program asks for an operation symbol (+, -, *, /) and keeps asking until a valid one is entered.
3️⃣ The user enters the second number.
4️⃣ The program performs the calculation and displays the result.

Code Breakdown
add(num1, num2) – Adds two numbers and returns the result.
sub(num1, num2) – Subtracts the second number from the first.
mult(num1, num2) – Multiplies two numbers.
div(num1, num2) – Divides the first number by the second (with zero-checking).
get_opp() – Ensures the user enters a valid operator (+, -, *, /). If not, it keeps asking.
Error Handling
⚠️ Invalid Operator Handling – If the user enters something other than +, -, *, /, they are prompted again.

⚠️ Division by Zero Prevention – If the user tries to divide by zero, they get an error message:
"Error: Division by 0 is undefined."
