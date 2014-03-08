from __future__ import division
a=input('scrivi qui fin quanto vuoi calcolare i numeri primi ')
b=range(3,a+1,2)
d=[]
x=[]
r=a+1
for c in b:
    for g in b:
        if c/2==g:
            d.append(c)
        else :
            if c/3==g:
                d.append(c)
        
for h in d:
  for j in b:
      if h==j:
          b.remove(j)
b.insert(0,2)
d=[]
for y in b:
  for z in b:
     if y*z<=r:
       x.append(y*z)
for t in x:
  for i in b:
    if t==i:
      d.append(i)
for h in d:
  for j in b:
      if h==j:
          b.remove(j)
print b
