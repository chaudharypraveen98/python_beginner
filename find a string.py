def count_substring(string, sub_string):
    ans=0
    string_list=[]
    sub_string_list=[]
    all_words=[]
    for k in sub_string:
        sub_string_list.append(k)
    for i in string:
        string_list.append(i)
    n=0
    while n!=len(string_list):
        for i in range(n,len(string_list)+1):
            if i!=n:
                all_words.append(string_list[n:i])
            else:
                pass
        n=n+1
    print(all_words)
    for i in all_words:
        if i==sub_string_list:
            ans=ans+1
        else:
            pass
    
    return(ans)

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)