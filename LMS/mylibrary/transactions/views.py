from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import TransactionSerializer
from .services import TransactionService

class TransactionViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        print("data:",request.data)
        serializer = TransactionSerializer(data=request.data)

        if serializer.is_valid():
            service = TransactionService()
            transaction = service.add_transaction(serializer.validated_data)
            return Response(TransactionSerializer(transaction).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        service = TransactionService()
        transaction = service.get_transaction_detail(pk)
        if isinstance(transaction, dict):  # If error message is returned
            return Response(transaction, status=status.HTTP_404_NOT_FOUND)
        return Response(TransactionSerializer(transaction).data)

    def update(self, request, pk=None):
        service = TransactionService()
        transaction = service.get_transaction_detail(pk)
        if isinstance(transaction, dict):  # If transaction not found
            return Response(transaction, status=status.HTTP_404_NOT_FOUND)
        
        # Validate data using the serializer
        serializer = TransactionSerializer(transaction, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        # Pass validated data to service
        updated_transaction = service.update_transaction(pk, serializer.validated_data)
        return Response(TransactionSerializer(updated_transaction).data)

    def destroy(self, request, pk=None):
        service = TransactionService()
        result = service.delete_transaction(pk)
        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        return Response({"message": "Transaction soft deleted successfully"}, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        service = TransactionService()
        transactions = service.get_all_transactions()
        return Response(TransactionSerializer(transactions, many=True).data)
