import requests
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated

from account.models import *
from orders.models import Order, Orderaddress ,orderapprovals
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

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdetails
        fields = ('about', 'description', 'size', 'variant', 'SKU')


class ProductimageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productimage
        fields = ('image',)


class productsSerialzier(serializers.ModelSerializer):
    category=serializers.SlugRelatedField(slug_field='name',queryset=Category.objects.all())
    productdetail = ProductDetailSerializer()
    productimg = ProductimageSerializer(many=True, required=False)
    mainimage = serializers.ImageField(required=False)
    seller = serializers.SlugRelatedField(slug_field='username',queryset=CustomerUser.objects.all())
    sellerid = serializers.IntegerField(source='seller.id')

    class Meta:
        model = Product
        fields = '__all__'


    def create(self, validated_data):
        name = validated_data.pop('name')
        productdetail_data = validated_data.pop('productdetail')
        productimage_data = validated_data.pop('productimg', [])

        product = Product.objects.create(name=name, **validated_data)
        Productdetails.objects.create(product=product, **productdetail_data)

        for productimg in productimage_data:
            Productimage.objects.create(product=product, **productimg)

        return product

    def update(self, instance, validated_data):
        name = validated_data.get('name', instance.name)
        img = validated_data.get('mainimage', instance.mainimage)
        productdetail_data = validated_data.get('productdetail', {})
        productimage_data = validated_data.get('productimg', [])

        instance.name = name
        instance.mainimage = img
        instance.save()

        productdetail = instance.productdetail
        for attr, value in productdetail_data.items():
            setattr(productdetail, attr, value)
        productdetail.save()

        existing_product_images = instance.productimg.all()
        existing_image_ids = [image.id for image in existing_product_images]

        for productimg in productimage_data:
            image_id = productimg.get('id')
            if image_id and image_id in existing_image_ids:
                image_instance = Productimage.objects.get(id=image_id, product=instance)
                image_instance.image = productimg.get('image', image_instance.image)
                image_instance.save()
            else:
                product_img = Productimage.objects.create(product=instance, **productimg)
                existing_image_ids.append(product_img.id)

        # Delete any existing images not present in the updated data
        instance.productimg.exclude(id__in=existing_image_ids).delete()

        return instance


class selleraprrovalserialzier(serializers.ModelSerializer):
    # seller = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    class Meta:
        model = orderapprovals
        fields = '__all__'

class DeliveryAddressser(serializers.ModelSerializer):
    class Meta:
        model = Orderaddress
        fields = '__all__'

# Orderdisplay
class OrderSerializer(serializers.ModelSerializer):
    sellerstatus = selleraprrovalserialzier(many=True)
    customer = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S %p')

    class Meta:
        model = Order
        fields = '__all__'





class FullorderdetailSerializer(serializers.ModelSerializer):
    sellerstatus = selleraprrovalserialzier(many=True)
    orderaddress = DeliveryAddressser(many=True)
    customer = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    created_at = serializers.DateTimeField(format='%d-%m-%Y %H:%M:%S %p')

    class Meta:
        model = Order
        fields = '__all__'