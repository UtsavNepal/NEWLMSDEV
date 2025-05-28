from .repositories import TransactionRepository

class TransactionService:
    def __init__(self):
        self.repo = TransactionRepository()

    def add_transaction(self, transaction_data):
        return self.repo.create_transaction(transaction_data)

    def get_transaction_detail(self, transaction_id):
        transaction = self.repo.get_transaction_by_id(transaction_id)
        if not transaction:
            return {"error": "Transaction not found"}
        return transaction

    def get_all_transactions(self):
        return self.repo.get_all_transactions()

    def update_transaction(self, transaction_id, updated_data):
        transaction = self.repo.get_transaction_by_id(transaction_id)
        if not transaction:
            return {"error": "Transaction not found"}

        updated_transaction = self.repo.update_transaction(transaction_id, updated_data)
        return updated_transaction

    def delete_transaction(self, transaction_id):
        transaction = self.repo.get_transaction_by_id(transaction_id)
        if not transaction:
            return {"error": "Transaction not found"}

        self.repo.delete_transaction(transaction_id)
        return {"message": "Transaction deleted successfully"}
