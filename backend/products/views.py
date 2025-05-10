from rest_framework import viewsets, permissions
from .models import HVACProduct
from .serializers import HVACProductSerializer

class HVACProductViewSet(viewsets.ModelViewSet):
    queryset = HVACProduct.objects.all()
    serializer_class = HVACProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # Allow read-only access to unauthenticated users
        if self.action in ['list', 'retrieve']:
            return [permissions.AllowAny()]
        return [permissions.IsAdminUser()]
