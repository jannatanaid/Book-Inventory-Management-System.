class Book:
    def __init__(self, titles, authors):
        self.titles = titles  # List of titles
        self.authors = authors  # List of authors
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
        if not self.head:
            print("Inventory is empty. No book to remove.")
            return
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

class AuthSystem:
    def __init__(self):
        self.users = {}
            
    def register(self):
        while True:
            username = input("Set up a username: ")
            if username in self.users:
                print("Username already exists. Please try another one.")
                continue
            break

        while True:
            password = input("Set up a password (max 6 characters): ")
            if len(password) > 6:
                print("Error: Password must be 6 characters or less.")
                continue
            break
            
        self.users[username] = password
        print("Registration successful!")
        return

    def login(self):
        if not self.users:
            print("No users registered. Please register first.")
            return False
        while True:
            username = input("Enter your username: ")
            if username not in self.users:
                print(f"No user '{username}' found.")
                choice = input("Would you like to register? (yes/no): ")
                if choice.lower() == 'yes':
                    self.register()
                else:
                    return False
            else:
                break
                
        while True:
            password = input("Enter your password: ")
            if self.users.get(username) == password:
                print("Login successful!")
                return True
            else:
                print("Wrong Password. Please try again.")
                continue

def main():
    inventory = BookInventory()
    auth = AuthSystem()

    while True:
        print("\nWelcome to the Book Inventory Management System")
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")  
        choice = input("\nEnter your choice: ")
        if choice == '1':
            auth.register()
        elif choice == '2':
            if auth.login():
                while True:
                    print("\nBook Inventory Menu:")
                    print("1. Add a book")
                    print("2. Remove a book")
                    print("3. Logout")
                    print("4. Exit")  
                    
                    choice = input("\nEnter your choice: ")
                    if choice == '1':
                        titles = input("Enter the titles of the book (separated by commas): ").split(', ')
                        if len(titles) > 3:
                            print("Error: You can enter up to 3 titles only.")
                            continue
                        authors = input("Enter the authors of the book (separated by commas): ").split(', ')
                        if len(authors) > 3:
                            print("Error: You can enter up to 3 authors only.")

                        inventory.add_book(titles, authors)
                        print("Book added to the inventory.")

                    elif choice == '2':
                        if inventory.head:
                            index = int(input('Enter the number of the book to remove: '))
                            inventory.remove_book(index)
                        else:
                            print("Inventory is empty. No book to remove.")

                    elif choice == '3':
                        print("Logging out.")
                        break
                    elif choice == '4':
                        print("Exiting the program.")
                        return  

                    else:
                        print("Invalid choice. Please try again.")
            else:
                print("Login failed. Please try again.")
        elif choice == '3':
            print("Exiting the program.")
            return  
        else:
            print("Invalid choice. Please try again.")

main()
