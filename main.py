from library_books import library_books
from datetime import datetime, timedelta

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
def view_available_books():

    info_to_print = ['id', 'title', 'author']

    def is_available(book):
        return book['available'] == True

    for book in library_books:
        if is_available(book):
            for info in info_to_print:
                if info in book:
                    print(f'{info}: {book[info]}')
            print('-------------------------')


# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

def search():
    user_search = str(input('Search books by author OR genre: ')).lower()

    matching_books = []
    for book in library_books:
        if book['author'].lower() == user_search or book['genre'].lower() == user_search:
            matching_books.append(book)
    
    if matching_books:
        print('------------------')
        for book in matching_books:
             print(f'Title: {book['title']}')
             print(f'Author: {book['author']}')
             print(f'Genre: {book['genre']}')
             print(f'Available?: {book['available']} ')
             print('--------------')
    else:
        print('Unable to find book. Please try again.')




# -------- Level 3 --------()
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Mark it unavailable
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Print a message saying it's already checked out

def checkout():
    user_ID = input('Please enter book ID to checkout: ').lower()
    book_found = False

    for book in library_books:
        if book['id'].lower() == user_ID:
            book_found = True
            if book['available'] == True:
                print(f'{book['title']} written by {book['author']}')
                correct = input('is this the book you would like? (y/n): ').lower()
                if correct == 'y': 
                     book['available'] = False
                     book['checkouts'] += 1
                     now = datetime.today()
                     two_weeks = timedelta(weeks=2)
                     book['due_date'] = now + two_weeks
                     print('---BOOK CHECKED OUT---')
                     print(f'you have checked out: {book['title']}')
                     print(f'Amount of checkouts: {book['checkouts']}')
                     print(f'please return by: {book['due_date']}')
                     break
                else:
                    print('ok, we hope you come back later!')
                    break
            elif book['available'] == False:
                print(f'sorry {book['title']} has already been checked out')
                break
    if not book_found:
        print('no book was found')


            

# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date
def return_book():
    book_id = input('please enter the ID of the book you would like to return: ').lower()
    book_found = False
    for book in library_books:
        if book['id'].lower() == book_id:
            book_found = True
            print(f'{book['title']} written by {book['author']}')
            correct = input('is this the book? (y/n): ').lower()

            if correct == 'y':
                book['available'] = True
                book['due_date'] = None
                print('book has been returned')
                print(book['available'])
                print(book['due_date'])
    
    if not book_found:
        print('no book found')

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out
def view_overdue():
    info_to_print = ['id', 'title', 'author', 'due_date']
    today = datetime.today()
    overdue =[]

    
    for book in library_books:
        if book['due_date'] is None:
                    continue
        
        due = datetime.strptime(book['due_date'],"%Y-%m-%d")
        
        if due < today and book['available'] == False:
            overdue.append(book)
    
    
    if overdue:
            print('---Overdue books---')
            for book in overdue:
                for info in info_to_print:
                    if info in book:
                        print(f'{info}: {book[info]}')
                print('-------------------------')
    
    else:
            print('no overdue books')
view_overdue()

#Add a new book

def add():
    while True:
        book_id = input('enter book id: ')
        if any(book['id'] == book_id for book in library_books):
            print("id already exists. Enter a different id")
        else:
            break

    title = input("enter title: ")
    author = input("enter author: ")
    genre = input("enter genre: ")

    new_book = {
        'id': book_id,
        'title': title,
        'author': author,
        'genre': genre,
        'available': True,
        'due_date': None,
        'checkouts': 0
    }

    library_books.append(new_book)
    print(f'{title} had been added')

def main_menu():
    print('welcome to the libary')
    print('select an option')
    print('1. view the available books')
    print('2. view the overdue books')
    print('3. add a new book')
    print('4. search for a book')
    print('5. checkout a book')
    print('6. return a book')
    print('7. exit')

    option = int(input('\nplease enter the number for your option: '))
    if option == 1:
        view_available_books()
    elif option == 2:
        view_overdue()
    elif option == 3:
        add()
    elif option == 4:
        search()
    elif option == 5:
        checkout()
    elif option == 6:
        return_book()
    elif option == 7:
        print(' \nthank you and goodbye')
    else:
        print('invalid option. try again')
    main_menu()



if __name__ == "__main__":
    main_menu()
    pass
