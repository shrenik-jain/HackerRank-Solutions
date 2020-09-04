n = int(input())
N = list(map(int , input().split()))
m = int(input())
M = list(map(int , input().split()))

x = set(N).difference(set(M)) 
y = set(M).difference(set(N)) 
z = sorted(list(x.union(y)))

for i in z:
    print(i)
