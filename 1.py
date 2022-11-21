n = int(input())
base = 3
if n == 0:
   print(0)
nums = []
while n:
   n, r = divmod(n, base)
   nums.append(str(r))
print(''.join(reversed(nums)))