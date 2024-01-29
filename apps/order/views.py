from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import OrderSerializer
from .models import Order

# Create your views here.
class OrderAPIView(ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        user = request.user
        orders = user.orders.all()
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data, 200)


