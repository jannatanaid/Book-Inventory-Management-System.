import pickle
class Book:
    def __init__(self, titles, authors):
        self.titles = titles  
        self.authors = authors  
        self.next_book = None
        self.prev_book = None
        
class Data:
    def __init__(self, inventory,auth):
        self.dataHead = inventory.head
        self.dataTail = inventory.tail
        self.dataUser = auth.users
    def save(self, directory):
        with open(directory, 'wb') as  f:
            pickle.dump(self.dataHead, f)
    def saveT(self, directory):
        with open(directory, 'wb') as  f:
            pickle.dump(self.dataTail, f)
    def saveauth(self, directory):
        with open(directory, 'wb') as  f:
            pickle.dump(self.dataUser, f)
    def load(self, directory):
        with open(directory, 'rb') as f:
            loaded  = pickle.load(f)
        return loaded
    def loadT(self, directory):
        with open(directory, 'rb') as f:
            loaded  = pickle.load(f)
        return loaded
    def loadauth(self, directory):
        with open(directory, 'rb') as f:
            loaded  = pickle.load(f)
        return loaded
        
        
class BookInventory:
    def __init__(self):
        super().__init__()
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
            print("The book inventory is empty. Please add a book first before removing.")
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
        super().__init__()
        self.users = {}

    def register(self):
        while True:
            username = input("Set up a username: ").strip()
            if not username:
                print("Username must not be blank. Please enter a valid username.")
                continue
            if username in self.users:
                print("Username already exists. Please try another one.")
                continue
            break
        while True:
            password = input("Set up a password (max 6 characters): ").strip()
            if not password:
                print("Password must not be blank. Please enter a valid password.")
                continue
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
                print(f"No {username} found. Please register first.")
                return False
            break
        while True:
            password = input("Enter your password: ")
            if self.users.get(username) == password:
                print("Login successful!")
                return True
            else:
                print("Authentication failed. Please try again.")
                continue

def main():
    inventory = BookInventory()
    auth = AuthSystem()
    while True:
            try:
                print("\nWelcome to the Book Inventory Management System")
                print("\n1. Register")
                print("2. Login")
                print("3. Admin")
                print("4. Exit")
                choice = input("\nEnter your choice: ")
                if choice == '1':
                    auth.register()
                elif choice == '2':
                    if auth.login():
                        while True:
                            print("\nBook Inventory Menu:")
                            print("1. Add a book")
                            print("2. Remove a book")
                            print("3. Replace a book")
                            print("4. View book inventory")
                            print("5. Logout")
                            choice = input("\nEnter your choice: ")
        
                            if choice == '1':
                                while True:
                                    titles = input("Enter the titles of the book (separated by commas): ").strip().split(', ')
                                    if any(not title.strip() for title in titles) or len(titles) > 3:
                                        print("Error: You must enter up to 3 valid titles.")
                                        continue
                                    authors = input("Enter the authors of the book (separated by commas): ").strip().split(', ')
                                    if any(not author.strip() for author in authors) or len(authors) > 3:
                                        print("Error: You must enter up to 3 valid authors.")
                                        continue
                                    inventory.add_book(titles, authors)
                                    print("Book added to the inventory.")
                                    break
        
                            elif choice == '2':
                                if not inventory.head:
                                    print("The book inventory is empty. Please add a book first before removing.")
                                else:
                                    while True:
                                        try:
                                            index = input('Enter the number of the book to remove: ').strip()
                                            if not index.isdigit():
                                                print("Invalid input. Please enter a valid book number.")
                                                continue
                                            index = int(index)
                                            inventory.remove_book(index)
                                            break
                                        except ValueError:
                                            print("Invalid input. Please try again.")
        
                            elif choice == '3':
                                while True:
                                    try:
                                        if not inventory.head:
                                            print("Please add a book first before replacing.")
                                            break
                                        index = int(input('Enter the number of the book to replace: '))
                                        new_titles = input("Enter the new titles of the book (separated by commas): ").strip().split(', ')
                                        if any(not title.strip() for title in new_titles) or len(new_titles) > 3:
                                            print("Error: You must enter up to 3 valid titles.")
                                            continue
                                        new_authors = input("Enter the new authors of the book (separated by commas): ").strip().split(', ')
                                        if any(not author.strip() for author in new_authors) or len(new_authors) > 3:
                                            print("Error: You must enter up to 3 valid authors.")
                                            continue
                                        inventory.replace_book(index, new_titles, new_authors)
                                        break
                                    except ValueError:
                                        print("Invalid input. Please try again.")
                            elif choice == '4':
                                inventory.view_inventory()
        
                            elif choice == '5':
                                print("Logging out.")
                                break
        
                            else:
                                print("Invalid choice. Please try again.")
                    else:
                        print("Login failed. Please try again.")
                elif choice == '4':
                    print("Exiting the program. Goodbye!")
                    break
                elif choice == '3':
                    mastercode="1234"
                    code = input("enter the master code to have admin access: ")
                    if code == mastercode:
                        print("Please input if you want to save or load an account: ")
                        choice = input(" 1. save \n 2. load\n Enter your choice: ")
                        if choice == '1':
                            data = Data(inventory, auth)
                            data.save("data.pkl")
                            data.saveT("dataT.pkl")
                            data.saveauth("dataauth.pkl")
                            print("data saved")
                        elif choice == '2':
                            data =  Data(inventory, auth)
                            loadedH = data.load("data.pkl")
                            loadedT = data.loadT("dataT.pkl")
                            loadedauth = data.loadauth("dataauth.pkl")
                            inventory.head = loadedH
                            inventory.tail = loadedT
                            auth.users = loadedauth
                    else:
                         print("youve entered the wrong code")
                    
                else:
                    print("Invalid choice. Please try again.")
            except ValueError:
                    print("wrong input")           
main()
