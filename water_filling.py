# 讓使用者輸入地形高度序列，以逗號分隔
heights_input = input("請輸入地形高度序列（以逗號分隔）：")

# 將輸入的字串轉換為整數列表
heights = list(heights_input.split(','))

# 將地形高度序列中的每個字串轉換為整數
for i in range(len(heights)):
    heights[i] = int(heights[i])

n = len(heights)  # 地形高度序列的長度

# 初始化左右指針和結果
left = 0
right = n - 1
water_units = 0

# 初始化左右最高高度
left_max = 0
right_max = 0

while left < right:
    if heights[left] < heights[right]:
        if heights[left] >= left_max:
            left_max = heights[left]
        else:
            water_units += left_max - heights[left]
        left += 1
    else:
        if heights[right] >= right_max:
            right_max = heights[right]
        else:
            water_units += right_max - heights[right]
        right -= 1

print("最多可以容納", water_units, "個單位的水")
