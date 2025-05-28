from .models import Student

class StudentRepository:
    def create_student(self, student_data):
        return Student.objects.create(**student_data)

    def get_student_by_id(self, studentid):
        try:
            return Student.objects.get(studentid=studentid, is_deleted=False)
        except Student.DoesNotExist:
            return None

    def get_all_students(self):
        return Student.objects.filter(is_deleted=False)

    def update_student(self, studentid, updated_data):
        student = self.get_student_by_id(studentid)
        if not student:
            return None

        for key, value in updated_data.items():
            setattr(student, key, value)

        student.save()
        return student

    def delete_student(self, studentid):
        student = self.get_student_by_id(studentid)
        if not student:
            return None

        student.is_deleted = True  # Soft Delete
        student.save()
        return student
