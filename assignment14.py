#Question1.

f=open("file.txt", encoding="utf8")
a=(f.readlines())
a.reverse()
n=int(input("enter number of lines"))
for i in range(0,n):
    print(a[i])
f.close()

#Question2.

a="kill"
f=open("file.txt","r")
k=f.read()
m=k.split()
print(k.count(a))

#Question3.

f=open("file.txt",encoding="utf8")
a=(f.readlines())
c=open("files3.txt","w")
c.writelines(a)

#Question4.

i=0
f=open("file1.txt","r")
a=(f.read())
f.writelines(a)


#Question5
import random

afile = open("Random.txt", "w" )

for line in afile:
    for i in range(input('How many random numbers?: ')):
         line = random.randint(1, 100)
         afile.write(line)
         print(line)

afile.close()

print("\nReading the file now." )
afile = open("Random.txt", "r")
print(afile.read())
afile.close()