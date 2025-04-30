from rest_framework.response import Response
from rest_framework.views import APIView
from .models import * 
from .serializers import ProductSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
# Create your views here.


class Productclass(APIView):
    
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]

    def get(self,request):
        products = Product.objects.all()
        serializer = ProductSerializer(products,many=True)
        return Response(
            {
                "status":True,
                "data": serializer.data
            }
        )
