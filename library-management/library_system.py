#---Library Management System---#
#---CLI Based application to manage library books and members---#
#---Contains: Functions, Loops, Conditionals and JSON for File Storage---#

import json # Import of  JSON library for file handling
import os # Import of OS library for file handling

#-----Constant: File path for all the saved book data
DATA_FILE = "books.json"

#-----User list and credentials for Login 
#-----Username --> Password 
USERS = {
    "admin": "library123",
    "staff": "books456"
}

#=========================================
#------REQUIREMENT 1: USER LOGIN SYSTEM
#------Authenticate users to login with password and username
#------A maximum of 3 login attempts are allowed 
#------While loop counts the login attempts 
#------Nested if/elife statements check for valid username and password

def login():
    """
    Handles user login with a maximum of 3 attempts.
    Returns True if login is successful, False otherwise.
    """
    print("-" * 45)
    print("   WELCOME TO THE LIBRARY MANAGEMENT SYSTEM")
    print("-" * 45)

    attempts = 0   # Counter to track how many attempts the user has made
    max_attempts = 3  # Maximum allowed login attempts

    while attempts < max_attempts: # Loop until user runs out of attempts
        attempts += 1  # Increment the attempts counter
        max_attempts = 3 # Maximum limit for login attempt
        
        print(f"\nLogin Attempt {attempts} of {max_attempts}") # Display the current attempt number to the user
        username = input("Enter username: ").strip() #.strip() for removing unintentional spaces while input
        password = input("Enter password: ").strip()

         # Check if the username exists in our USERS dictionary
        if username in USERS:
            if USERS[username] == password: # Nested conditional: check if password also matches
                print(f"\n Login successful! Welcome, {username}.")
                return True  # Exit function after login in successful 
            else:
                print("! Incorrect password. Please try again.")   # Username correct but password wrong
        else:
            print(" ! Username not found. Please try again.")  # Username not found in system
        
        # Show remaining attempts if remains
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f" You have {remaining} attempts left.")
        else:
            print(" Maximum login attempts reached.")
    # If All 3 attempts used without success, return False
    print("\n ! Too many failed attempts. Access denied.")
    print("  Please contact the administrator.")
    return False  # Login failed

#=========================================
#------REQUIREMENT 4: DATA STORAGE - LOAD & SAVE Functions 
#------Use of JSON File to read/write book data
#------Provides simple data storage solution for the application
#------Uses try/except blocks to handle file errors gracefully without crashing 

def load_books():
    """
    Loads books and the last used book ID from the JSON data file.
    If the file does not exist, returns empty list and last_id = 0.
    Returns:
        books (list): list of book dictionaries
        last_id (int): last issued book ID
    """
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as file:
                data = json.load(file)

            # Expecting NEW JSON structure:
            # {
            #   "last_id": <int>,
            #   "books": [ {...}, {...} ]
            # }
            books = data.get("books", [])
            last_id = data.get("last_id", 0)

            return books, last_id

        except Exception as e:
            print(f"Warning: Could not read data file. Starting fresh. ({e})")
            return [], 0
    else:
        return [], 0

def save_books(books, last_id):
    """
    Saves the current list of books and the last used book ID
    into the JSON data file.
    Parameters:
        books (list): list of book dictionaries
        last_id (int): last issued book ID
    """
    try:
        with open(DATA_FILE, "w") as file:
            json.dump(  #export contents into .JSON file
                {
                    "last_id": last_id,
                    "books": books
                },
                file,
                indent=4)
        print(" Data saved successfully.")
    except Exception as e:
        print(f" Error saving data: {e}")

#=========================================
#------REQUIREMENT 3a: ADD BOOK
#------Allows  user to add a new book
#------Takes user input for title, author, genre, year, copies
#------Uses try/except blocks to validate numeric input
#------Saves and updates list to file 

def add_book(books, last_id):
    """
    Asks user for book details and adds a new book to the list.
    IDs are strictly increasing and never reused.
    Parameters:
        books (list): current list of book dictionaries
        last_id (int): last issued book ID
    Returns:
        last_id (int): updated last issued book ID
    """
    print("\n" + "-" * 40)
    print("         ADD A NEW BOOK")
    print("-" * 40)

    # Collect book details from the user
    title = input("Enter the book title:  ").strip()
    author = input("Enter book author name: ").strip()
    genre = input("Enter book genre:       ").strip()

    # Validate the year is a number
    while True:
        try:
            year = int(input("Enter publication year: ").strip())
            break
        except ValueError:
            print(" Invalid year. Please enter a number (for example: 2020).")

    # Validate that copies is a positive number
    while True:
        try:
            copies = int(input("Enter number of copies: ").strip())
            if copies < 1:
                print(" Number of copies must be at least 1.")
            else:
                break
        except ValueError:
            print(" Invalid input. Please enter a whole number.")

    # Always increment last_id (never reuse IDs)
    last_id += 1

    # Create new book dictionary
    new_book = {
        "id": last_id,
        "title": title,
        "author": author,
        "genre": genre,
        "year": year,
        "copies": copies
    }

    # Add and save
    books.append(new_book)
    save_books(books, last_id)

    print(f"\n '{title}' by {author} has been added to the library.")

    #  return updated last_id
    return last_id

#=========================================
#------REQUIREMENT 3b: REMOVE BOOK
#------ Allows the user to delete a book using its ID
#------Uses a for loop to search through all books
#------Uses try/except blocks to validate numeric input
#------Uses if/else to confirm deletion

def remove_book(books, last_id):
    """
    Removes a book from the library using its ID number.
    Parameters: books - the current list of book dictionaries
    """
    print("\n" + "-" * 40)
    print("           REMOVE A BOOK")
    print("-" * 40)

    # List to show the books so the user knows which book ID to enter
    view_books(books)

    # Check if there are any books to remove
    if len(books) == 0:
        return  # Nothing to remove - go back to menu

    # Ask user which book to remove
    while True:
        try:
            book_id = int(input("\nEnter the Book ID to remove (Enter - 0 to cancel): ").strip()) #.strip() for removing unintentional spaces while input
            break
        except ValueError:
            print("! Please enter a valid number.")

    # If user enteres 0, cancel operation
    if book_id == 0:
        print("  Removal cancelled.")
        return

    # Search for book with the matching ID using a for loop
    book_found = None
    for book in books:
        if book["id"] == book_id:
            book_found = book
            break  # Stop searching once found

    # Check if a book was found
    if book_found is not None:
        # Confirm before deleting
        title = book_found.get("title", "Unknown Title")
        confirm = input(f"  Are you sure you want to remove '{title}'? (yes/no): ").strip().lower() #strip() for removing unintentional spaces while input and lower() if user case sensitive input
        if confirm == "yes":
            books.remove(book_found)   # Remove the book from the list
            save_books(books, last_id)           # Save updated list to file
            print(f"! '{book_found['title']}' has been removed from the books list.")
        else:
            print("  Removal cancelled.")
    else:
        # No book matched the entered book ID
        print(f"! No book found with ID {book_id}.")

#=========================================
#------REQUIREMENT 3c: UPDATE BOOK
#------Allows the user to modify an existing book's details
#------Uses a for loop to find the book using book  ID
#------Leaves fields unchanged if user presses Enter (blank)

def update_book(books, last_id):
    """
    Updates the details of an existing book in books list.
    Leaves a field unchanged if user leaves blank information.
    Parameters: books - the current list of book dictionaries
    """
    print("\n" + "-" * 40)
    print("           UPDATE A BOOK")
    print("-" * 40)

    # Show already existing books first
    view_books(books)

    if len(books) == 0:
        return  # Return if nothing to update

    # Ask user which book to update
    while True:
        try:
            book_id = int(input("\nEnter the Book ID to update (0 to cancel): ").strip())
            break
        except ValueError:
            print("! Please enter a valid number.")

    if book_id == 0: # if users cancels update
        print("  Update cancelled.")
        return

    # Find the book by boook ID
    book_found = None
    for book in books:
        if book["id"] == book_id:
            book_found = book
            break # exit loop

    if book_found is not None:
        title = book_found.get("title", "Unknown Title")
        print(f"\n  Editing: '{title}' (press Enter to keep current value)") # Press enter if user wants to keep current book title 

        # For each field, show current value and allow update
        # If user just presses Enter (blank input), keep the old value

        new_title = input(f"  Title [{book_found['title']}]: ").strip()
        if new_title != "":
            book_found["title"] = new_title

        new_author = input(f"  Author [{book_found['author']}]: ").strip()
        if new_author != "":
            book_found["author"] = new_author

        new_genre = input(f"  Genre [{book_found['genre']}]: ").strip()
        if new_genre != "":
            book_found["genre"] = new_genre

        # Validates the  year input if user provides one
        new_year = input(f"  Year [{book_found['year']}]: ").strip()
        if new_year != "":
            while True:
                try:
                    book_found["year"] = int(new_year)
                    break
                except ValueError:
                    new_year = input("  ! Invalid year. Enter again: ").strip()

        # Validate copies input if user provides one
        new_copies = input(f"  Copies [{book_found['copies']}]: ").strip()
        if new_copies != "": 
            while True: #loop to keep asking the user for valid input
                try:
                    copies_val = int(new_copies)
                    if copies_val < 1:
                        new_copies = input("  ! Number of copy must be at least 1. Enter again: ").strip() 
                    else: #save valid input and exit loop
                        book_found["copies"] = copies_val
                        break
                except ValueError:
                    new_copies = input("  ! Invalid input. Enter a number: ").strip()

        # Save the updated book list to file
        save_books(books, last_id)
        print(f"\n Book ID {book_id} has been updated successfully.") #confirmation for successful operation
    else:
        print(f" ! No book found with ID {book_id}.")

#=========================================
#------REQUIREMENT 5: SEARCH and View Books 
#------Display books in a readable format
#------Users can search by title and author keyword
#------Uses loops to iterate over all the books 
#------Uses 'in' membership operator for keyword matching

def view_books(books):
    """
    Responsible for displaying all books currently in the library in a formatted table.
    Parameters: books - the current list of book dictionaries
    """
    print("\n" + "-" * 75)
    print(f"{'ID':<5} {'Title':<25} {'Author':<20} {'Genre':<12} {'Year':<6} {'Copies'}") #alignment spaces  for table header
    print("-" * 75)

    # Check if the library has the books
    if len(books) == 0:
        print("  No books found in the library.")
    else:
        # Loop through every book and print its details
        for book in books:
            # f-string formatting keeps columns aligned by using spaces
            print(f"{book.get('id',''):<5} "
                  f"{book.get('title',''):<25} "
                  f"{book.get('author',''):<20} "
                  f"{book.get('genre',''):<12} "
                  f"{book.get('year',''):<6} "
                  f"{book.get('copies','')}")

            
    print("-" * 75)
    print(f"  Total books in library: {len(books)}")

def search_books(books):
    """
    Searches  for books by a keyword by title or author name.
    Uses  'in' membership operator for case-insensitive matching.
    Parameters: books - the current list of book dictionaries
    """
    print("\n" + "-" * 40)
    print("           SEARCH FOR A BOOK")
    print("-" * 40)

    # Receive the search keyword from the user
    keyword = input("Enter title or author to search: ").strip().lower()

    if keyword == "":
        print(" Please enter a search term.")
        return

    # Search through all books using a for loop
    results = []   # Empty list to store matching books
    for book in books:
        # Uses 'in' membership operator to check if the keyword appears
        # in title OR author [case-insensitive using .lower()]
        if keyword in book.get("title", "").lower() or keyword in book.get("author", "").lower(): #
            results.append(book)  # Add match to results list

    # Display results or a not-found message
    if len(results) > 0:
        print(f"\n  Found {len(results)} result(s) for '{keyword}':")
        view_books(results)
    else:
        print(f"\n! No books found matching '{keyword}'.")

#=========================================
#------REQUIREMENT 2: Interactive MENU SYSTEM
#------Display clear numbered menu options for the users
#------Users while loop to keep the menu running 
#------Uses if/elif/else statements to handle choice of user menu 
#------Each option calls for a dedicated function which results in a modular design 

def display_menu():
    """
    Displays the main menu options to the user.
    This is a separate function to keep the menu clean and reusable.
    """
    print("\n" + "=" * 45)
    print("          LIBRARY MANAGEMENT SYSTEM MENU")
    print("=" * 45)
    print("  1. View All Books")
    print("  2. Add a New Book")
    print("  3. Remove a Book")
    print("  4. Update a Book")
    print("  5. Search for a Book")
    print("  6. Exit")
    print("=" * 45)


def main_menu():
    """
    This is the  main menu loop. Keeps running until user chooses to Exit.
    Each menu choice calls the coresponding function appropiatly to handle the user's request.
    """
    # Load existing book data from file when program starts
    books, last_id = load_books()
    print(f"\n  Library loaded. {len(books)} book(s) found in the system.")

    # Keeping the  menu running in a loop until user chooses to exit
    while True:
        display_menu()  # Show menu options

        choice = input("  Enter your choice (1-6): ").strip()

        # Handle each menu choice using if/elif/else
        if choice == "1":
            # View all books
            view_books(books)

        elif choice == "2":
            # Add a new book
            last_id = add_book(books, last_id)

        elif choice == "3":
            # Remove an existing book
            remove_book(books, last_id)

        elif choice == "4":
            # Update/edit an existing book
            update_book(books, last_id)

        elif choice == "5":
            # Search for a book by keyword
            search_books(books)

        elif choice == "6":
            # Exit the program
            print("\n  Thank you for using the Library Management System.")
            print("  Goodbye!\n")
            break  # Exit the while loop and end the program

        else:
            # Invalid option entered if user enters something other than 1-6
            print("! Invalid choice. Please enter a number between 1 and 6.")

#=========================================
#------REQUIREMENT 2: Interactive MENU SYSTEM
#------First runs the login function to authenticate the user before showinging the menu
#------Only open the menu if login is successful, otherwise login fail message is shown and program ends
if __name__ == "__main__":
    # Step 1: Attempt login (Requirement 1)
    login_success = login()

    # Step 2: Only open the menu when login is successful
    if login_success:
        main_menu()   # Requirement 2: Interactive menu
    # If login failed the program ends here automatically