from Emp.models import UsrRg,NewData
from django import forms

class UsregForm(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','password']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"enter user name",
			"required":True,
			}),

		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"enter mail id",
			"required":True,
			}),
		"password":forms.PasswordInput(attrs={
			"class":"form-control",
			"placeholder":"enter password",
			"required":True,
			}),
		}


class Userupdate(forms.ModelForm):
	class Meta:
		model=UsrRg
		fields=['username','email','age']
		widgets={
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"update user name",
			"required":True,
			}),

		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"update your mail id",
			"required":True,
			}),

		"age":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"update your age",
			"required":True,
			}),
		}

class NewUsrForm(forms.ModelForm):
	class Meta:
		model = NewData
		fields = ['mobile','gender']
		widgets={
		"mobile":forms.NumberInput(attrs={
			"class":"form-control",
			"placeholder":"Enter your mobile number",
			"required":True,
			}),
		 "gender":forms.Select(attrs={
		 	"class":"form-control",
		 	}),
		 }