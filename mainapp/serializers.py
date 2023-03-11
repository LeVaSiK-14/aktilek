from rest_framework import serializers
from mainapp.models import (
    School,Teacher,New,Rewiew,Galeria,
)




class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=Teacher
        fields=(
            'id', 'school', 'name', 'photo',
        )

class GaleriaSerializer(serializers.ModelSerializer):
    class Meta:
        model=Galeria
        fields=(
            'id', 'school', 'photo', 'name',
        )

class NewSerializer(serializers.ModelSerializer):
    # news= SchoolSerializer(many=True, read_only=True)
    class Meta:
        model=New
        fields = (
            'id', 'description', 'school', 'author','created_at', 'name' ,  'profile_pickture',  'photo', 'add_dates',
        )

class RewiewSerializer(serializers.ModelSerializer):
    class Meta:
        model=Rewiew
        fields = (
        'id','photo','parent', 'comment', 'name',
        )

class SchoolSerializer(serializers.ModelSerializer):
    news=NewSerializer(many=True, read_only=True)
    teachers=TeacherSerializer(many=True,read_only=True)
    galeries=GaleriaSerializer(many=True, read_only=True)
    rewiews=RewiewSerializer(many=True, read_only=True)
    class Meta:
        model=School
        fields=(
            'id','logo','whatsapp','twitter','facebook','name','description',\
            'admissiontouniversity','staff','students','successworkyear','mail',\
            'address', 'description_2', 'number_1', 'number_2', 'number_3', 'news',\
            'teachers', 'galeries', 'rewiews',
                
        )
        