
n=2**17
sum = 0
for i in range(int(n/2)):
    sum += (1/(n-2*i-1))-(1/(n-2*i))
    print(sum, i)