question1

#zexception occured is ZeroDivisionError

try:
    a=3
    a=a/(a-3)
except ZeroDivisionError:
    print("error")
else:
    print(a)
finally:
    print("handeled")

#question2

#IndexError

try:
    l=[1,2,3]
    a=l[3]
except IndexError:
    print("list index is out boundes")
else:
    print(l)
finally:
    print("handeled")

#question3

print("output is : an exception")

#question4

print(" AbyB(2.0,3.0) , output is : -5 ")
print(" AbyB (3.0,3.0) , output is a/result in 0")

#question5

#import error
try:
    import prink
except ImportError:
    print("error")

#value error
try:
    n=int(input("enter the value"))
except ValueError:
    print("please enter a value")

#index error

try:
    l=[1,2]
    n=l[4]
except IndexError:
    print("Index out of bounds")

#question6

i=0
class Agetosmall(Exception):
    pass
while(i<18):
    try:
        i=int(input("Enter the age :"))
        if (i<18):
            raise Agetosmall
    except Agetosmall:
        print("age is less than 18 ")
else :
    while(False):
        pass
