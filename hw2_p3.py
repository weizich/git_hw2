print("Welcome to the simple calculator program!")
first_number=int(input("Enter the first number:"))
second_number=int(input("Enter the second number:"))
operation=str(input("Select an arithmetic operation(+,,-,*,/):"))
if operation=="+":
	print("Result:",first_number+second_number)
elif operation=="-":
	print("Result:",first_number-second_number)
elif operation=="*":
	print("Result:",first_number*second_number)
elif operation=="/":
	print("Result:",first_number/second_number)
yn=str(input("Do you want to perform another calculation?(yes or no):"))
while yn=="yes":
	first_number=int(input("Enter the first number:"))
	second_number=int(input("Enter the second number:"))
	operation=str(input("Select an arithmetic operation(+,,-,*,/):"))
	if operation=="+":
		print("Result:",first_number+second_number)
	elif operation=="-":
		print("Result:",first_number-second_number)
	elif operation=="*":
		print("Result:",first_number*second_number)
	elif operation=="/":
		print("Result:",first_number/second_number)
	yn=str(input("Do you want to perform another calculation?(yes or no):"))
print("Goodbye!") 