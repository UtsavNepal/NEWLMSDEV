export interface Dashboard {
  total_student_count: number;
  total_book_count: number;
  total_transaction_count: number;
  total_borrowed_books: number;
  total_returned_books: number;
}

export interface OverdueBorrower {
  student_name: string; // Match backend field name
  borrowed_id: string;  // Match backend field name
}