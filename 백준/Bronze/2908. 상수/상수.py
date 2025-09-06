A, B = map(str, input().split())

A = list(A)
B = list(B)

K = A[0]
A[0] = A[2]
A[2] = K

K = B[0]
B[0] = B[2]
B[2] = K

A = "".join(A)
B = "".join(B)

if int(A) > int(B):
  print(A)
else:
  print(B)