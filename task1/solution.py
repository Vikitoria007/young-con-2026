n = int(input())
numbers = list(map(int, input().split()))
new_nums = {}
for num in numbers:
    new_nums[num] = new_nums.get(num, 0) + 1
first = {}
for i, num in enumerate(numbers):
    if num not in first:
        first[num] = i 

numbers.sort(key = lambda x: (-new_nums[x], first[x]))
answer = []

print(*numbers)
