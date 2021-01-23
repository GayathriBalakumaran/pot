N=int(input())
p=0
for i in range(N):
  total=0
  x=int(input())
  y=x%10
  z=x//10
  total=z**y
  p=p+total
print(p)