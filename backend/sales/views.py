from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import SalesQuote, SalesQuoteItem
from .serializers import SalesQuoteSerializer, SalesQuoteItemSerializer

class SalesQuoteViewSet(viewsets.ModelViewSet):
    queryset = SalesQuote.objects.all()
    serializer_class = SalesQuoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Sales reps can only see their own quotes, admins see all
        user = self.request.user
        if user.is_staff or user.role == 'manager':
            return SalesQuote.objects.all()
        return SalesQuote.objects.filter(sales_rep=user)

    def perform_create(self, serializer):
        # Automatically assign the current user as sales rep
        serializer.save(sales_rep=self.request.user)

    @action(detail=True, methods=['POST'], permission_classes=[permissions.IsAuthenticated])
    def add_item(self, request, pk=None):
        quote = self.get_object()
        serializer = SalesQuoteItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(quote=quote)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['PATCH'], permission_classes=[permissions.IsAuthenticated])
    def update_status(self, request, pk=None):
        quote = self.get_object()
        quote.status = request.data.get('status', quote.status)
        quote.save()
        serializer = self.get_serializer(quote)
        return Response(serializer.data)
