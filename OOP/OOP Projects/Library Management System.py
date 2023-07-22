# Library management system

class Library:
    def __init__(self, books):
        self.books_name = books
        self.lendDic = dict()

    def available_books(self):
        print("This books are available in our Library")
        for i, book in enumerate(self.books_name):
            print(f"{i}. {book}")

    def add_book(self, book):
        self.books_name.append(book)
        print("Added book")

    def lend_book(self, user, book):
        if book not in self.lendDic.keys():
            self.lendDic.update({book: user})
            print("You can take this book")
        else:
            print(f"Sorry, this book is already taken by {self.lendDic[book]}")

    def return_book(self, book):
        self.lendDic.pop(book)
        print("Book are updated")


if __name__ == '__main__':
    print("*********Welcome to the Library*********")
    print("press 'a' to see the available books")
    print("press 'b' to add book")
    print("press 'l' to lend book")
    print("press 'r' to return book")
    print("press 'e' to exit")

    obj = Library(["Python", "Java", "C++", "JavaScript", "Django", "React"])

    while True:
        user_input = input("Enter your input: ")
        if user_input == 'a':
            obj.available_books()
        if user_input == 'b':
            obj.add_book(input("Enter your book name: "))
        if user_input == 'l':
            user_name = input("Enter your name: ")
            book_name = input("Enter your book name: ")
            obj.lend_book(user_name, book_name)
        if user_input == 'r':
            obj.return_book(input("Enter your book name: "))
        if user_input == 'e':
            exit()