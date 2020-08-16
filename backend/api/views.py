from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from api.serializers import CategorySerializer, ProductSerializer
from api.models import Category, Product


class CategoryViewSet(ViewSet):

    def list(self, request):
        queryset = Category.objects.order_by('pk')
        serializer = CategorySerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Category.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = CategorySerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        serializer = CategorySerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)


class ProductViewSet(ViewSet):

    def list(self, request):
        queryset = Product.objects.order_by('pk')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def retrieve(self, request, pk=None):
        queryset = Product.objects.all()
        item = get_object_or_404(queryset, pk=pk)
        serializer = ProductSerializer(item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        try:
            item = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        serializer = ProductSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def destroy(self, request, pk=None):
        try:
            item = Product.objects.get(pk=pk)
        except Product.DoesNotExist:
            return Response(status=404)
        item.delete()
        return Response(status=204)
