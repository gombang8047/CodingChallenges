row, col = map(int, input().split())

T = int(input())

lst1 = []
lst2 = []

for _ in range(T):
  a, b = map(int, input().split())

  if a == 0:
    lst1.append(b)
  elif a == 1:
    lst2.append(b)

lst1.append(0)
lst1.append(col)
lst2.append(0)
lst2.append(row)

lst1.sort()
lst2.sort()

fin1 = []
fin2 = []

for i in range(len(lst1)):
  if i+1 <= len(lst1) - 1:
    fin1.append(lst1[i+1] - lst1[i])

for i in range(len(lst2)):
  if i+1 <= len(lst2) - 1:
    fin2.append(lst2[i+1] - lst2[i])

print(max(fin1) * max(fin2))
