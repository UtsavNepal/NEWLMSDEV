import { Dashboard, OverdueBorrower } from '../types/dashboard';
import apiClient from './tokenManagement/apiClient';

export const getDashboardData = async (): Promise<Dashboard> => {
  const response = await apiClient.get<Dashboard>('/dashboard');
  return response.data;
};

export const getOverdueBorrowers = async (): Promise<OverdueBorrower[]> => {
  const response = await apiClient.get<OverdueBorrower[]>('/dashboard/GetOverdueBorrowers');
  return response.data;
};