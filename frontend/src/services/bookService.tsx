import { Book } from '../types/books';
import apiClient from './tokenManagement/apiClient';

export const fetchBooks = async (): Promise<Book[]> => {
  const response = await apiClient.get<Book[]>('/books/');
  return response.data;
};

export const createBook = async (book: Book): Promise<Book> => {
  const response = await apiClient.post<Book>('/books/', book);
  return response.data;
};

export const updateBook = async (book: Book): Promise<void> => {
  await apiClient.put(`/books/${book.bookid}/`, book);
};

export const deleteBook = async (bookId: number): Promise<void> => {
  await apiClient.delete(`/books/${bookId}/`);
};