a = [-2,-1,0,1,2,3]
N = 1
b = []
for i in a:
    # 1 -N < n < N
    # 0 |n| > N
    if abs(i) > N:
        b.append(0)
    elif -N <= i or i <= N:
        b.append(1)


def degrau(n):
    d = 1*(n>=0)
    return d

