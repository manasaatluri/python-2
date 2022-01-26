x=open("jk.txt")
n=x.read()

m=open("v.txt")
h=m.read()

d=open("jk.txt","w")
d.write(h)

a=open("v.txt","w")
a.write(n)



