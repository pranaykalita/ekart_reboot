from django.db.models import Q
from rest_framework.authentication import SessionAuthentication
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, UpdateModelMixin, CreateModelMixin
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

from .serializers import *
from .tests import MultipleFieldLookupORMixin

# pagination


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

class cartListView(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset =Cart.objects.all()
    serializer_class = CartSerializer
    authentication_classes = [SessionAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)


class cartRetriveView(RetrieveModelMixin, MultipleFieldLookupORMixin, GenericAPIView):
    queryset =Cart.objects.all()
    serializer_class = CartDataSerializer
    lookup_field = lookup_fields = ('id', 'customer')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class orderlist(ListModelMixin,GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = Orderserializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class orderRetrive(RetrieveModelMixin,MultipleFieldLookupORMixin,GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = Orderserializer
    lookup_field = lookup_fields = ('id', 'customer')

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)



class allorderView(ListModelMixin,GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = AllorderSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class RetriveorderView(RetrieveModelMixin,GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = AllorderSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)