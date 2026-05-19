
arr = [4, 6, 6, 6, 6, 8, 8]

from collections import Counter

freq = Counter(arr)
cur_max = -1
cur_num = -1
for key, value in freq.items():
    if value > cur_max:
        cur_max = value
        cur_num = key

if cur_max > len(arr) / 2:
    print(cur_num)
else:
    print(-1)
