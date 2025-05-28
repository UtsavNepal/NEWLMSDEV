from .repositories import DashboardRepository
from .utils.email_helper import EmailHelper

class DashboardService:
    def __init__(self, dashboard_repo: DashboardRepository):
        """Injecting the repository into the service"""
        self.repository = dashboard_repo

    def get_dashboard_data(self):
        return {
            'total_student_count': self.repository.get_total_students(),
            'total_book_count': self.repository.get_total_books(),
            'total_transaction_count': self.repository.get_total_transactions(),
            'total_borrowed_books': self.repository.get_borrowed_books_count(),
            'total_returned_books': self.repository.get_returned_books_count(),
        }
    
    def get_overdue_borrowers(self):
        return self.repository.get_overdue_borrowers()
    
    def email_get_overdue_borrowers(self):
        overdue_borrowers = self.repository.get_overdue_borrowers()

        for borrower in overdue_borrowers:
            subject = "Library Overdue Notice"
            message = (
                f"Dear {borrower.student.name},\n\n"
                "Our records show that you have an overdue book borrowed from the library. "
                "Please return it as soon as possible to avoid penalties.\n\n"
                "Thank you."
            )
            recipient_email = borrower.student.email

            # Use EmailHelper
            EmailHelper.send_email(subject, message, recipient_email)

        return overdue_borrowers
