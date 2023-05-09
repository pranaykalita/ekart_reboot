from rest_framework import serializers

from account.models import *
from products.models import *


###################################################
# Simple Account Serializer
###################################################
class AccountDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customerdetail
        fields = '__all__'


class AccountSerializer(serializers.ModelSerializer):
    customer = AccountDataSerializer()

    class Meta:
        model = CustomerUser
        exclude = ('password', 'user_permissions', 'groups',)


###################################################
# create Acccount [default CUSTOMER else Seller ]
###################################################

class CreateaccountSerializer(serializers.ModelSerializer):
    is_seller = serializers.BooleanField(required=False)

    class Meta:
        model = CustomerUser
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_seller', 'is_customer',)

    def create(self, validated_data):
        password = validated_data.pop('password')
        is_seller = validated_data.pop('is_seller', False)
        is_customer = validated_data.pop('is_customer', True)
        if (is_seller == True):
            is_seller = validated_data.pop('is_seller', True)
            is_customer = validated_data.pop('is_customer', False)
        user = CustomerUser.objects.create_customer(password=password, is_seller=is_seller, is_customer=is_customer, **validated_data)
        return user


class AccountRetriveSerializer(serializers.ModelSerializer):
    customer = AccountDataSerializer()

    class Meta:
        model = CustomerUser
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'customer', 'is_seller', 'is_customer',)


###################################################
# Category Serialziers
###################################################


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name',)


class SubCategorySerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())

    class Meta:
        model = Subcategory
        fields = ('id', 'category', 'name',)


###################################################
# Products Serialziers
##################################################

class ProductSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    subcategory = serializers.SlugRelatedField(slug_field='name', queryset=Subcategory.objects.all())

    class Meta:
        model = Product
        fields = '__all__'

#
# class productImgSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Productimage
#         fields = ('image',)
#
# class productDataSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Productdetails
#         fields = '__all__'
#
# class ProductSerializer(serializers.ModelSerializer):
#
#     category = serializers.CharField(source='category.name')
#     subcategory = serializers.CharField(source='subcategory.name')
#
#     about = serializers.CharField(source='productdetail.about')
#     description = serializers.CharField(source='productdetail.description')
#     size = serializers.CharField(source='productdetail.size')
#     variant = serializers.CharField(source='productdetail.variant')
#     SKU = serializers.CharField(source='productdetail.SKU')
#
#     productimg = productImgSerializer(many=True)
#
#     class Meta:
#         model = Product
#         fields = '__all__'
#
#     def get_category(self, obj):
#         return CategorySerializer(obj.category).data
#
#     def get_subcategory(self, obj):
#         return SubCategorySerializer(obj.subcategory).data
#
