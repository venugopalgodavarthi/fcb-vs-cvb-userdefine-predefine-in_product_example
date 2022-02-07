from cgitb import reset
from re import template
from django.http import HttpResponse
from django.shortcuts import render,redirect
from product.forms import productform
from product.models import productmodel
from django.views import View
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
# Create your views here.
#userdefined function based view(send html, form object creation, by modelform store the data)
def fproduct(request):
    form=productform()
    if request.method=='POST' and request.FILES:
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("value is created")
    return render(request,'product.html',{'form':form})

#userdefined class based view(send html, form object creation, by modelform store the data)
class cproduct(View):
    def get(self,request):
        form=productform()
        return render(request,'product.html',{'form':form})
    def post(self,request):
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("value is created")
        
#predefined class based view using TemplateView (send html, form object creation, by modelform store the data)
class ctemp1(TemplateView):
    template_name='product.html'
    form=productform()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']= self.form
        return context
    def post(self,request):
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("value is created")
        
#predefined class based view using FormView (send html, form object creation, by modelform store the data)
class cform(FormView):
    template_name='product.html'
    form_class = productform
    def form_valid(self,form):
        form.save()
        return HttpResponse('value is  created')
    
#predefined class based view using CreateView (send html, form object creation, by modelform store the data)
class ccre(CreateView):
    model=productmodel
    fields='__all__'
    template_name='product.html'
    context_object_name='form'
    success_url=reverse_lazy('chome')
    
#predefined class based view using TemplateView (send html, form object creation, )
class ctemp(TemplateView):
    template_name='product.html'

#predefined class based view using TemplateView (send html, form object creation, )
class home(TemplateView):
    template_name='home.html'
    
'''
predefined class based view for templateview

 # if you want sent only html file use below code
class ctemp1(TemplateView):
    template_name='product.html'   
    
# if you want sent html file with context use below code
class ctemp1(TemplateView):
    template_name='product.html'
    form=productform()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']= self.form
        return context
        
# if you want sent html file with form context  and store the data inside the db use below code
class ctemp1(TemplateView):
    template_name='product.html'
    form=productform()
    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['form']= self.form
        return context
    def post(self,request):
        form=productform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse("value is created")
    
#if you want sent html with form object use below code (normal form or model form)
class cform(FormView):
    template_name='product.html'
    form_class = productform

#if you want sent html with form object and storing the data by use below code (model form)
class cform(FormView):
    template_name='product.html'
    form_class = productform
    def form_valid(self,form):  #form validation
        form.save()
        return HttpResponse('value is  created')
        
#if you want sent html with form object and storing the data by use below code (normal form)
class cform(FormView):
    template_name='product.html'
    form_class = productform
    def form_valid(self,form):  #form validation
        product.objects.create(pname=form.cleaned_data['pname'],pdesc=form.cleaned_data['pdesc'],
        pprice=form.cleaned_data['pprice'],discount=form.cleaned_data['discount'],pimg=form.cleaned_data['pimg'])
        return HttpResponse('value is  created')
'''
    
#userdefined function based view(get the data from db, send the data to html, by help of orm) 
def fselect(request):
    res=productmodel.objects.all()
    return render(request,'select.html',{'res':res})

#userdefined class based view(get the data from db, send the data to html, by help of orm) 
class cselect(View):
    def get(self,request):
        res=productmodel.objects.all()
        return render(request,'select.html',{'res':res})

#perdefined class based view(get the data from db, send the data to html, by help of orm) 
class pcselect(ListView):
    model=productmodel
    template_name='select.html'
    context_object_name='res'
    
#userdefined function based view(get the data from db, send the data to html, by help of orm) 
def fdetails(request,pk):
    res=productmodel.objects.get(id=pk)
    return render(request,'details.html',{'res':res})

#userdefined class based view(get the data from db, send the data to html, by help of orm)
class cdetails(View):
    def get(self,request,pk):
        res=productmodel.objects.get(id=pk)
        return render(request,'details.html',{'res':res})
    
#predefined function based view(get the data from db, send the data to html, by help of orm)
class pcdetails(DetailView):
    model=productmodel
    template_name='details.html'
    context_object_name='res'

#userdefined function based view(get the data from db, send the data to html, and update the record)
def fupdate(request,pk):
    res=productmodel.objects.get(id=pk)
    form=productform(instance=res)
    if request.method=='POST' and request.FILES:
        form=productform(request.POST,request.FILES,instance=res)
        if form.is_valid():
            form.save()
            return redirect('/fselect')
    return render(request,'update.html',{'form':form})

#userdefined class based view(get the data from db, send the data to html, and update the record)
class cupdate(View):
    def get(self,request,pk):
        res=productmodel.objects.get(id=pk)
        form=productform(instance=res)
        return render(request,'update.html',{'form':form})

    def post(self,request,pk):
        res=productmodel.objects.get(id=pk)
        if request.method=='POST' and request.FILES:
            form=productform(request.POST,request.FILES,instance=res)
            if form.is_valid():
                form.save()
                return redirect('/cselect')

#predefined function based view(get the data from db, send the data to html, and update the record)
class pcupdate(UpdateView):
    model=productmodel
    fields='__all__'
    template_name='update.html'
    context_object_name='form'
    success_url=reverse_lazy('pcselect')
        
#userdefined function based view(get the data from db, and delete the record)
def fdelete(request,pk):
    productmodel.objects.get(id=pk).delete()
    return redirect('/fselect')  

#userdefined class based view(get the data from db,  and update the record)
class cdelete(View):
    def get(self,request,pk):
        productmodel.objects.get(id=pk).delete()
        return redirect('/fselect')  
    
#perdefined class based view(get the data from db,  and update the record)
class pcdelete(DeleteView):
    model=productmodel
    template_name='delete.html'
    success_url=reverse_lazy('pcselect')
        

    
