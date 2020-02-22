divident,divisor=map(int(input().split())
def all_quot(divident,divisor):
    q=[]
    q.append(1)
    while q[0]!=0:
        quotient=divident//divisor
        q.pop(0)
        q.append(quotient)
    print(q)
all_quot(divident,divisor)
        