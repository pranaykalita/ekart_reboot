from rest_framework import serializers

from cart.models import *
from orders.models import *
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
    category = categoryOnlySerializer()
    subcategory = subcategorySerializer()

    productdetail = ProductdetailsSerializer()
    seller = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    sellerid = serializers.IntegerField(source='seller.id')

    class Meta:
        model = Product
        fields = ['id', 'name', 'price', 'quantity', 'category', 'subcategory', 'seller',
                  'sellerid', 'productdetail', 'mainimage']


# Single Product
class singleProductSerializer(serializers.ModelSerializer):
    productdetail = ProductdetailsSerializer()
    productimg = ProductimagesSerializer(many=True)
    seller = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    category = categoryOnlySerializer()
    subcategory = subcategorySerializer()

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'quantity', 'seller', 'category', 'subcategory', 'productdetail', 'mainimage', 'productimg',)


###################### CART ######################

class CartProductsSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(slug_field='name', queryset=Category.objects.all())
    subcategory = serializers.SlugRelatedField(slug_field='name', queryset=Subcategory.objects.all())
    productdetail = ProductdetailsSerializer()
    seller = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())

    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'seller', 'mainimage', 'category', 'subcategory', 'productdetail')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class cartitemsSerializer(serializers.ModelSerializer):
    product = CartProductsSerializer(many=False)
    itemtotal = serializers.SerializerMethodField(method_name="total")

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'quantity', 'itemtotal']

    def total(self, cartitems: CartItem):
        total = cartitems.quantity * cartitems.product.price
        return total


class CartDataSerializer(serializers.ModelSerializer):
    id = serializers.UUIDField(read_only=True)
    items = cartitemsSerializer(many=True)
    Subtotal = serializers.SerializerMethodField(method_name='grandtotal')

    class Meta:
        model = Cart
        fields = ['id', 'customer', 'items', "Subtotal"]

    def grandtotal(self, cart: Cart):
        items = cart.items.all()
        sum = 0
        for item in items:
            sum += item.quantity * item.product.price
        return sum


####################


class Orderserializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Order
        fields = '__all__'
#######################################################
class SellersstatusSer(serializers.ModelSerializer):
    seller = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    class Meta:
        model = orderapprovals
        fields = '__all__'

class DeliveryAddressser(serializers.ModelSerializer):
    class Meta:
        model = Orderaddress
        fields = '__all__'

class AllorderSerializer(serializers.ModelSerializer):
    sellerstatus = SellersstatusSer(many=True)
    customer = serializers.SlugRelatedField(slug_field='username', queryset=CustomerUser.objects.all())
    orderaddress = DeliveryAddressser(many=True)
    class Meta:
        model = Order
        fields = '__all__'