T = int(input())

for _ in range(T):
  R, S = input().split()

  R = int(R)

  K = []
  for i in S:
    K.append(i * R)

  print("".join(K))