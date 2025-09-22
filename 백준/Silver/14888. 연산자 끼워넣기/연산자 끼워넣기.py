def calculate(n, lst, method_list, fin):

    if n >= len(method_list):
        result.append(fin)
        return

    for i in range(len(method_list)):
        if used[i] == False:
            before = fin
            if method_list[i] == "+":
                fin += lst[n+1]
            elif method_list[i] == "-":
                fin -= lst[n+1]
            elif method_list[i] == "*":
                fin *= lst[n+1]
            elif method_list[i] == "/":
                if fin < 0:
                    fin = (fin * -1) // lst[n+1]
                    fin = fin * -1
                else:
                    fin //= lst[n+1]
            used[i] = True
            calculate(n+1, lst, method_list, fin)
            fin = before
            used[i] = False

N = int(input())
lst = list(map(int, input().split()))
method = list(map(int, input().split()))

method_list = ["+"]*method[0] + ["-"]*method[1] + ["*"]*method[2] + ["/"]*method[3]
result = []
used = [False] * len(method_list)

calculate(0, lst, method_list, lst[0])

print(max(result))
print(min(result))