while True:
    a = int(input())
    if a == -1:
        break
    num = []
    for i in range(1, a):
        if a % i == 0:
            num.append(i)
    
    if sum(num) == a:
        print(a, ' = ', " + ".join(str(i) for i in num), sep='')
    else:
        print(a, 'is NOT perfect.')