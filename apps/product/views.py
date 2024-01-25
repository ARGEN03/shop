from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from rest_framework.pagination import PageNumberPagination
from .serializers import ProductSerializer
from .models import Product
from .permissions import IsOwner
from apps.rating.serializers import RatingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response



# Create your views here.
class StandartResultPaginations(PageNumberPagination):
    page_size =10
    page_query_param = 'page'


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = StandartResultPaginations


    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_permissions(self):
        if self.request.method in ['PATCH', 'PUT', 'DELETE']:
            return [IsOwner()]
        else:
            return [permissions.IsAuthenticatedOrReadOnly()]
        
    @action(['GET', 'POST', 'PATCH', 'PUT', 'DELETE'], detail=True)
    def rating(self, request, pk):
        product = self.get_object()
        user = request.user

        if request.method == 'GET':
            ratings = product.rating.all()
            serialiazer = RatingSerializer(ratings, many=True)

            return Response(serialiazer.data, 200)
        
        elif request.method == 'POST':
            serialiazer = RatingSerializer(data=request.data)
            serialiazer.is_valid(raise_exception=True)
            serialiazer.save(owner=user, product=product)
            return Response(serialiazer.data, 201)
        
        elif request.method in['PATCH', 'PUT']:
            if not product.ratings.filter(owner=user).exists():
                return Response('Ты не оставлял рейтинг на этот продукт!', 400)
            rating = product.ratings.get(owner=user)
            serialiazer = RatingSerializer(rating, data=request.data, partial=True)
            serialiazer.is_valid(raise_exception=True)
            serialiazer.save()
            return Response(serialiazer.data, 200)
        
        else:
            if not product.ratings.filter(owner=user).exists():
                return Response('Ты не оставлял рейтинг на этот продукт!', 400)
            rating = product.ratings.get(owner=user)
            rating.delete()
            return Response('Удалено', 204)



