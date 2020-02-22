B=2
E=int(input())
remain=[]
X=E
while X!=0:
    remainder=X%B
    remain.append(remainder)
    X=X//B
all_poss=[]
all_find=[]
for i in range(1,len(remain)+1):
    s=[]
    for j in range(0,i):
        s.append(1)
    all_find.append(s)
n=0
while n!=len(remain):    
    for i in range(n,len(remain)):
        all_poss.append(remain[n:i+1])
    n=n+1
all_find=all_find[::-1]
for i in all_find:
    if i in all_poss:
        print(len(i))
        break