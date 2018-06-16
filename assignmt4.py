#question 1
a=(1,2,3,4)
b=(5,6,7,8,9)
c=(a+b)
print(len(c))

#question 2
d=(1,2,3,4)
e=(4,6,7)
f=(d+e)
print(min(f))
print(max(f))

#question 3
r=(1*2*3*4*5)
print(r)

#question 4
q=set([1,2,3,4])
w=set([3,4,5,6,7])
print((q-w))
print((q&w))
print((q|w))
print((q<=w))
print((q>=w))

#question 5
d={'name':'rohit',
   'marks':40}
print(d)

#question 6
g=['M','I','S','S','I','S','S','I','P','P','I']
n={'M':g.count('M'),
   'I':g.count('I'),
   'S':g.count('S'),
   'P':g.count('P')}
print(n)

#question 7
k=input("Enter the number")
s=input("Enter the number")
d={'name':k,
   'marks':s}
print(d)