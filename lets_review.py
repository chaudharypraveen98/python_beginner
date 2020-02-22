# Enter your code here. Read input from STDIN. Print output to STDOUT
test_case=int(input())
words=[]
for i in range(0,test_case):
    q=str(input())
    words.append(q)
def review(words):
    for m in words:
        letters=[]
        even_words=[]
        odd_words=[]
        ev_index=[]
        odd_index=[]
        for k in m:
            letters.append(k)
        for i in range(0,len(letters)):
            if i%2==0:
                ev_index.append(i)
            else:
                odd_index.append(i)
        for h in ev_index:
            even_words.append(letters[h])
        for h in odd_index:
            odd_words.append(letters[h])
        print("".join(even_words),"".join(odd_words))

review(words)

