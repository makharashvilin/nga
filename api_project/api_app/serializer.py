from datetime import datetime

from django.template.defaultfilters import upper
from rest_framework import serializers
from .models import Post, Category



class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields = '__all__'
    def create(self, validated_data):
        instance = super().create(validated_data)
        instance.create_date = datetime.now()
        instance.title = instance.title.upper()
        print(instance.title)
        return instance


    def update(self, instance, validated_data):
        instance = super().update(instance, validated_data)
        instance.write_date = datetime.now()
        instance.edited = True
        return instance



class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model=Category
        fields = '__all__'
        # depth = 1