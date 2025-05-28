import { FormEvent, useEffect, useState } from "react";
import { Student } from "../../types/student";


interface StudentFormProps {
  student?: Student | null;
  isEdit: boolean;
  onSubmit: (student: Student) => void;
}

const StudentForm: React.FC<StudentFormProps> = ({ student, isEdit, onSubmit }) => {
  const [formData, setFormData] = useState<Student>({
    studentid: 0,
    name: "",
    email: "",
    contact_no: "",
    faculty: "",
  });

  useEffect(() => {
    if (student) {
      setFormData(student);
    }
  }, [student]);

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData((prev) => ({ ...prev, [name]: value }));
  };

  return (
    <div className="bg-[#E3E3E3] p-6 rounded-lg shadow-md mb-4">
      <form onSubmit={handleSubmit}>
        <input type="hidden" name="studentId" value={formData.studentid} />
        <div className="mb-3">
          <label className="text-sm font-medium">Student Name</label>
          <input type="text" name="name" value={formData.name} onChange={handleChange} required className="w-full p-2 bg-gray-200 rounded-md" />
        </div>
        <div className="mb-3">
          <label className="text-sm font-medium">Email</label>
          <input type="email" name="email" value={formData.email} onChange={handleChange} required className="w-full p-2 bg-gray-200 rounded-md" />
        </div>
        <div className="grid grid-cols-2 gap-4 mb-3">
          <div>
            <label className="text-sm font-medium">Contact Number</label>
            <input type="text" name="contact_no" value={formData.contact_no} onChange={handleChange} required className="w-full p-2 bg-gray-200 rounded-md" />
          </div>
          <div>
            <label className="text-sm font-medium">Department</label>
            <input type="text" name="faculty" value={formData.faculty} onChange={handleChange} required className="w-full p-2 bg-gray-200 rounded-md" />
          </div>
        </div>
        <button type="submit" className="bg-[#255D81] text-white px-5 py-2 rounded-md">
          {isEdit ? "Update Student" : "Add Student"}
        </button>
      </form>
    </div>
  );
};

export default StudentForm;