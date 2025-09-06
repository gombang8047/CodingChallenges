A, B, V = map(int, input().split())

day = (V-A) // (A-B) + 1
remainder = (V-A) % (A-B)

if remainder > 0:
  day += 1

print(day)
