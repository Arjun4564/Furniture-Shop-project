from django.urls import path
from . import views

urlpatterns = [
    path('Home_Page/',views.Home_Page,name='Home_Page'),
    path('product_page/',views.product_page,name='product_page'),
    path('about_page/',views.about_page,name='about_page'),
    path('contact_page/',views.contact_page,name='contact_page'),
    path('services_page/',views.services_page,name='services_page'),
    path('blog_page/',views.blog_page,name='blog_page'),
    path('save_contact/',views.save_contact,name='save_contact'),
    path('product_filtered/<cat_name>/',views.product_filtered,name='product_filtered'),
    path('single_product/<int:sin_id>/',views.single_product,name='single_product'),
    path('Sign_up/',views.Sign_up,name='Sign_up'),
    path('',views.Sign_in,name='Sign_in'),
    path('Save_Sign_up/',views.Save_Sign_up,name='Save_Sign_up'),
    path('User_Sign_in/',views.User_Sign_in,name='User_Sign_in'),
    path('User_Sign_out/',views.User_Sign_out,name='User_Sign_out'),
    path('Save_Cart',views.Save_Cart,name='Save_Cart'),
    path('Cart_Page/',views.Cart_Page,name='Cart_Page'),
    path('Cart_delete/<int:del_id>/',views.Cart_delete,name='Cart_delete'),
    path('Proceed_CheckOut/',views.Proceed_CheckOut,name='Proceed_CheckOut')
]