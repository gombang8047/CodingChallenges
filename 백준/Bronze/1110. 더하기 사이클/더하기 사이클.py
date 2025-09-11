def count(N, num):

    if int(N) < 10:
        N = "0" + str(N)
    
    N = str(N)

    k = (int(N[0]) + int(N[1])) % 10
    fin = int(N[1] + str(k))

    num += 1

    if fin == first:
        print(num)
        exit()

    count(fin, num)

N = int(input())

first = N

count(N, 0)

