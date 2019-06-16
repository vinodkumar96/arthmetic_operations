from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def input (request):
    return render(request,"base.html")
def arthmetic (request):
    try:
        a=request.POST["t1"]
        b=request.POST["t2"]
        c=int(a)
        d=int(b)
        op= request.POST["operation"]
    except(ValueError):
        return HttpResponse("ivalid input")
    if op=="add":
        e=c+d
        return HttpResponse("the sum is :" +str(e))
    elif op == "sub":
        e = c - d
        return HttpResponse("the sub is :" +str(e))
    elif op == "mul":
        e = c * d
        return HttpResponse("the mul is :" +str(e))
    elif op == "div":
        try:
            e = c / d
            return HttpResponse("the div is :" + str(e))
        except(ZeroDivisionError):
            return HttpResponse("zero division error")

