import logging
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import BookSerializer
from .services import BookService

logger = logging.getLogger('student')

class BookViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        logger.info("Received request to add a new book")
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            service = BookService()
            book = service.add_book(serializer.validated_data)
            logger.info(f"Book added successfully: {book}")
            return Response(BookSerializer(book).data, status=status.HTTP_201_CREATED)
        logger.error(f"Book creation failed: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        logger.info(f"Received request to retrieve book ID: {pk}")
        service = BookService()
        book = service.get_book_detail(pk)
        if isinstance(book, dict):
            logger.warning(f"Book ID {pk} not found")
            return Response(book, status=status.HTTP_404_NOT_FOUND)
        return Response(BookSerializer(book).data)

    def update(self, request, pk=None):
        logger.info(f"Received request to update book ID: {pk}")
        service = BookService()
        updated_data = request.data
        book = service.update_book(pk, updated_data)
        if isinstance(book, dict):
            logger.warning(f"Book ID {pk} not found for update")
            return Response(book, status=status.HTTP_404_NOT_FOUND)
        logger.info(f"Book ID {pk} updated successfully")
        return Response(BookSerializer(book).data)

    def destroy(self, request, pk=None):
        logger.info(f"Received request to delete book ID: {pk}")
        service = BookService()
        result = service.delete_book(pk)
        if isinstance(result, dict) and "error" in result:
            logger.warning(f"Book ID {pk} not found for deletion")
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        logger.info(f"Book ID {pk} deleted successfully")
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        logger.info("Received request to list all books")
        service = BookService()
        books = service.get_all_books()
        return Response(BookSerializer(books, many=True).data)