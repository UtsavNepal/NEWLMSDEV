export interface IssuingTransaction {
  user: string; // UUID from User model
  bookid: number; // Matches bookid in backend
  studentid: number; // Matches studentid in backend
  transaction_type: 'borrow' | 'return'; // Matches backend choices
  date: string; // ISO datetime string (e.g., "2025-05-24T13:19:00+0545")
}

export interface Student {
    studentid: number;
    name: string;
    email?: string;
    contact_no?: string;
    faculty?: string;
}
export interface Book {
    bookid: number;
    title: string;
    authorid?: number;
    genre?: string;
    isbn?: string;
    quantity?: number;
}