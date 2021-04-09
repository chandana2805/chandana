from django.urls import path
from Noteapp import views
from django.contrib.auth import views as ad

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.aboutus,name="ab"),
	path('cnt/',views.contactus,name="con"),
	path('lg/',ad.LoginView.as_view(template_name='stc/login.html'),name="log"),
	path('rg/',views.regi,name="rge"),
	path('ds/',views.dashboard,name="dsh"),
	path('lgo/',ad.LogoutView.as_view(template_name='stc/logout.html'),name="logo"),
	]