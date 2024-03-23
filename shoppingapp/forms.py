from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.contrib import auth

from shoppingapp.models import *
from ckeditor.widgets import CKEditorWidget


    

class ShopForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Store Title :"
        self.fields['location'].label = "Store Location :"
        self.fields['avg_spend'].label = "Avg Spend :"
        self.fields['description'].label = "Shop Description :"
        self.fields['tags'].label = "Tags :"
        self.fields['last_date'].label = "Submission Deadline :"
        self.fields['url'].label = "Website :"



        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Starbucks',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : 1st Floor',
            }
        )
        self.fields['avg_spend'].widget.attrs.update(
            {
                'placeholder': '€5 - €150',
            }
        )
        self.fields['tags'].widget.attrs.update(
            {
                'placeholder': 'Use comma separated. eg: Coffee, Sandwhich ',
            }
        )                        
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
                
            }
        )                
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'Logo',
            }
        )   
         


    class Meta:
        model = Shop

        fields = [
            "title",
            "location",
            "shop_type",
            "category",
            "avg_spend",
             "description",
            "tags",
            "last_date",
            "url",
            "picture"
            ]



    def save(self, commit=True):
        shop = super(ShopForm, self).save(commit=False)
        if commit:
            
            shop.save()
        return shop








class ShopEditForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        forms.ModelForm.__init__(self, *args, **kwargs)
        self.fields['title'].label = "Store Title :"
        self.fields['location'].label = "Store Location :"
        self.fields['avg_spend'].label = "Avg Spend :"
        self.fields['description'].label = "Store Description :"    
        self.fields['last_date'].label = "Dead Line :"
        self.fields['url'].label = "Website :"


        self.fields['title'].widget.attrs.update(
            {
                'placeholder': 'eg : Starbucks',
            }
        )        
        self.fields['location'].widget.attrs.update(
            {
                'placeholder': 'eg : 1st Floor',
            }
        )
        self.fields['avg_spend'].widget.attrs.update(
            {
                'placeholder': '€5 - €150',
            }
        )                 
        self.fields['last_date'].widget.attrs.update(
            {
                'placeholder': 'YYYY-MM-DD ',
            }
        )            
        self.fields['url'].widget.attrs.update(
            {
                'placeholder': 'https://example.com',
            }
        )    

    
        last_date = forms.CharField(widget=forms.TextInput(attrs={
                    'placeholder': 'Service Name',
                    'class' : 'datetimepicker1'
                }))

    class Meta:
        model = Shop

        fields = [
            "title",
            "location",
            "shop_type",
            "category",
            "avg_spend",
            "description",
            "last_date",
            "url"
            ]

    def save(self, commit=True):
        shop = super(ShopEditForm, self).save(commit=False)
      
        if commit:
            shop.save()
        return shop

