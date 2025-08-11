#What This Program Is For
#This program calculates the probability of 
# getting at least one 'a' when choosing K items
#  randomly from a list of N letters.

def combination(n, r):
    if r > n:
        return 0
    r = min(r, n - r)
    numerator = 1
    denominator = 1
    for i in range(r):
        numerator *= (n - i)
        denominator *= (i + 1)
    return numerator // denominator

# Read input
N = int(input())
letters = input().split()
K = int(input())

# Count 'a' in the list
a_count = letters.count('a')

# Calculate probability
no_a_combinations = combination(N - a_count, K)
total_combinations = combination(N, K)
prob_no_a = no_a_combinations / total_combinations if total_combinations > 0 else 0
prob_at_least_one_a = 1 - prob_no_a

# Output result rounded to 3 decimal places
print("{:.3f}".format(prob_at_least_one_a))