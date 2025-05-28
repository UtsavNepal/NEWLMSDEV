from .repositories import AuthorRepository

class AuthorService:
    def __init__(self):
        self.repo = AuthorRepository()

    def add_author(self, author_data):
        return self.repo.create_author(author_data)

    def get_author_detail(self, authorid):
        author = self.repo.get_author_by_id(authorid)
        if not author:
            return {"error": "Author not found"}
        return author

    def get_all_authors(self):
        return self.repo.get_all_authors()

    def update_author(self, authorid, updated_data):
        author = self.repo.get_author_by_id(authorid)
        if not author:
            return {"error": "Author not found"}

        updated_author = self.repo.update_author(authorid, updated_data)
        return updated_author

    def delete_author(self, authorid):
        author = self.repo.get_author_by_id(authorid)
        if not author:
            return {"error": "Author not found"}

        self.repo.delete_author(authorid)
        return {"message": "Author deleted successfully"}
