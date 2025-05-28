from .models import Author

class AuthorRepository:
    def create_author(self, author_data):
        return Author.objects.create(**author_data)

    def get_author_by_id(self, authorid):
        try:
            return Author.objects.get(authorid=authorid, is_deleted=False)
        except Author.DoesNotExist:
            return None

    def get_all_authors(self):
        return Author.objects.filter(is_deleted=False)

    def update_author(self, authorid, updated_data):
            author = self.get_author_by_id(authorid)
            if not author:
                return None

            for key, value in updated_data.items():
                setattr(author, key, value)

            author.save()  # Save changes
            return author

    def delete_author(self, authorid):
        author = self.get_author_by_id(authorid)
        if not author:
            return None

        author.is_deleted = True  # Soft delete
        author.save()
        return author
