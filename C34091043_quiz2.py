money=int(input("Enter the shopping amount:"))
level=str(input("Enter the membership level(Regular or Gold):"))
if level=="Regular":
    if money<1000:
        money=money
    elif money<2000:
        money=money*0.9
    elif money<3000:
        money=money*0.85
    elif money>=3000:
        money=money*0.8
elif level=="Gold":
    if money<1000:
        money=money
    elif money<2000:
        money=money*0.85
    elif money<3000:
        money=money*0.8
    elif money>=3000:
        money=money*0.75
else:
    print("Invalid member level. Please enter 'Regular' or 'Gold'.")
    exit()
print(level," ＄",money)