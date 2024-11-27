from django.shortcuts import render,redirect
from .models import Category_Db,Product_Db
from django.utils.datastructures import MultiValueDictKeyError
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
import datetime
from Web_App.models import Contact_Db

from django.contrib import messages

# Create your views here.
def Furniture_Details(request):
    C_count=Category_Db.objects.count()
    P_count=Product_Db.objects.count()
    date=datetime.datetime.now
    return render(request,'index.html',{'date':date,'C_count':C_count,'P_count':P_count})

def Add_Category(request):
    return render(request,'add_category.html')

def Save_Category(request):
    if request.method=='POST':
        _category_name=request.POST.get('category_name_')
        _discription=request.POST.get('discription_')
        _category_image=request.FILES['category_image_']
        obj=Category_Db(Category_name=_category_name,Category_image=_category_image,Discription=_discription)
        obj.save()
        messages.success(request, "Category Saved...!!!")
        return redirect(Add_Category)
    
def display_category(request):
    dis=Category_Db.objects.all()
    return render(request,'display_category.html',{'pass':dis})

def Delete_category(request,del_id):
    remov=Category_Db.objects.filter(id=del_id)
    remov.delete()
    messages.error(request, "Deleted...!!!")
    return redirect(display_category)

def edit_category(request,edit_id):
    edit=Category_Db.objects.get(id=edit_id)
    return render(request,'edit_category.html',{'pass':edit})

def upload_category(request,upd_id):
    if request.method=='POST':
        _category_name=request.POST.get('category_name_')
        _discription=request.POST.get('discription_')
        try:
            _category_image=request.FILES['category_image_']
            fs=FileSystemStorage()
            category_image=fs.save(_category_image.name,_category_image)
        except MultiValueDictKeyError:
            category_image=Category_Db.objects.get(id=upd_id).Category_image

        Category_Db.objects.filter(id=upd_id).update(Category_name=_category_name,Category_image=category_image,Discription=_discription)
        messages.info(request, "Updated...!!!")
        return redirect(display_category)
    
def add_product(request):
    Category_name=Category_Db.objects.all()
    return render(request,'add_product.html',{'pass':Category_name})

def save_product(request):
    if request.method=='POST':
        _p_category=request.POST.get('p_category_')
        _p_name=request.POST.get('p_name_')
        _quantity=request.POST.get('quantity_')
        _mrp=request.POST.get('mrp_')
        _discription=request.POST.get('discription_')
        _c_origin=request.POST.get('c_origin_')
        _manufactured_by=request.POST.get('manufactured_by_')
        _p_image1=request.FILES['p_image1_']
        _p_image2=request.FILES['p_image2_']   
        _p_image3=request.FILES['p_image3_']
        obj=Product_Db(Product_Category=_p_category,Product_Name=_p_name,Quantity=_quantity,MRP=_mrp,Discription=_discription,Country_of_Origin=_c_origin,Manufactured_By=_manufactured_by,Product_Image1=_p_image1,Product_Image2=_p_image2,Product_Image3=_p_image3)
        obj.save()
        messages.success(request,"Product Saved...!!!")
        return redirect(add_product)

def display_product(request):
    dis=Product_Db.objects.all()
    return render(request,'display_product.html',{'pass':dis})

def Delete_product(request,del_id):
    remov=Product_Db.objects.filter(id=del_id)
    remov.delete()
    messages.error(request, "Deleted...!!!")
    return redirect(display_product)

def edit_product(request,edit_id):
    edit=Product_Db.objects.get(id=edit_id)
    Category_name=Category_Db.objects.all()
    return render(request,'edit_product.html',{'key':edit,'pass':Category_name})

def upload_product(request,upd_id):
    if request.method=='POST':
        _p_category=request.POST.get('p_category_')
        _p_name=request.POST.get('p_name_')
        _quantity=request.POST.get('quantity_')
        _mrp=request.POST.get('mrp_')
        _discription=request.POST.get('discription_')
        _c_origin=request.POST.get('c_origin_')
        _manufactured_by=request.POST.get('manufactured_by_')
        try:
            _p_image1=request.FILES['p_image1_']
            fs=FileSystemStorage()
            p_image1=fs.save(_p_image1.name,_p_image1)
        except MultiValueDictKeyError:
            p_image1=Product_Db.objects.get(id=upd_id).Product_Image1

        try:
            _p_image2=request.FILES['p_image2_']
            fs=FileSystemStorage()
            p_image2=fs.save(_p_image2.name,_p_image2)
        except MultiValueDictKeyError:
            p_image2=Product_Db.objects.get(id=upd_id).Product_Image2
        
        try:
            _p_image3=request.FILES['p_image3_']
            fs=FileSystemStorage()
            p_image3=fs.save(_p_image3.name,_p_image3)
        except MultiValueDictKeyError:
            p_image3=Product_Db.objects.get(id=upd_id).Product_Image3

       
        Product_Db.objects.filter(id=upd_id).update(Product_Category=_p_category,Product_Name=_p_name,Quantity=_quantity,MRP=_mrp,Discription=_discription,Country_of_Origin=_c_origin,Manufactured_By=_manufactured_by,Product_Image1=p_image1,Product_Image2=p_image2,Product_Image3=p_image3)
        messages.info(request, "Updated...!!!")
        return redirect(display_product)
    
def login_page(request):
    return render(request,'admin_login.html')

def admin_login(request):
    if request.method=="POST":
        _username=request.POST.get('username_') 
        _password=request.POST.get('password_')
        if User.objects.filter(username__contains=_username).exists():
            user=authenticate(username=_username,password=_password)
            if user is not None:
                login(request,user)
                request.session['username']=_username
                request.session['password']=_password
                messages.success(request,"Welcome...!!!")
                return redirect(Furniture_Details)
            else:
                messages.info(request,"password incorect...!!")
                return redirect(login_page)
        else:
            messages.error(request,"Invalid Username...!!!")
            return redirect(login_page)
        
def admin_logout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)

def contact_display(request):
    con=Contact_Db.objects.all()
    return render(request,'contact_display.html',{'con':con})

def contact_delete(request,del_id):
    cot_del=Contact_Db.objects.filter(id=del_id)
    cot_del.delete()
    return redirect(contact_display)

