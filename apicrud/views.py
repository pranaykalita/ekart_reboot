from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from .serializer import *
from api.tests import MultipleFieldLookupORMixin

#########################################
# Account LIST API
#########################################


class AccountList(ListModelMixin, GenericAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = AccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class AccountDetail(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = AccountSerializer
    lookup_field = 'username'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


#########################################
# create ac by API
#########################################

class CreateAccountApi(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = CreateaccountSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class InsertAcoountDetail(RetrieveModelMixin, UpdateModelMixin, GenericAPIView):
    queryset = CustomerUser.objects.all()
    serializer_class = AccountRetriveSerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#########################################
# Category CRUD
#########################################

class CategoryList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class CategoryDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#########################################
# Subcategory CRUD
#########################################

class SubcategoryList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class SubcategoryDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Subcategory.objects.all()
    serializer_class = SubCategorySerializer
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


#########################################
# product CRUD
#########################################

class ProductsList(ListModelMixin,CreateModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = productsSerialzier

    def get_queryset(self):
        seller_id = self.request.query_params.get('seller_id')
        return Product.objects.filter(seller_id=seller_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class ProductDetail(RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin,GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = productsSerialzier
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

class OrderList(ListModelMixin,MultipleFieldLookupORMixin,GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerialzier
    lookup_field = lookup_fields = ('id', 'seller')
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)