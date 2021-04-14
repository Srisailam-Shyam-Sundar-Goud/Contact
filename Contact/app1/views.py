from django.shortcuts import render
from .models import contact_details
from .admin import contact_detailsAdmin
# Create your views here.
def html_view(request):
    return render(request,'contact.html')
def insert(request):
    name = request.POST['n1']
    number = int(request.POST['num1'])
    address = request.POST['add1']
    email1 = request.POST['e1']
    cre=contact_details.objects.create(Cname='name',Cnumber=number,Caddress=address,Cemail1=email1)
    cre.save
    retrive=contact_details.objects.all()
    dict_list = {'data':retrive,'cre1':cre}
    return render(request,'store.html',context=dict_list)