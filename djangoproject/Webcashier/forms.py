from django import forms

from .models import *

# อ้างอิง - https://docs.djangoproject.com/en/3.0/topics/forms/modelforms/


class OrderForm(forms.ModelForm):

    class Meta:
        model = Order
        fields = ['Oid', 'list_Order', 'sum_Order', 'point', 'sum_price',  ]


class RegisterForm(forms.ModelForm):

    class Meta:
        model = Incustumer
        fields = (
            'face_id',
            'first_name',
            'last_name',
            'phone',
            'gender',
            'age',
            'email',
            'career',
            'imageInfo',
            'imageInfo2',
           
        )

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
