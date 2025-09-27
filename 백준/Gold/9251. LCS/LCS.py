import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

first_word = list(input().strip())
second_word = list(input().strip())

dp = [[-1] * (len(second_word)+1) for _ in range(len(first_word)+1)]

def lcs(first_word_length, second_word_length):

    if dp[first_word_length][second_word_length] != -1:
        return dp[first_word_length][second_word_length]

    if first_word_length == 0 or second_word_length == 0:
        return 0
    
    if first_word[first_word_length-1] != second_word[second_word_length-1]:
        dp[first_word_length][second_word_length] = max(lcs(first_word_length-1, second_word_length), lcs(first_word_length, second_word_length-1))
    else:
        dp[first_word_length][second_word_length] = lcs(first_word_length-1, second_word_length-1) + 1

    return dp[first_word_length][second_word_length]

print(lcs(len(first_word), len(second_word)))