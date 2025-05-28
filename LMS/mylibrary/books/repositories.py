from .models import Book
from .models import Author

class BookRepository:
    def create_book(self, book_data):
        return Book.objects.create(**book_data)

    def get_book_by_id(self, bookid):
        try:
            return Book.objects.get(bookid=bookid, is_deleted=False)
        except Book.DoesNotExist:
            return None

    def get_all_books(self):
        return Book.objects.filter(is_deleted=False)  # Fetch all non-deleted books

    def update_book(self, bookid, updated_data):
        book = self.get_book_by_id(bookid)  # Correctly fetch the book

        if not book:
            raise ValueError(f"Book with ID {bookid} does not exist")

        for key, value in updated_data.items():
            if key == "authorid":  # Ensure ForeignKey is assigned correctly
                try:
                    value = Author.objects.get(authorid=value)  # FIXED: Use correct primary key field
                except Author.DoesNotExist:
                    raise ValueError(f"Author with ID {value} does not exist")
            
            setattr(book, key, value)  # Update book attributes

        book.save()
        return book



    def delete_book(self, bookid):
        book = self.get_book_by_id(bookid)
        if not book:
            return None

        book.is_deleted = True  # Soft delete
        book.save()
        return book
