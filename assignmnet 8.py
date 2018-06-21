
#question5
import datetime,time
print(time.localtime(50*366*86400+366*86400+280*86400-4*86400))

#question2
import _datetime,time
print(_datetime.datetime.today())

#question3
a=datetime.date.today()
print(a.month)
print(datetime.date.today().month)

#question4
b=datetime.date.today()
print(b.day)
print(datetime.date.today().day)

#question7
import math
print(math.factorial(10))

#question6
import datetime
print(datetime.datetime.now().strftime('%d-%b-%Y'))

#question8
a=int(input('1st no \n'))
b=int(input('2nd no \n'))
def gcd(m,n):
    z=abs(m-n)
    if(m-n)==0:
        return n
    else:
        return gcd(z,min(m,n))
print(gcd(a,b))


#question9
import os
print(os.environ)
print(os.getcwd())

#question1
a=("Many of python's time function handle time as a tuple of 9 numbers, as shown below"
   "these have index,field,values for index,Field,values are 0 to 8 of tuple of 9 numbers"
   "for ex  4-digit year is value are 2008"
   "and this is describe the month,hour,day,minute,second,day of week,day of year,daylight savings"
   "These are above tuple is equivalent to struct_time structure.this structure has following attribute"
   "the Attributes and value like tm_year,tm_mon,tm_mday,tm_hour etc is the example of attributes")
print(a)