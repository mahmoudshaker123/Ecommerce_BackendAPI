from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view  , permission_classes
from rest_framework.response import Response 
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated


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


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data = data)

    if  serializer.is_valid():
        product = Product.objects.create(**data , user=request.user)
        res = ProductSerializer(product , many=False)

        return Response({"product":res.data})

    else:
        return Response(serializer.errors)



@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data = data)

    if  serializer.is_valid():
        product = Product.objects.create(**data , user=request.user)
        res = ProductSerializer(product , many=False)

        return Response({"product":res.data})

    else:
        return Response(serializer.errors)






#serializer = ProductSerializer(products , many=True)
#products = Product.objects.all()