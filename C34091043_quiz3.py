#歡迎使用者
print("Welcome to the simple calculator program!")
#選第一個數字
first_number=int(input("Enter the first number:"))
#選第二個數字
second_number=int(input("Enter the second number:"))
#選運算符號
arithmetic=str(input("Select an arithmetic operation(+,-,*./):"))
if arithmetic == '+':
    print(first_number+second_number)
elif arithmetic == '-':
    print(first_number-second_number)
elif arithmetic == '*':
	print(first_number*second_number)
elif arithmetic == '/':
    print(first_number/second_number)
answer=str(input("Do you want to perform another calculation?(yes or no):"))
#若答案為yes則再做一次，否則跳出迴圈
while answer=='yes':
    first_number=int(input("Enter the first number:"))
    second_number=int(input("Enter the second number:"))
    arithmetic=str(input("Select an arithmetic operation(+,-,*./):"))
    if arithmetic == '+':
        print(first_number+second_number)
    elif arithmetic == '-':
        print(first_number-second_number)
    elif arithmetic == '*':
	    print(first_number*second_number)
    elif arithmetic == '/':
        print(first_number/second_number)
    answer=str(input("Do you want to perform another calculation?(yes or no):"))
print("Goodbye!")