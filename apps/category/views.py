from rest_framework.viewsets import ModelViewSet
from .serializers import CategorySerializer
from .models import Category
from rest_framework import permissions

# Create your views here.
class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAdminUser()]
        
    