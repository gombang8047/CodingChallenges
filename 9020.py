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

T = int(input())

for _ in range(T):
  A = int(input())

  k = []

  for i in range(A//2, A+1):
    if is_prime(i):
      k.append(i)

  for i in k:
    if is_prime(A - i):
      print(A-i, i)
      break
