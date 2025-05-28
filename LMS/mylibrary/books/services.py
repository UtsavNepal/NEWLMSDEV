import logging
from .repositories import BookRepository

logger = logging.getLogger('student')

class BookService:
    def __init__(self):
        self.repo = BookRepository()

    def add_book(self, book_data):
        logger.info(f"Adding new book: {book_data}")
        return self.repo.create_book(book_data)

    def get_book_detail(self, bookid):
        logger.info(f"Fetching details for book ID: {bookid}")
        book = self.repo.get_book_by_id(bookid)
        if not book:
            logger.warning(f"Book ID {bookid} not found")
            return {"error": "Book not found"}
        return book

    def get_all_books(self):
        logger.info("Fetching all books")
        return self.repo.get_all_books()

    def update_book(self, bookid, updated_data):
        logger.info(f"Updating book ID {bookid} with data: {updated_data}")
        book = self.repo.get_book_by_id(bookid)
        if not book:
            logger.warning(f"Book ID {bookid} not found for update")
            return {"error": "Book not found"}

        updated_book = self.repo.update_book(bookid, updated_data)
        logger.info(f"Book ID {bookid} updated successfully")
        return updated_book

    def delete_book(self, bookid):
        logger.info(f"Attempting to delete book ID: {bookid}")
        book = self.repo.get_book_by_id(bookid)
        if not book:
            logger.warning(f"Book ID {bookid} not found for deletion")
            return {"error": "Book not found"}

        self.repo.delete_book(bookid)
        logger.info(f"Book ID {bookid} deleted successfully")
        return {"message": "Book deleted successfully"}