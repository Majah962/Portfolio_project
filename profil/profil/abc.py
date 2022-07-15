import django
print(django.get_version())




class Student():   #class 
    
    
    def __init__(self, name, surname, email, number, city): #constructor
        self.name = name  # instance atributes
        self.surname = surname
        self.email = email
        self.number = number
        self.city = city
        self.a = "I am from Croatia."  #public
        self.__c = "I am from Croatia."   #encapsulation private
     
   
    
         
     
    def print_c(self):
        print(self.__c)
 
    def studying(self):   #class method
        print("I'am currently studying in {}.".format(self.city))
        
 ## Polymorphism   
    def intro(self):
            print("I'm on master's degree.")
  
    def story(self):
        print("I like to go in gym.")

    attr1 = "student" #class attribute


p1 = Student("Maja","Hercigonja","majah9973gmail.com",385989557898, "Slovenia")

#object   #variables

#polymorphism
def func(obj):
        obj.intro()
        obj.story()
    

#Object instantiation #pristup klasinim atributima
print("Hi,I'am {}.".format(p1.__class__.attr1))
print("My name is {}".format(p1.name) +" and my surname is {}.".format(p1.surname) )
print("Some of my data are:  ")
print(p1.email)
print(p1.number)



p1.studying()  #method

#inheritance
#child Class
class college(Student):
    
    def __init__(self, name, adress, city, country,surname,email, number): #constructor
        self.adress = adress #atributi
        self.country = country
        self.number = number
        Student.__init__(self,name,surname,email,number,city)
        #invoking from parent class
    
   
    def details(self): #class method
        print("College name is {}.".format(p2.name))
        print("College is on {},".format(p2.adress) + "in {}".format(p2.city))
        print("Country is  {}".format(p2.country))
        print("College is also {}.".format(p2.surname))
        print("Email is in {}".format(p2.email))
        print("College number is {}.".format(p2.number))
    
    ## Polymorphism   
    def intro(self):
            print("ALM is a college.")
  
    def story(self):
        print("ALM has a lot of different majors.")
    
p2 = college("Alma Mater Europea","Slovenska 17", "Maribor","Slovenia","European center"," info@almamater.si",38622501999)
    
p2.details()

#Polymorphism
def func(obj):
        obj.intro()
        obj.story()
func(p1)
func(p2)

#drugi način:
#p1.intro()
#p1.story()
#p2.intro()
#p2.story()

#Encapsulation
#private __
class Information:
    def __init__(self):
        Student.__init__(self)
        print("Calling private member of base class: ")
        print(self.__c)
        
print(p1.a)
  

   