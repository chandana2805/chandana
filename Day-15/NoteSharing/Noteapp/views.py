from django.shortcuts import render,redirect
from Noteapp.forms import UsForm

# Create your views here.
def home(req):
	return render(req,'stc/home.html')

def aboutus(re):
	return render(re,'stc/about.html')

def contactus(rq):
	return render(rq,'stc/contact.html')

def regi(request):
	if request.method=="POST":
		t=UsForm(request.POST)
		if t.is_valid():
			t.save()
			return redirect('/lg')
	t=UsForm()
	return render(request,'stc/register.html',{'u':t})	

def dashboard(qw):
	return render(qw,'stc/dashboard.html')
	
