from django.urls import path
from Emp import views

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="con"),
	path('log/',views.login,name='lg'),
    path('registation/',views.registation,name='registation'),
    path('cr/',views.crud,name='cd'),
    path('delete/<str:id>',views.deletedata,name='delete'),
    path('df/',views.dform,name='dff'),
]