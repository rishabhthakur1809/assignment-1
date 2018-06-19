#question 1
a=int(input("Enter the year"))
if(a%4==0 and a%100!=0 or a%400==0):
    print("leap year")
else:
    print("it not leap year")

#qustion 2
l=input("Enter the length")
b=input("Enter the breath")
if(l==b):
 print("this is square")
else:
 print("this is rectangle")

 #question 3
 r=input("Enter the 1st person")
 t=input("Enter the 2nd person")
 i=input("Enter the 3rd person")
 if(r>=t and r>=i):
     print("r is oldest to all")
 elif(t>=i and t>=r):
     print("t is oldest to all")
 else:
     print("i is oldest to all")

   #question 4
 g=int(input("Enter the points out of 200"))
if(g>=1 and g<=50):
     print("sorry! you have no prize.")
elif(g>=51 and g<=150):
    print("congratulations! you won wooden dog!")
elif(g>=151 and g<=180):
    print("condratulations! you won Book!")
elif(g>=181 and g<=200):
    print("congratulations! you won choclates!")
    
   #question 5
j=int(input("Enter the number of unit,one unit costs 100"))
sum=j*100
print(sum)
if(sum>=1000):
     b=(sum-(sum*10/100))
     print("amount"+str(b))
else:
     print("amount :" +str(sum))
