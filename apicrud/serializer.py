from rest_framework import serializers

from category.models import Category, Subcategory
from products.models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name',)


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Subcategory
        fields = ('category', 'name',)

class productImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productimage
        fields = ('image',)

class productDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdetails
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):

    category = serializers.CharField(source='category.name')
    subcategory = serializers.CharField(source='subcategory.name')

    about = serializers.CharField(source='productdetail.about')
    description = serializers.CharField(source='productdetail.description')
    size = serializers.CharField(source='productdetail.size')
    variant = serializers.CharField(source='productdetail.variant')
    SKU = serializers.CharField(source='productdetail.SKU')

    productimg = productImgSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'

    def get_category(self, obj):
        return CategorySerializer(obj.category).data

    def get_subcategory(self, obj):
        return SubCategorySerializer(obj.subcategory).data

