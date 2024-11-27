from django.urls import path
from . import views

urlpatterns = [
    path('Furniture_Details/',views.Furniture_Details,name='Furniture_Details'),

    path('Add_Category/',views.Add_Category,name='Add_Category'),
    path('Save_Category/',views.Save_Category,name='Save_Category'),
    path('display_category/',views.display_category,name='display_category'),
    path('Delete_category/<int:del_id>/',views.Delete_category,name='Delete_category'),
    path('edit_category/<int:edit_id>/', views.edit_category, name='edit_category'),
    path('upload_category/<int:upd_id>/',views.upload_category,name='upload_category'),
   
    path('add_product/',views.add_product,name='add_product'),
    path('save_product/',views.save_product,name='save_product'),
    path('display_product/',views.display_product,name='display_product'),
    path('Delete_product/<int:del_id>/',views.Delete_product,name='Delete_product'),
    path('edit_product/<int:edit_id>/',views.edit_product,name='edit_product'),
    path('upload_product/<int:upd_id>/',views.upload_product,name='upload_product'),

    path('login_page/',views.login_page,name='login_page'),
    path('admin_login/',views.admin_login,name='admin_login'),
    path('admin_logout/',views.admin_logout,name='admin_logout'),

    path('contact_display/',views.contact_display,name='contact_display'),
    path('contact_delete/<int:del_id>/',views.contact_delete,name='contact_delete')
   

]
