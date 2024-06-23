# initialize num1 and num2 here
num1=str(input("num1:"))
num2=str(input("num2:"))
ans = 0
m, n = len(num1), len(num2)
i = 0
while i < m:
    a = int(num1[m - 1 - i])
    j = 0
    while j < n:
        b = int(num2[n - 1 - j])
        ans += a * b * (10 ** (i + j))
        j += 1
    i += 1
print(ans)