

num = 1

for _ in range(1, 11):
    a = input()
    result = 0

    if a == "...":
        print("...")
        break
    else:
        lst = list(map(int, input().split()))

        i = 2
        while True:
            if i > len(lst)-3:
                break
            else:
                tmp = [lst[i-2], lst[i-1], lst[i+1], lst[i+2]]
                maxNum = max(tmp)
                if maxNum < lst[i]:
                    result = result + lst[i] - maxNum
                    i+=3
                else:
                    i+=1


    print(f"#{num} {result}")
    num += 1