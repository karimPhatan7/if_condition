from django.shortcuts import render

# Create your views here.
def ifcond(request):
    data={'a':10,'b':20,'c':33}
    return render(request,'ifcond.html',data)