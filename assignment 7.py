
#question1
radius=float(input("Enter the number"))
def area(radius):
 area=3.14*radius*radius
'return area'
ar=area(radius)
print(ar)

#question2
n=6
def perfect(i,n):
    sum=0
    for i in range(i,n):
       if(n%i==0):
            sum=sum+i
    if(sum==n):
     return True
    else:
      return False
for i in range(1,1001):
     if(perfect(i)==True):
        print("perfect number is:" +str(i))
     else:
         pass

#question3

def tables(n,t=1):
   if t==13:
       return
   print(str(n) + " "+str(t) + " = " + str(n*t))
   tables(n,t+1)

   tables(int(input("enter the number: ")))

#question4
def power(x,y):
    if y==1:
        return

    if y==1:
        return x * power(x,y - 1)

#question5
d = {}
f=1
for i in range(1,11):
    f=f*i
    d[i] = f
print(f)
print(d)