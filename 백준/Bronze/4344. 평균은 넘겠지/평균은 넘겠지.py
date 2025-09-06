T = int(input())

for _ in range(T):
  score = list(map(int, input().split()))
  N = score[0]
  score.pop(0)

  count = 0
  avg = sum(score) / N

  for i in score:
    if avg < i:
      count += 1
  num = "%.3f" % (count/len(score)*100)
  print(f"{num}%")