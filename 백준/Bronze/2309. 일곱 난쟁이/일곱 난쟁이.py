def dwarf(n, lst):
    

    if len(fin) == 7:
        if sum(fin) == 100: 
            fin.sort()
            print("\n".join(map(str, fin)))
            exit()
    
    if n >= 9:
        return

    fin.append(lst[n])
    dwarf(n+1, lst)
    fin.pop(-1)
    dwarf(n+1, lst)


lst = []

for _ in range(9):
    lst.append(int(input()))

fin = []

dwarf(0, lst)