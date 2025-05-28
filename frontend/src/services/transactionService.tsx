import { Transaction } from '../types/transaction';
import apiClient from './tokenManagement/apiClient';

export const fetchTransactions = async (): Promise<Transaction[]> => {
  const response = await apiClient.get<Transaction[]>('/transactions/');
  return response.data;
};