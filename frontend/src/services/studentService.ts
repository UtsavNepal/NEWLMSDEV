import { Student } from '../types/student';
import apiClient from './tokenManagement/apiClient';

export const fetchStudents = async (): Promise<Student[]> => {
  const response = await apiClient.get<Student[]>('/student/');
  return response.data;
};

export const createStudent = async (student: Student): Promise<Student> => {
  const response = await apiClient.post<Student>('/student/', student);
  return response.data;
};

export const updateStudent = async (student: Student): Promise<void> => {
  await apiClient.put(`/student/${student.studentid}/`, student);
};

export const deleteStudent = async (studentId: number): Promise<void> => {
  await apiClient.delete(`/student/${studentId}/`);
};