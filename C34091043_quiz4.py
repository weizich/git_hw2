#輸入整數並用空白格作為分界
nums = input("Enter a list of integers separated by spaces: ").split()
nums = [int(num) for num in nums]
start = 0
max_length = 1
max_start = 0
current_length = 1

#開始使用for迴圈
for i in range(1, len(nums)):
#檢查數字是否比上一個大
    if nums[i] > nums[i - 1]:
        current_length += 1
# 檢查此sequence是否比上一個sequence長
        if current_length > max_length:
            max_length = current_length
            max_start = start
    else:
#重置
        start = i
        current_length = 1

#拉出最長的sequence
LICS = nums[max_start:max_start + max_length]
print("Length :", max_length)
print("LICS:", LICS)