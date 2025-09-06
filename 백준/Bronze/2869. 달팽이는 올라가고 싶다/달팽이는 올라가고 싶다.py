A, B, V = map(int, input().split())

count = (V - A) // (A - B) + 1
remainder = (V - A) % (A - B)

if remainder > 0 :
    count += 1

print(count)