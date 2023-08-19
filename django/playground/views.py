from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def calculate():
    x =1
    y = 2
    return x
def say_hello(request):
    return render(request,'hello.html')

def post(self, request, *args, **kwargs):
   update_type = request.POST.get('update_type')
   if update_type == 'manual':
       return ('hello')
   else:
       "update the db with auto to true"