from django.shortcuts import render, redirect, get_object_or_404
from .models import *

from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.

def pdf(request, *args, **kwargs):

    pk = kwargs.get('pk')
    a = get_object_or_404(Add, pk=pk)

    template_path = 'pdf.html'
    context = {'a': a}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funny view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        password = request.POST.get("password")

        query = Register(name=name, email=email, contact=contact, password=password)
        query.save()
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            checkuser = Register.objects.get(email=email, password=password)
        except:
            checkuser = None
    
        if checkuser is not None:
            return redirect('add')
        else:
            return redirect('login')
        
    return render(request, 'login.html')

def add(request):
    if request.method == 'POST':
        cname = request.POST.get("cname")
        ccolor = request.POST.get("ccolor")
        cprice = request.POST.get("cprice")

        query = Add(cname=cname, ccolor=ccolor, cprice=cprice)
        query.save()
    return render(request, 'add.html')

def display(request):
    data = Add.objects.all()
    return render(request, 'display.html', {'data': data})

def delete(request, id):
    dele = Add.objects.get(id=id)
    dele.delete()
    return redirect('display')

def update(request, id):
    upd = Add.objects.get(id=id)
    return render(request, 'update.html', {'upd': upd})

def edit(request, id):
    if request.method == 'POST':
        cname = request.POST.get("cname")
        ccolor = request.POST.get("ccolor")
        cprice = request.POST.get("cprice")

        obj = Add.objects.get(id=id)
        obj.cname = cname
        obj.ccolor = ccolor
        obj.cprice = cprice
        obj.save()
        return redirect('display')
    return render(request, 'update.html')