from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination

from .models import *
from .serializers import *
from .filters import *
# Create your views here.


@api_view(['GET'])
def get_all_products(request):

    filterset = ProductsFilter(request.GET , queryset=Product.objects.all().order_by('id'))
    paginator = PageNumberPagination()
    paginator.page_size = 3
    queryset = paginator.paginate_queryset(filterset.qs , request)
    serializer = ProductSerializer(queryset , many=True)

    return Response({"products":serializer.data})



@api_view(['GET'])
def get_by_id_product(request , pk):
    products= get_object_or_404(Product , id=pk)
    serializer = ProductSerializer(products , many=False)
    return Response({"product":serializer.data})









#serializer = ProductSerializer(products , many=True)
#products = Product.objects.all()