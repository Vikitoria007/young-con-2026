def solution():
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    

    def check(b):
        if len(b) <= 2:
            return True
        diff = b[1] - b[0]
        for i in range(2, len(b)):
            if b[i] - b[i-1] != diff:
                return False
        return True
    
    if n == 3:
        
        if check(nums[1:]):
            print(1)
            print(nums[0])
            print(2)
            print(' '.join(map(str, nums[1:])))
            return
       
        if check(nums[:2]):
            print(2)
            print(' '.join(map(str, nums[:2])))
            print(1)
            print(nums[2])
            return
        
        if check(nums):
            print(3)
            print(' '.join(map(str, nums)))
            print(0)
            print()
            return
    
    if n == 2:
        print(1) 
        print(nums[0])
        print(1)
        print(nums[1])
    if all(x == nums[0] for x in nums):
        half = n // 2 
        print(half) 
        print(' '.join(map(str, [nums[0]] * half)))
        print(n - half) 
        print(' '.join(map(str, [nums[0]] * (n - half))))
        return 
    if check(nums):
        print(n)
        print(' '.join(map(str, nums)))
        print(0)
        print()
        return

    for diff in [nums[1] - nums[0], 0]:
        used = [False] * n
        first = []
        current = nums[0]
        while current <= nums[-1]:
            ok = False
            for i in range(n):
                if not used[i] and nums[i] == current:
                    used[i] = True
                    first.append(current)
                    ok = True
                    break
            if not ok:
                break
            if diff == 0:
                for i in range(n):
                    if not used[i] and nums[i] == current:
                        used[i] = True
                        first.append(current)
                break
            current += diff
        rest = [nums[i] for i in range(n) if not used[i]]
        if check(rest):
            print(len(first))
            print(' '.join(map(str, first)))
            print(len(rest))
            print(' '.join(map(str, rest)))
            return

    for diff in [nums[2] - nums[1], 0]:
        used = [False] * n
        first = []
        current = nums[1]
        while current <= nums[-1]:
            ok = False
            for i in range(n):
                if not used[i] and nums[i] == current:
                    used[i] = True
                    first.append(current)
                    ok = True
                    break
            if not ok:
                break
            if diff == 0:
                for i in range(n):
                    if not used[i] and nums[i] == current:
                        used[i] = True
                        first.append(current)
                break
            current += diff
        rest = [nums[i] for i in range(n) if not used[i]]
        if check(rest):
            print(len(first))
            print(' '.join(map(str, first)))
            print(len(rest))
            print(' '.join(map(str, rest)))
            return

    if check(nums):
        print(n)
        print(' '.join(map(str, nums)))
        print(0)
        print()
        return

    print(-1)

if __name__ == "__main__":
    solution()
