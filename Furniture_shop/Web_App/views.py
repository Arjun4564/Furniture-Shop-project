from django.shortcuts import render,redirect
from Furniture_app.models import Product_Db,Category_Db
from Web_App.models import Contact_Db,SignUp_Db,Cart_Db
from django.contrib import messages


# Create your views here.
def Home_Page(request):
    
    cat_d=Category_Db.objects.all()
    cart_data=Cart_Db.objects.filter(User_name=request.session['Name'])
    x=cart_data.count()
    return render(request,'home.html',{'cat_d':cat_d , 'x':x})

def product_page(request):
    products=Product_Db.objects.all()
    cart_data=Cart_Db.objects.filter(User_name=request.session['Name'])
    x=cart_data.count()
    return render(request,'product_page.html',{'products':products, 'x':x})

def about_page(request):
    return render(request,'about_page.html')


def contact_page(request):
    return render(request,'contact_page.html')

def services_page(request):
    return render(request,'services_page.html')

def blog_page(request):
    return render(request,'blog_page.html')

def save_contact(request):
    if request.method == 'POST':
        fname=request.POST.get('fname_')
        lname=request.POST.get('lname_')
        email=request.POST.get('email_')
        message=request.POST.get('message_')
        obj=Contact_Db(First_name=fname,Last_name=lname,Email=email,Message=message)
        obj.save()
        return redirect(contact_page)
    
def product_filtered(request,cat_name):
    data=Product_Db.objects.filter(Product_Category=cat_name)
    return render(request,'product_filtered.html',{'data':data})
    
def single_product(request,sin_id):
    sing=Product_Db.objects.get(id=sin_id)
    return render(request,'single_product.html',{'sing':sing})

def Sign_up(request):
    return render(request,'sign_up.html')

def Save_Sign_up(request):
    if request.method=='POST':
        _name=request.POST.get('name_')
        _mobile_number=request.POST.get('mobile_number_')
        _email=request.POST.get('email_')
        _Password=request.POST.get('Password_')
        _re_pass=request.POST.get('re_pass_')
        obj=SignUp_Db(Name=_name,Mobile_number=_mobile_number,Email=_email,Password=_Password,Repeat_Password=_re_pass)
        obj.save()
        return redirect(Sign_up)

def Sign_in(request):
    return render(request,'Sign_in.html')

def User_Sign_in(request):
    if request.method=='POST':
        _username=request.POST.get('name_')
        _password=request.POST.get('password_')
        if SignUp_Db.objects.filter(Name=_username,Password=_password).exists():
            request.session['Name']=_username
            request.session['Password']=_password
            messages.success(request,"Login successfully...!!!")
            return redirect(Home_Page)
        else:
            messages.info(request,"password incorect...!!")
            return redirect(Sign_in)
    else:
        messages.error(request,"Invalid Username...!!!")
        return redirect(Sign_in)

def User_Sign_out(request):
    del request.session['Name']
    del request.session['Password']
    messages.info(request,"Logout successfully...!!!")
    return redirect(Home_Page)

def Save_Cart(request):
    if request.method=='POST':
        _user_name=request.POST.get('user_name_')
        _product_name=request.POST.get('product_name_')
        _total=request.POST.get('total_')
        _price=request.POST.get('price_')
        _quantity=request.POST.get('quantity_')
        obj=Cart_Db(User_name=_user_name,Product_name=_product_name,Quantity=_quantity,Price=_price,Total_Price=_total,)
        obj.save()
        messages.success(request,"item added to cart")
        return redirect(Cart_Page)
    
def Cart_Page(request):
    
    obj=Cart_Db.objects.filter(User_name=request.session['Name'])
    Sub_total=0
    Shipping_amount=0
    total_amount=0
    for i in obj:
        Sub_total = Sub_total+i.Total_Price
        if Sub_total>50000:
            Shipping_amount = 100
        else:
            Shipping_amount = 250
        total_amount = Shipping_amount + Sub_total 
    

    return render(request,'cart.html',{'obj':obj,'Sub_total':Sub_total,'total_amount':total_amount,'Shipping_amount':Shipping_amount,})

def Cart_delete(request,del_id):
    remove=Cart_Db.objects.filter(id=del_id)
    remove.delete()
    return redirect(Cart_Page)

def Proceed_CheckOut(request):
    obj=Cart_Db.objects.filter(User_name=request.session['Name'])
    Sub_total=0
    Shipping_amount=0
    total_amount=0
    for i in obj:
        Sub_total = Sub_total+i.Total_Price
        if Sub_total>50000:
            Shipping_amount = 100
        else:
            Shipping_amount = 250
        total_amount = Shipping_amount + Sub_total 
    return render(request,'proceed_checkout.html',{'obj':obj,'Sub_total':Sub_total,'total_amount':total_amount,'Shipping_amount':Shipping_amount})
   
        

