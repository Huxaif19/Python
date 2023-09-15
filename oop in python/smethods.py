class Book():
    def __init__(self, title , author , pages):
        self.author = author
        self.title = title
        self.pages = pages
    def __str__(self):
        return f"{self.title} by {self.author}"
    def __len__(self) :
        return self.pages
    def __del__(self) :
        print("book object deleted")
book = Book('life', 'huzaif', 89)
print(book, len(book))
del(book)