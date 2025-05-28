from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer
from .services import StudentService

class StudentViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    def create(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            service = StudentService()
            student = service.add_student(serializer.validated_data)
            return Response(StudentSerializer(student).data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        service = StudentService()
        student = service.get_student_detail(pk)
        if isinstance(student, dict):
            return Response(student, status=status.HTTP_404_NOT_FOUND)
        return Response(StudentSerializer(student).data)

    def update(self, request, pk=None):
        service = StudentService()
        updated_data = request.data
        student = service.update_student(pk, updated_data)
        if isinstance(student, dict):
            return Response(student, status=status.HTTP_404_NOT_FOUND)
        return Response(StudentSerializer(student).data)

    def destroy(self, request, pk=None):
        service = StudentService()
        result = service.delete_student(pk)
        if isinstance(result, dict) and "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def list(self, request):
        service = StudentService()
        students = service.get_all_students()
        return Response(StudentSerializer(students, many=True).data)
