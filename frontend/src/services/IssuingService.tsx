import { IssuingTransaction } from '../types/issuing';
import apiClient from './tokenManagement/apiClient';

export const createTransaction = async (transaction: IssuingTransaction): Promise<number> => {
  const response = await apiClient.post('/transactions/', transaction);
  return response.data;
};