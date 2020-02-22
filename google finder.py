poss_ways=[]
g_1=["g","G"]
o_1=["O","0","o","()","[]","<>"]
o_2=["O","0","o","()","[]","<>"]
g_2=["g","G"]
l_1=["l","L","I"]
e_1=["e","E","3"]
for i in g_1:
    for j in o_1:
        for k in o_2:
            for x in g_2:
                for y in l_1:
                    for z in e_1:
                        poss_ways.append([i,j,k,x,y,z])
check=[]

to_che=str(input())
for i in to_che:
    check.append(i)
if len(check)==6:
    if check in poss_ways:
        print(True)
    else:
        print(False)
elif len(check)==7:
    if check[1]=="<" or check[1]=="[" or check[1]=="("  and check[2]==">" or check[2]==")" or check[2]=="]":
        to_join="".join(check[1:3])
        check.pop(1)
        check.pop(1)
        check.insert(1,to_join)
        if check in poss_ways:
            print(True)
        else:
            print(False)
            
    elif check[2]=="<" or check[2]=="[" or check[2]=="(" and check[3]==">" or check[3]==")" or check[3]=="]":
        to_join="".join(check[2:4])
        check.pop(2)
        check.pop(2)
        check.insert(2,to_join)
        if check in poss_ways:
            print(True)
        else:
            print(False)
    else:
        print(False)
            
elif len(check)==8:   
    if check[1]=="<" or check[1]=="[" or check[1]=="(" and check[2]==")" or check[2]==">" or check[2]=="]" and check[3]=="<" or check[3]=="[" or check[3]=="(" and check[4]==">" or check[4]==")" or check[4]=="]": 
        to_join="".join(check[1:3])
        to_join1="".join(check[3:5])
        check.pop(1)
        check.pop(1)
        check.pop(1)
        check.pop(1)
        check.insert(1,to_join)
        check.insert(2,to_join1)
        if check in poss_ways:
            print(True)
        else:
            print(False)
    else:
        print(False)
else:
    print(False)