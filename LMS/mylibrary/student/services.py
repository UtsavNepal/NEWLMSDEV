from .repositories import StudentRepository

class StudentService:
    def __init__(self):
        self.repo = StudentRepository()

    def add_student(self, student_data):
        return self.repo.create_student(student_data)

    def get_student_detail(self, studentid):
        student = self.repo.get_student_by_id(studentid)
        if not student:
            return {"error": "Student not found"}
        return student

    def get_all_students(self):
        return self.repo.get_all_students()

    def update_student(self, studentid, updated_data):
        student = self.repo.get_student_by_id(studentid)
        if not student:
            return {"error": "Student not found"}

        updated_student = self.repo.update_student(studentid, updated_data)
        return updated_student

    def delete_student(self, studentid):
        student = self.repo.get_student_by_id(studentid)
        if not student:
            return {"error": "Student not found"}

        self.repo.delete_student(studentid)
        return {"message": "Student deleted successfully"}
