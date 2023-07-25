from django.urls import path
from . import views


urlpatterns=[
    path('',views.home_page,name="home_page"),
    path('my_file',views.my_file,name="my_file"),
    path('data_10',views.datalistview,name="data_10"),
    path('delete',views.delete,name="delete"),
    path('return_to_home_page',views.return_to_home_page,name="return_to_home_page")
]