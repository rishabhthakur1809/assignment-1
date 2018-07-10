#Question1
class Circle:
    def __init__(self,radius):
            self.radius = radius

    def getArea(self):
            return self.radius**2*3.14

    def getCircumference(self):
            return self.radius*2*3.14
obj = Circle(10)
print(obj.getArea())
print(obj.getCircumference())

#Question2

class Student:
    def __init__(self,Name,RollNumber):
            self.Name = Name
            self.RollNumber = RollNumber

    def Display(self):
            print("Name of student = ",self.Name)
            print("RollNumber of Student  = ",self.RollNumber)

obj = Student("Rahul",19)
obj.Display()

#Question3
class Temprature():
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)
obj = Temprature()
print(obj.convertCelsius(0))
print(obj.convertFahrenhiet(91))


#Question4
class MovieDetails:
    def __init__(self,moviename, artistname, yearofrelease, ratings):
        self.moviename=moviename
        self.artistname=artistname
        self.yearofrelease=yearofrelease
        self.ratings=ratings
    def Display(self):
        print("movie name is "+ self.moviename)
        print("artist name is "+ self.artistname)
        print("year of release is "+self.yearofrelease)
        print("ratings is"+self.ratings)
    def Update(self,moviename, artistname, yearofrelease, ratings):
        self. moviename = moviename
        self.artistname = artistname
        self.yearofrelease = yearofrelease
        self.ratings = ratings
        print("movie name is "+self.moviename)
        print("artist name is "+self.artistname)
        print("year of release is "+self.yearofrelease)
        print("ratings is " +self.ratings)
l=MovieDetails("Ammy","Virk",str(2016),str(4))
l.Display()
l.Update("Diljit","dOSANJH",str(2019),str(5))


#Question5
class Expenditure:
    expenditure=2000
    savings=1000
    def __init__(self):
        print(self.expenditure)
        print(self.savings)
    def display(self):
        print(self.expenditure)
        print(self.savings)
        salary=2000
        totalsalary=(self.expenditure)+(self.savings)
        print(salary)
        print(totalsalary)
a=Expenditure()
a.display()