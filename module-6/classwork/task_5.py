nums = [1,24,336,4,6,23,6,52]
result = {}

for num in nums:
    digit_length = len(str(abs(num)))
    result [digit_length] = result.setdefault(digit_length, 0) + 1

for item in sorted(result):
    print(item, result[item])