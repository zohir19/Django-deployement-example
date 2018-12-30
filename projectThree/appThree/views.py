from django.shortcuts import render
from appThree.forms import NewUser 
from appThree.models import User    
# Create your views here.
def index(request):
    return render(request,'appThree/index.html')
def user(request):
    form=NewUser()
    if request.method == "POST":
        form=NewUser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print("ERROR")
    return render(request,'appThree/user.html',{'form':form})
    
