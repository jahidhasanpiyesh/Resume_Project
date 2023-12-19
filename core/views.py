from django.shortcuts import render
from .models import User
# Create your views here.
def home(request):
    context={"home":"active"}
    return render(request,'core/home.html',context)

def contact(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        txt = request.POST.get('message')
        enqury = User(name=nm, email=em, subject=sub, massage=txt)
        enqury.save()
    context={"contact":"active"}
    return render(request,'core/contact.html',context)