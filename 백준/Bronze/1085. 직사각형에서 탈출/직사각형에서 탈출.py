
x, y, w, h = map(int, input().split())
a1 = abs(x - 0)
a2 = abs(y - 0)
a3 = abs(w - x)
a4 = abs(h - y)
a = [a1, a2, a3, a4]
print(min(a))