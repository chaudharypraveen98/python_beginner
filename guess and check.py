x=int(input("Enter integer:"))
ans=0
while ans**3<abs(x):
  ans+=1
if ans**3!=abs(x):
  print(x,"isn't a perfect cube")
else:
  if x<0:
    ans=-ans
  print("cube root of",x,"is",ans)