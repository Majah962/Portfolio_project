from django.db import models


# Create your models here.
class Student:
    def __init__(self, name,phone,city,age,degree,email): 
        self.name = name  
        self.phone = phone
        self.city = city
        self.age = age
        self.degree = degree
        self.email = email
        
    def printname(self): 
       return self.name 
   
inf1 = Student('','','','','','',)
inf1.printname()
print(inf1.printname())

class college(Student):
    
    def __init__(self, name,email, adress, city, phone,age,degree,): 
        self.adress = adress
        self.a = "I am from Croatia."
 
        Student.__init__(self,name,email,phone,city,age,degree)
        
    def details(self):
         return self.adress
inf2 = college('','','','','','','')
inf2.details()
print(inf2.details())

