from django import forms
from django.contrib.auth.models import User
from . import models


class CustomerUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
        widgets = {
        'password': forms.PasswordInput()
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model=models.Customer
        fields=['address','mobile','profile_pic']


class PaymentForm(forms.Form):
    stripeToken = forms.CharField(widget=forms.HiddenInput())
    amount = forms.DecimalField(label='Amount', max_digits=10, decimal_places=2)
    class Meta:
        model = models.Customer
        fields = ['address', 'mobile', 'profile_pic']




























# from django import forms
# from django.contrib.auth.models import User
# from . import models


# class CustomerUserForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=['first_name','last_name','username','password']
#         widgets = {
#         'password': forms.PasswordInput()
#         }

# class CustomerForm(forms.ModelForm):
#     class Meta:
#         model=models.Customer
#         fields=['address','mobile','profile_pic']

