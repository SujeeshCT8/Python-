from itertools import combinations_with_replacement

S, k = input().split()
k = int(k)
for combination in combinations_with_replacement(sorted(S), k):
    print(''.join(combination))