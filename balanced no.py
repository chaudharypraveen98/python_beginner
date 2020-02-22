B,L=map(int,input().split())
E=list(map(int,input().split()))
D=E[::-1]
pass_value=[]
#for calculating N
N=0
for i in D:
    if 0<=i<B:
        N=N+(B**(D.index(i)))*(i)
    else:
        pass
    
sum=0
if 1<B<10001 and 2<=B*(L*L)<=2*((10)**7) and 0<(D[0]):
    for x in range(1,N+1):
        no_of_digit=[]
        for y in str(x):
            no_of_digit.append(y)
        m=len(no_of_digit)
        remain=[]
        quot=x//B
        X=x
        if m==1:
            sum=sum+x
            pass_value.append(x)
         
        else:        
            while X!=0:           
                remainder=X%B
                remain.append(remainder)
                X=X//B
            remain=remain[::-1]
            
            
            if len(remain)%2!=0:
                first_half=remain[0:(len(remain)//2)]
                sec_half=remain[(len(remain)//2)+1:len(remain)]
                f_sum=0
                s_sum=0
                for i in first_half:
                    f_sum=f_sum+i
                for i in sec_half:
                    s_sum=s_sum+i
                if f_sum==s_sum:
                    sum=sum+x
                    pass_value.append(x)
                else:
                    pass
            else:
                first_half=remain[0:(len(remain)//2)]
                f_sum=0
                s_sum=0
                sec_half=remain[(len(remain)//2):len(remain)]
                for i in first_half:
                    f_sum=f_sum+i
                for i in sec_half:
                    s_sum=s_sum+i            
                if f_sum==s_sum:
                    sum=sum+x
                    pass_value.append(x)
                else:
                    pass
        
print(len(pass_value),sum)