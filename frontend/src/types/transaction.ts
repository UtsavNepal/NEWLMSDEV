export interface Transaction {
  transaction_id: number; // Matches transaction_id
  user: string; // ForeignKey ID (UUID from User)
  bookid: number; // ForeignKey ID (integer from Book)
  studentid: number; // ForeignKey ID (integer from Student)
  transaction_type: 'borrow' | 'return';
  date: string; // ISO datetime string
  username?: string; // Read-only from serializer
  book_title?: string; // Read-only from serializer
  student_name?: string; // Read-only from serializer
}