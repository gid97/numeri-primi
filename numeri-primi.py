from __future__ import division
a=input('scrivi qui fin quanto vuoi calcolare i numeri primi ')
b=range(3,a+1,2)
d=[]
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
    for x in b:
      if y*z==x:
	d.append(x)
for h in d:
  for j in b:
      if h==j:
          b.remove(j)
print b
