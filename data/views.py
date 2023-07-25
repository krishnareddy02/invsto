from django.shortcuts import render
from django.http import JsonResponse
from django.contrib import messages
from .models import data101
from .forms import *
from tablib import Dataset

# Create your views here.
def home_page(request):

    return render(request,'home.html')

def my_file(request):
    # if request.method==['POST']:
    # form=data_form(request.POST,request.FILES)
    # if form.is_valid():

        print("hi")
        dataset=Dataset()
        data_sheet=request.FILES['myfile']
            
        import_data=dataset.load(data_sheet.read(),format='xlsx')


        for i in import_data:
            value=data101(
                datetime=i[0],
                close=i[1],
                high=i[2],
                low=i[3],
                open=i[4],
                volume=i[5],
                instrument=i[6]
                
                )
            value.save()
    # else:
    #     # messages.error("please upload the file")
    #     return render(request,'home.html')
        
    
        return render(request,'home.html')

def datalistview(request):
    temp=True
    d={}
    data1=data101.objects.all()
    d={
            "data1":data1
        }
    return render(request,'data.html',context=d)

def delete(request):
     delete_data=data101.objects.all()
     delete_data.delete()
     return render(request,'data.html')

def return_to_home_page(request):
     
     return render(request,'home.html')