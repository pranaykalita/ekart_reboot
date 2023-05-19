from rest_framework import serializers

from account.models import *
from cart.models import *
from products.models import *


###################### Accounts ######################

# account data
class accountdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customerdetail
        fields = ('profileimg',)


# account Display
class accountSerializer(serializers.ModelSerializer):
    profileImage = accountdetailsSerializer(source='customer')

    class Meta:
        model = CustomerUser
        fields = ['username', 'email', 'profileImage']


###################### Category ######################

# subcategory
class subcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Subcategory
        fields = ['id', 'name']


# category
class categorySerializer(serializers.ModelSerializer):
    subcategory = subcategorySerializer(many=True)

    class Meta:
        model = Category
        fields = ['id', 'name', 'subcategory']


class categoryOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


###################### Products ######################

# productDetails
class ProductdetailsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productdetails
        fields = ['about', 'description', 'size', 'variant', 'SKU']


class ProductimagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productimage
        fields = ['image']


# product Images
class ProductSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField()
    subcategory = serializers.StringRelatedField()
    productdetail = ProductdetailsSerializer()
    seller = serializers.SlugRelatedField(slug_field='username',queryset=CustomerUser.objects.all())

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'category', 'subcategory','seller', 'productdetail', 'mainimage']


# Single Product
class singleProductSerializer(serializers.ModelSerializer):
    productdetail = ProductdetailsSerializer()
    productimg = ProductimagesSerializer(many=True)

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'category', 'subcategory', 'productdetail', 'mainimage', 'productimg',)


###################### CART ######################
# Product for Cart
class SimpelItemdetailserializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'price', 'mainimage']


# cart
class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id', 'customer']


# cart Items
class CartItemsSerialzier(serializers.ModelSerializer):
    product = SimpelItemdetailserializer()

    class Meta:
        model = CartItem
        fields = ['product', 'quantity', 'total']


class CartDataSerializer(serializers.ModelSerializer):
    items = CartItemsSerialzier(many=True)
    subtotal = serializers.SerializerMethodField(method_name='sub_total')

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items', 'subtotal']

    def sub_total(self, cart: Cart):
        items = cart.items.all()
        sum = 0
        for item in items:
            sum += item.quantity * item.product.price
        return sum
