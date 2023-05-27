from django.db.models import Prefetch
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin, RetrieveModelMixin

from api.tests import MultipleFieldLookupORMixin
from .serializer import *
from orders.models import *

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

class ProductsList(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = productsSerialzier

    def get_queryset(self):
        seller_id = self.request.query_params.get('seller_id')
        return Product.objects.filter(seller_id=seller_id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ProductDetail(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Product.objects.all()
    serializer_class = productsSerialzier
    lookup_field = 'id'

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class OrderList(ListModelMixin, MultipleFieldLookupORMixin, GenericAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    lookup_field = lookup_fields = ('id', 'seller')

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.order_by('-created_at')
        return queryset
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


# order by seller

class OrderBysellerView(ListModelMixin, GenericAPIView):
    serializer_class = OrderSerializer

    def get_queryset(self):
        seller_id = self.kwargs['seller_name']
        sellerno = self.request.session.get('sellerID')
        orders = Order.objects.all()
        orders = orders.order_by('-created_at')
        filtered_orders = []

        for order in orders:
            filtered_items = []

            for item in order.items:
                if item['product']['seller'] == seller_id:
                    filtered_items.append(item)

            if filtered_items:
                order.items = filtered_items
                filtered_sellerstatus = order.sellerstatus.filter(seller__seller=sellerno)

                if filtered_sellerstatus.exists():
                    filtered_order = order
                    filtered_order.sellerstatus.set(filtered_sellerstatus)
                    filtered_orders.append(filtered_order)

        return filtered_orders

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

# class OrderBysellerView(ListModelMixin,GenericAPIView):
#     serializer_class = OrderSerializer
#
#     def get_queryset(self):
#         seller_id = self.kwargs['seller_name']
#         orders = Order.objects.all()
#         orders = orders.order_by('-created_at')
#         filtered_orders = []
#
#         for order in orders:
#             filtered_items = []
#             for item in order.items:
#                 if item['product']['seller'] == seller_id:
#                     filtered_items.append(item)
#
#             if filtered_items:
#                 order.items = filtered_items
#                 filtered_orders.append(order)
#
#         return filtered_orders
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)


class OrderRetriveview(RetrieveModelMixin, GenericAPIView):
    serializer_class = FullorderdetailSerializer
    queryset = Order.objects.all()

    def get_object(self):
        seller_id = self.kwargs['seller_name']
        order_id = self.kwargs['id']
        orders = super().get_queryset()

        for order in orders:
            filtered_items = []
            for item in order.items:
                if item['product']['seller'] == seller_id:
                    filtered_items.append(item)

            if filtered_items and order.id == order_id:
                order.items = filtered_items
                return order

        return None

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

