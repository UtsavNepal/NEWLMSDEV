import { Author } from '../types/authors';
import apiClient from './tokenManagement/apiClient';

export const getAuthors = async (): Promise<Author[]> => {
  const response = await apiClient.get<Author[]>('/Author/');  
  return response.data;
};

export const addAuthor = async (author: Author): Promise<Author> => {
  const response = await apiClient.post<Author>('/Author/', author); 
  return response.data;
};

export const updateAuthor = async (author: Author): Promise<void> => {
  await apiClient.put(`/Author/${author.authorid}/`, author); 
};

export const deleteAuthor = async (authorID: number): Promise<void> => {
  await apiClient.delete(`/Author/${authorID}/`);  
};