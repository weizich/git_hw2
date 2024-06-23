n = int(input("Enter a positive integer: "))
prime_numbers = []

x = 0
i = list(range(3, n + 1))  # 定義 i 為我們的數字範圍
while x < len(i):
    is_prime = True
    j = 2
    while j < i[x]:
        if i[x] % j == 0:
            is_prime = False
            break
        j += 1
    if is_prime:
        prime_numbers.append(i[x])
    x += 1

print("Prime list from 2 to",n,"are",prime_numbers)