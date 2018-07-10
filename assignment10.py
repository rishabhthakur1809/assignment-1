 #Question 1
class Animal:
     def animal_attribute(self):
         print("This animal is ")
 class Tiger(Animal):
     def animal_name(self):
         print("Tiger")
obj = Tiger()
obj.animal_attribute()
obj.animal_name()


class A:
     def f(self):
         return self.g()

     def g(self):
         return 'A'


 #Question 4



 #Question 3
 class Cop:
     def __init__(self,name,age,work,experience,designation):
         self.name = name
         self.age = age
         self.work = work
         self.experience = experience
         self.designation = designation

     def Add(self):
          print("Following details of the cop is")

     def display(self):
         print("name is = " , self.name)
         print("age is = ", self.age)
         print("work is = ", self.work)
         print("experience is = ", self.experience)
         print("designation is = ", self.designation)


     def update(self,name,age,work,experience,designation):
         self.name = name
         self.age = age
         self.work = work
         self.experience = experience
         self.designation = designation
         print("name is = ", self.name)
         print("age is = ", self.age)
         print("work is = ", self.work)
         print("experience is = ", self.experience)
         print("designation is = ", self.designation)


class Mission(Cop):
     def add_mission_details(self):
         print("Mission Details of cop")

obj = Mission("Prink",str(25),"Work for Company" , "Fresher" , "Sales")
obj.Add()
obj.display()
obj.update("Prinkpal",str(25),"Work for Company" , "Fresher" , "Sales")


# #Question2
# A B
 # A B

class Shape:

    l = 20
    b = 20
    def Area(self,len,br):

        self.area = self.l * self.b
        print("Area = ", self.area)


class Rectangle(Shape):

    def data(self):
        print
        print("how")


obj = Rectangle()
obj.Area()
obj.data()