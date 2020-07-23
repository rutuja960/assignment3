from django.shortcuts import render
from . import forms
from . import models

def userinfpage(request):
    f1=forms.MyForm()
    return render(request,"userinf.html",{'form':f1})

def getdata(request):
   if request.method=='POST':
       un = request.POST['username']
       p = request.POST['password']
       n=request.POST['phone_no']   
       a=request.POST['address']
       s1=models.Student(username=un,password=p,phone_no=n,address=a)
       s1.save()
       return render(request,"userinf.html",{"username":un,"password":p,"phone_no":n,"address":a})   

