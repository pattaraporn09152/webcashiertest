from django import forms

from .models import *


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