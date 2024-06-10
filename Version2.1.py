class Book:
    def __init__(self, titles, authors):
        self.titles = titles
        self.authors = authors
        self.next_book = None
        self.prev_book = None

class BookInventory:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_book(self, titles, authors):
        new_book = Book(titles, authors)
        if not self.head:
            self.head = new_book
            self.tail = new_book
        else:
            new_book.prev_book = self.tail
            self.tail.next_book = new_book
            self.tail = new_book

    def get_book_by_index(self, index):
        current = self.head
        for i in range(1, index):
            if current is None:
                return None
            current = current.next_book
        return current

    def remove_book(self, index):
        current = self.get_book_by_index(index)
        if current:
            if current == self.head:
                self.head = current.next_book
                if self.head:
                    self.head.prev_book = None
            else:
                current.prev_book.next_book = current.next_book
                if current.next_book:
                    current.next_book.prev_book = current.prev_book
            print("Book has been removed.")
        else:
            print(f"Book at index {index} not found in the inventory.")
    
    def replace_book(self, index, new_titles, new_authors):
        current = self.get_book_by_index(index)
        if current:
            current.titles = new_titles
            current.authors = new_authors
            print("Book has been replaced.")
        else:
            print(f"Book at index {index} not found in the inventory.")

    def view_inventory(self):
        if not self.head:
            print("The book inventory has no book stored.")
            return
        current = self.head
        index = 1
        while current:
            print(f"Book {index}:")
            print(f"  Titles: {', '.join(current.titles)}")
            print(f"  Authors: {', '.join(current.authors)}")
            current = current.next_book
            index += 1

class AuthSystem:
    def __init__(self):
        self.users = {}

    def input_with_validation(self, prompt, validation_error):
        while True:
            user_input = input(prompt).strip()
            if not user_input:
                print(validation_error)
            else:
                return user_input

    def register(self):
        while True:
            username = self.input_with_validation("Set up a username: ", "Error: Username cannot be empty or just spaces.")
            if username in self.users:
                print("Username already exists. Please try another one.")
                continue
            break
        while True:
            password = self.input_with_validation("Set up a password (max 6 characters): ", "Error: Password cannot be empty or just spaces.")
            if len(password) > 6:
                print("Error: Password must be 6 characters or less.")
                continue
            break
        self.users[username] = password
        print("Registration successful!")

    def login(self):
        while True:
            username = self.input_with_validation("Enter your username: ", "Error: Username cannot be empty or just spaces.")
            if username not in self.users:
                print(f"No user named {username} found. Please try again.")
                continue
            break
        while True:
            password = self.input_with_validation("Enter your password: ", "Error: Password cannot be empty or just spaces.")
            if self.users.get(username) == password:
                print("Login successful!")
                return True
            else:
                print("Authentication failed. Please try again.")

def main():
    inventory = BookInventory()
    auth = AuthSystem()

    while True:
        print("\nWelcome to the Book Inventory Management System")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            auth.register()
        elif choice == '2':
            if auth.login():
                while True:
                    print("\nBook Inventory Menu:")
                    print("1. Add a book")
                    print("2. Remove a book")
                    print("3. Replace a book")
                    print("4. Logout")
                    choice = input("Enter your choice: ")

                    if choice == '1':
                        titles = input("Enter the titles of the book (separated by commas): ").split(', ')
                        titles = [title.strip() for title in titles if title.strip()]
                        if not titles:
                            print("Error: Titles cannot be empty or just spaces.")
                            continue
                        if len(titles) > 3:
                            print("Error: You can enter up to 3 titles only.")
                            continue
                        authors = input("Enter the authors of the book (separated by commas): ").split(', ')
                        authors = [author.strip() for author in authors if author.strip()]
                        if not authors:
                            print("Error: Authors cannot be empty or just spaces.")
                            continue
                        if len(authors) > 3:
                            print("Error: You can enter up to 3 authors only.")
                            continue
                        inventory.add_book(titles, authors)
                        print("Book added to the inventory.")

                    elif choice == '2':
                        try:
                            index = int(input('Enter the number of the book to remove: '))
                            inventory.remove_book(index)
                        except ValueError:
                            print("Invalid input. Please enter a valid book number.")

                    elif choice == '3':
                        try:
                            index = int(input('Enter the number of the book to replace: '))
                            current_book = inventory.get_book_by_index(index)
                            if not current_book:
                                print(f"Book at index {index} not found in the inventory.")
                                continue

                            new_titles = input("Enter the new titles of the book (separated by commas): ").split(', ')
                            new_titles = [title.strip() for title in new_titles if title.strip()]
                            if not new_titles:
                                print("Error: Titles cannot be empty or just spaces.")
                                continue
                            if len(new_titles) > 3:
                                print("Error: You can enter up to 3 titles only.")
                                continue

                            new_authors = input("Enter the new authors of the book (separated by commas): ").split(', ')
                            new_authors = [author.strip() for author in new_authors if author.strip()]
                            if not new_authors:
                                print("Error: Authors cannot be empty or just spaces.")
                                continue
                            if len(new_authors) > 3:
                                print("Error: You can enter up to 3 authors only.")
                                continue
                            
                            inventory.replace_book(index, new_titles, new_authors)
                        except ValueError:
                            print("Invalid input. Please enter a valid book number.")

                    elif choice == '4':
                        print("Logging out.")
                        break

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

main()
