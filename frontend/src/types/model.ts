export interface User {
  userId?: string; // Use string to match UUID format, optional for signup
  user_name: string;
  email: string;
  role: 'librarian' | 'admin';
  password?: string; // Optional for signup
}
export interface LoginDTO {
  user_name: string;
  password: string;
}
export interface Tokens {
  accessToken: string;
  refreshToken: string;
  userId: string; // Update to string to match UUID
}