from rest_framework import serializers
from Webcashier.models import *

from .models import *



# class GenderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gender
#         fields = ( 'Gid', 'name', )

class IncustumerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incustumer
        fields = ( 'face_id', 'first_name', 'last_name', 'phone' , 
                    'birth_day','gender',  'age',  'email',
                     'career',  )

# class OrderSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Order
#         fields = ( 'Oid', 'information', 'list_Order', 
#                      'number_Order' , 'point','created_at', )
 

# class ImageSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Image
#         fields = ( 'Mid', 'information', 'imageInfo', )  


# class StaffSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Staff
#         fields = ( 'Sid', ' password', 'first_name',
#                     'last_name','gender', )  

# class RecommendSerializer(serializers.ModelSerializer):

#     class Meta:
#         model = Recommend
#         fields = ( 
#                 'Rid', 'information', 'Order',
#                 )
