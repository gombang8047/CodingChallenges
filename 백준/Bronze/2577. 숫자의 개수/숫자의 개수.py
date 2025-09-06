A = int(input())
B = int(input())
C = int(input())

T = A * B * C

T = str(T)
k = dict()

for i in range(10):
  k[f"{i}"] = 0

for i in T:
  k[i] += 1

for i in range(10):
  print(k[f"{i}"])

