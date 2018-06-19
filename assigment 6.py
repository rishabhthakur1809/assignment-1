# quesstion1
i=0
while(i<10):
    i=i+1
    a=input("Enter the number")
    print(a)

 #question2
a=10
while(a==10):
    print(a)

#question 5
even=[]
odd=[]
for i in range(0,101):
    if i %2--0:
       even.append(i)
    else:
        odd.append(i)
        print("number is even",even)
        print("number is odd",odd)


    # question4
list = ["apple", 1, "name", "hello", 2.2, 3, "phone"]
Int = []
Float = []
String = []
for i in list:
        if isinstance(i, int):
            Int.append(i)

        elif isinstance(i, str):
            String.append(i)

        else:
             Float.append(i)
print(Float)
print(String)
print(Int)
print("float list =" + str(Float))
print("string list =" + str(String))
print("int list =" + str(Int))

#question 3
r=[ ]
i=int(input("enter the number"))
s=int(input("enter the number"))
r.append(i)
r.append(s)
for i in r:
 print(r)

#question 6
for i in range(0,4):
 for i in range(0,i+1):
  print("*",end=" ")
  print()

#question7
dictionary={"name":"megha","age":"21"}
for i in dictionary:
    dictionary.get(i)
    print(i)

 #question8
l=[]
for i in range(0,5):
    num=int(input("enter the number"))
    l.append(num)
print(l)
l2=[ ]
a=int(input("Enter the value:"))
x=l.index(2)
x=l.remove(2)
print(l)