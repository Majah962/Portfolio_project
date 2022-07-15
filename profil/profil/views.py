
from django.shortcuts import render
from .models import Student
from .models import  college



def index(request):
    return render(request, 'index.html')

def about(request):
    inf1=Student('Maja Hercigonja','+385989557898','Klanjec,Croatia',22,'Undergraduate','majah9973@gmail.com')
    print(inf1.printname())
    
    return render(request, "about.html", {'inf1': inf1})
  
def education(request):
    return render(request, 'education.html')
      
def experience(request):
    inf2 = college('Maja Hercigonja','majah9973@gmail.com,','Zabok','Croatia','+38598955787',22,'Undergraduate')
    print(inf2.details())
    return render(request, 'experience.html', {'inf2': inf2})
      
