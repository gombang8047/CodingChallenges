def fac(a):
  num = 1
  for i in range(1, a+1):
    num *= i
  return num

print(fac(int(input())))