happy=0
n,m=input().split()
main=[input() for i in range(int(n))]
A = [input() for i in range(int(m))]
B = [input() for i in range(int(m))]
for i in A:
    if i in main:
        happy=happy+1
    else:
        pass

for j in B:
    if j in main:
        happy=happy-1
    else:
        pass

print(happy)


        