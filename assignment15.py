#Question1
f=open("fftt.txt","r",encoding="UTF8")
n=int(input("enter no.of lines to be read"))
list1=f.readlines()
m=len(list1)-n
for l in list1[m:]:
    print(l)

#Question2
f=open("fftt.txt","r",encoding="UTF8")
word = input("enter a word to search its frequency")
l=f.read()
l1=l.lower()
print(l1.count(word))

#Question3
f=open("fftt.txt","r",encoding="UTF8")
f1=open("dan.txt","a",encoding="UTF8")
for a in f:
    f1.write(a)

#Question4
f=open("fftt.txt","r",encoding="UTF8")
f1=open("dan.txt","r",encoding="UTF8")
f2=open("dan2.txt","a",encoding="UTF8")
for a,b in zip(f,f1):
    f2.write(a)
    f2.write(b)

#Question5
import random
def Rand(start,end,num):
    res=[]
    for j in range(num):
        res.append(random.randint(start,end))
    return res
num=10
start=20
end=40
print(Rand(start,end,num))
