from django.db.models import Q
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin

from .serializers import *
from .tests import MultipleFieldLookupORMixin


##################### ACCOUNT #####################

# accounts LIST
class AccountsList(ListModelMixin, GenericAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = accountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


##################### CATEGORY AND SUB #####################

# Category and SubCategory
class CategorySubList(ListModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = categorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class CategoryList(ListModelMixin,GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = categoryOnlySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class SubcategoryList(ListModelMixin,GenericAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = subcategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


##################### PRODUCT #####################

# List All Products Filter By Category,SubCategory,Size,Variants
class ProductList(ListModelMixin, MultipleFieldLookupORMixin, GenericAPIView):
    serializer_class = ProductSerializer
    lookup_field = ('category__name', 'subcategory__name', 'productdetail__size', 'productdetails__variant')

    def get_queryset(self):
        keyword = self.request.query_params.get('filter', None)
        if keyword:
            search = Q(category__name=keyword) | Q(subcategory__name=keyword) | Q(productdetail__size=keyword) | Q(productdetail__variant=keyword)
            queryset = Product.objects.filter(search).all()
        else:
            queryset = Product.objects.all()
        return queryset

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# List Single Product By product ID
class ProductRetrive(RetrieveModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = singleProductSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


##################### CART #####################

# Carts
class CartList(ListModelMixin, GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# display cart Items
class CartRetrive(RetrieveModelMixin, GenericAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartDataSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)