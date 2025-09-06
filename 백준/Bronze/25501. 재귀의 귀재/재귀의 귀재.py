import sys

input = sys.stdin.readline

def recursion(word, start, end, count):
  count += 1
  if start >= end:
    return 1, count
  if word[start] != word[end]:
    return 0, count
  else:
    return recursion(word, start + 1, end - 1, count)

def is_palindrome(word):
  return recursion(word, 0, len(word)-1, 0)


T = int(input())

for _ in range(T):
  answer = is_palindrome(input().strip())
  print(answer[0], answer[1])