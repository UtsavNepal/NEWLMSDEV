from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import AuthorSerializer
from .services import AuthorService


class AuthorViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]
    

    def create(self, request):
        print("Request Data:", request.data)
        serializer = AuthorSerializer(data=request.data)
        if serializer.is_valid():
            service = AuthorService()
            author = service.add_author(serializer.validated_data)
            return Response(AuthorSerializer(author).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        service = AuthorService()
        author = service.get_author_detail(pk)
        if isinstance(author, dict):  # If error message is returned
            return Response(author, status=status.HTTP_404_NOT_FOUND)
        return Response(AuthorSerializer(author).data)

    def update(self, request, pk=None):
        service = AuthorService()
        updated_data = request.data
        author = service.update_author(pk, updated_data)
        if isinstance(author, dict):  # If error message is returned
            return Response(author, status=status.HTTP_404_NOT_FOUND)
        return Response(AuthorSerializer(author).data)

    def destroy(self, request, pk=None):
        service = AuthorService()
        result = service.delete_author(pk)
        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        service = AuthorService()
        authors = service.get_all_authors()
        return Response(AuthorSerializer(authors, many=True).data)
