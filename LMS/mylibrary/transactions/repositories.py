from .models import Transaction

class TransactionRepository:
    def create_transaction(self, transaction_data):
        return Transaction.objects.create(**transaction_data)

    def get_transaction_by_id(self, transaction_id):
        try:
            return Transaction.objects.get(transaction_id=transaction_id, is_deleted=False)
        except Transaction.DoesNotExist:
            return None

    def get_all_transactions(self):
        return Transaction.objects.filter(is_deleted=False)

    def update_transaction(self, transaction_id, updated_data):
        transaction = self.get_transaction_by_id(transaction_id)
        if not transaction:
            return None

        for key, value in updated_data.items():
            setattr(transaction, key, value)

        transaction.save()  # Save changes
        return transaction

    def delete_transaction(self, transaction_id):
        transaction = self.get_transaction_by_id(transaction_id)
        if not transaction:
            return None

        transaction.is_deleted = True
        transaction.save()
        return transaction
