def is_prime(A):
  if A <= 1:
    return False
  if A ==2:
    return True
  if A % 2 == 0:
    return False
  for i in range(3, int(A**(1/2)) + 1, 2):
    if A % i == 0:
      return False
  return True

N = int(input())

count = 0

a = list(map(int, input().split()))
for i in range(len(a)):
  if is_prime(a[i]):
    count += 1

print(count)