def find_missing_ranges(nums, lower, upper):
    def format_range(start, end):
        if start == end:
            return str(start)
        else:
            return f"{start}->{end}"
    
    missing_ranges = []
    prev = lower - 1  # 初始化為 lower 的前一個數字
    
    # 加上 upper + 1 來處理最後一個元素之後的範圍
    for num in nums + [upper + 1]:
        if num - prev > 1:
            missing_ranges.append(format_range(prev + 1, num - 1))
        prev = num
    
    return missing_ranges

# 主程式
if __name__ == "__main__":
    # 讓使用者輸入數字列表
    nums_input = input("Input list:")
    nums = list(map(int, nums_input.split(" ")))
    
    # 讓使用者輸入範圍邊界
    lower = int(input("Input low："))
    upper = int(input("Input high："))
    
    # 確認列表是排序過的
    nums.sort()
    
    # 找出缺失範圍
    missing_ranges = find_missing_ranges(nums, lower, upper)
    
    # 輸出結果
    print("缺失的範圍為：", missing_ranges)
