T = int(input())

for _ in range(T):
  k = input()
  count = 0
  sum = 0

  for i in range(len(k)):
    if k[i] == "O":
      count += 1
      sum += count
    else:
      count = 0
      
  print(sum)

