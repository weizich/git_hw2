nums_str = input("Enter sorted integer list separated by spaces: ")
nums = list(nums_str.split())
lower = int(input("Enter lower bound: "))
upper = int(input("Enter upper bound: "))
missing_ranges = []
i = lower
while i <= upper:
    if str(i) not in nums:
        start = i
        while i + 1 <= upper and str(i + 1) not in nums:
            i += 1
        end = i
        if start == end:
            missing_ranges.append(str(start))
        else:
            missing_ranges.append(str(start) + "->" + str(end))
    i += 1
print("Missing ranges:", missing_ranges)