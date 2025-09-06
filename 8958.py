T = int(input())

for _ in range(T):
  k = input()
  count = 0
  q = 0

  for i in range(len(k)):
    if k[i] == "O":
      count += 1
      q += count
    else:
      count = 0

  print(q)

