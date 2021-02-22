from django.shortcuts import render
from .models import participatent
from django.core.exceptions import ValidationError

# Create your views here.
def home(request):
    context = {}
    return render(request,'coolapp/home.html',context)
def register(request):
    context = {}
    if request.method == 'POST':
        p1 = participatent()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.email = request.POST.get('phone','-')
        p1.email = request.POST.get('insitution','-')

        if  len(participatent.objects.all())>5:
            return render(request,'coolapp/failed.html',context)
        else:
            p1.save()
            return render(request,'coolapp/success.html',context)
    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''
        context['insitution'] = ''


    return render(request, 'coolapp/register.html', context)
def result(request):
    context = {}

    context['participatent'] = participatent.objects.all()

    return render(request, 'coolapp/result.html', context)

