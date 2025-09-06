#한수
#100보다 작은수는 모두 한수, 111 123 135 147 159 210

N = input()

count = 99

if int(N) < 100:
  print(N)
elif int(N) >= 100:
  for i in range(100, int(N)+1):
    i = str(i)
    if abs(int(i[0]) - int(i[1])) == abs(int(i[1])- int(i[2])):
      if i[0] <= i[1] <= i[2] or i[0] >= i[1] >= i[2]:
        count +=1
  print(count)