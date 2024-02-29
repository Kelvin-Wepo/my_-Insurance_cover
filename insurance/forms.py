from django import forms
from .models import *





class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']

class PolicyForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label="Category Name", to_field_name="id")
    class Meta:
        model = Policy
        fields = ['policy_name', 'sum_assurance', 'premium', 'tenure']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['description']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6, 'cols': 30})
        }

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'
