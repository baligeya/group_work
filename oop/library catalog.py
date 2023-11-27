class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        return f"{self.title} by {self.author} ({'Available' if self.available else 'Not Available'})"


class Catalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Invalid book object")
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def display_catalog(self):
        for book in self.books:
            print(book)


class LibraryMember:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.available:
            book.available = False
            self.borrowed_books.append(book)
            print(f"{self.name} has successfully borrowed {book.title}.")
        else:
            print(f"Sorry, {book.title} is not available for borrowing.")

    def return_book(self, book):
        if book in self.borrowed_books:
            book.available = True
            self.borrowed_books.remove(book)
            print(f"{self.name} has successfully returned {book.title}.")
        else:
            print(f"{self.name} did not borrow {book.title} or the book was already returned.")


class VirtualLibrary(Catalog):
    def __init__(self):
        super().__init__()
        self.members = []

    def add_member(self, member):
        if not isinstance(member, LibraryMember):
            raise ValueError("Invalid member object")
        self.members.append(member)

    def display_members(self):
        print("\nLibrary Members:")
        for member in self.members:
            print(member.name)

    def display_borrowed_books(self, member_name):
        member = next((m for m in self.members if m.name == member_name), None)
        if member:
            print(f"\nBooks borrowed by {member_name}:")
            for book in member.borrowed_books:
                print(book)
        else:
            print(f"Member {member_name} not found.")

    def simulate_library(self):
        member_name = input("Enter your name: ")
        member = LibraryMember(member_name)
        self.add_member(member)

        while True:
            print("\n===== Virtual Library Menu =====")
            print("1. Add Book")
            print("2. Search by Title")
            print("3. Search by Author")
            print("4. Display Catalog")
            print("5. Borrow Book")
            print("6. Return Book")
            print("7. Display Members")
            print("8. Display Borrowed Books")
            print("0. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                title = input("Enter the book title: ")
                author = input("Enter the author's name: ")
                new_book = Book(title, author)
                self.add_book(new_book)
                print(f"Book '{title}' by {author} added successfully.")

            elif choice == "2":
                search_title = input("Enter the title to search: ")
                results = self.search_by_title(search_title)
                if results:
                    print("Search Results:")
                    for book in results:
                        print(book)
                else:
                    print("No matching books found.")

            elif choice == "3":
                search_author = input("Enter the author's name to search: ")
                results = self.search_by_author(search_author)
                if results:
                    print("Search Results:")
                    for book in results:
                        print(book)
                else:
                    print("No matching books found.")

            elif choice == "4":
                print("\nLibrary Catalog:")
                self.display_catalog()

            elif choice == "5":
                borrow_title = input("Enter the title of the book to borrow: ")
                book_to_borrow = next((book for book in self.books if borrow_title.lower() == book.title.lower()), None)
                if book_to_borrow:
                    member.borrow_book(book_to_borrow)
                else:
                    print("Book not found in the catalog.")

            elif choice == "6":
                return_title = input("Enter the title of the book to return: ")
                book_to_return = next((book for book in member.borrowed_books if return_title.lower() == book.title.lower()), None)
                if book_to_return:
                    member.return_book(book_to_return)
                else:
                    print("Book not found in the borrowed list.")

            elif choice == "7":
                self.display_members()

            elif choice == "8":
                self.display_borrowed_books(member_name)

            elif choice == "0":
                print("Exiting the Virtual Library. Goodbye!")
                break

            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    library = VirtualLibrary()
    library.simulate_library()
