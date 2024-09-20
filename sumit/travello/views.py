from django.shortcuts import render
from .models import Destination
def index(request):
    dest1=Destination()
    dest1.name='Mumbai'
    dest1.price=700
    dest1.img='destination_1.jpg'
    dest1.desc="hey how are you!"
    dest2=Destination()
    dest2.name='Delhi'
    dest2.price=800
    dest2.img='destination_2.jpg'
    dest2.desc="it's raining outside"
    dest3=Destination()
    dest3.name="Hyderabad"
    dest3.price=1000
    dest3.img='destination_3.jpg'
    dest3.desc="great!!"
    dests=[dest1,dest2,dest3]
    return render(request, 'index.html',{'dests':dests})
# Create your views here.
# def index(request):
#     return render(request,'index.html')
def about(request):
    return render(request,'about.html')
def elements(request):
    return render(request,'elements.html')
def news(request):
    return render(request,'news.html')
def contact(request):
    return render(request,'contact.html')
