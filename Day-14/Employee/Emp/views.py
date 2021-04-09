from django.shortcuts import render,redirect
from Emp.models import UsrRg,NewData
from Emp.forms import UsregForm,Userupdate,NewUsrForm
from django.http import HttpResponse
# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')

def login(request):
	return render(request,'html/login.html')

def registation(reg):
	if reg.method=="POST":
		n=reg.POST['name']
		p=reg.POST['pswd']
		emailid=reg.POST['email']
		age=reg.POST['number']
		d={'user':n,'pass':p,'email':emailid,'mobilenumber':mobile}
		return render(reg,'html/details.html',{'d':d})
	return render(reg,'html/registation.html')


def crud(request):
	if request.method=='POST':
		u=request.POST['username']
		p=request.POST['password']
		e=request.POST['email']
		a=request.POST['age']
		if len(u)!=0:
			data2=UsrRg.objects.create(username=u,password=p,email=e,age=a)
			data2=UsrRg.objects.all()
			return render(request,'html/actions.html',{'info':data2})
	return render(request,'html/actions.html')


def deletedata(request,id):
	data=UsrRg.objects.get(id=id)
	data.delete()
	return redirect('/cr')


def dform(req):
	if req.method=="POST":
		e=UsregForm(req.POST)
		if e.is_valid():
			q=e.save()
			y=NewData.objects.create(pid_id=q.id)
			# return HttpResponse("User Created Succesfully")
			return redirect('/showdata')
	e=UsregForm()
	return render(req,'html/dform.html',{'tu':e})


def showinfo(req):
	data=UsrRg.objects.all()
	return render(req,'html/showdata.html',{'info':data})


def infodelete(req,id):
	data=UsrRg.objects.get(id=id)
	if req.method=="POST":
		data.delete()
		return redirect('/showdata')
	return render(req,'html/userdel.html',{'sd':data})


#def edit(re,id):
#	data=UsrRg.objects.get(id=id)
#	if re.method=="POST":
#		data.username=re.POST['Username']
#		data.age=re.POST['Age']
#		data.email=re.POST['Email']
#		data.password=re.POST['Password']
#		data.save()
#       return HttpResponse("Data Saved")
#	return render(re,'html/useredit.html',{'info':data})


def userupdate(up,si):
	t=UsrRg.objects.get(id=si)
	y=NewData.objects.get(pid_id=si)
	if up.method=="POST":
		d=Userupdate(up.POST,instance=t)
		k=NewUsrForm(up.POST,instance=y)
		if d.is_valid() and k.is_valid():
			d.save()
			k.save()
			return redirect('/showdata')
	d=Userupdate(instance=t)
	k=NewUsrForm(up.POST,instance=y)
	return render(up,'html/updateuser.html',{'us':d,'nt':k})


def userinfo(ty,uname):
	p=UsrRg.objects.get(username=uname)
	h=NewData.objects.get(pid_id=p.id)
	return render(ty,'html/uinfo.html',{'y':p,'yu':h})

