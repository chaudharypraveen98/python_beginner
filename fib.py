def fib(n):
  a,b=0,1
  while a<n:
    a,b=b,a+b
    print(a,end=" ")

print(fib(0))