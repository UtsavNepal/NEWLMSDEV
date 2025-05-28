from django.core.mail import send_mail

class EmailHelper:
    @staticmethod
    def send_email(subject, message, recipient_email):
        send_mail(
            subject,
            message,
            "aayushbajracharya90@gmail.com",  # From email (update this)
            [recipient_email],
            fail_silently=False,  # If set to True, Django won't raise an error if email sending fails
        )
