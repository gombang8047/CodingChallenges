import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = N - 1
best_sum = abs(arr[start] + arr[end])
ans = [arr[start], arr[end]]

while start < end:
    s = arr[start] + arr[end]

    if abs(s) < best_sum:
        best_sum = abs(s)
        ans = [arr[start], arr[end]]

    if s == 0:
        break
    elif s < 0:
        start += 1
    else:
        end -= 1

print(ans[0], ans[1])
