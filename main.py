import pandas as pd
from datetime import datetime, timedelta

# Constants
FINE_PER_DAY = 1  # 1 rupee per day fine for late submission from the due date
BORROW_PERIOD = 15  # Due date will be 15 DAYS from the date of borrow

# File path for the book list CSV
CSV_FILE_PATH = r'C:\Users\himan\Documents\GitHub\Library-management-system\Book_list.csv'

def get_date(offset_days=0):
    now = datetime.now() + timedelta(days=offset_days)
    return now.strftime('%d-%m-%Y')

def calculate_fine(due_date, return_date):
    date_format = '%d-%m-%Y'
    d1 = datetime.strptime(due_date, date_format)
    d2 = datetime.strptime(return_date, date_format)
    diff = d2 - d1
    days_late = max(0, diff.days)
    return days_late * FINE_PER_DAY

def display_available_books():
    df = pd.read_csv(CSV_FILE_PATH)
    available_books = df[df['Status'] == 'AVAILABLE']['Book Code'].tolist()
    print('The available books are:')
    for book_code in available_books:
        print(book_code)

def borrow_book():
    borrower_id = input('Please input the ID: ')
    df = pd.read_csv(CSV_FILE_PATH)
    
    if borrower_id in df['Borrower ID'].tolist():
        borrowed_books = df[df['Borrower ID'] == borrower_id]
        print('The borrowed books are:')
        print(borrowed_books[['Book Code', 'Book Title', 'Due Date']])
    
    book_code = input('Enter the book code of the book to be borrowed: ')
    
    if book_code not in df['Book Code'].values:
        print('Please enter a valid book code.')
        return
    
    book_index = df[df['Book Code'] == book_code].index[0]
    
    if df.loc[book_index, 'Status'] == 'BORROWED':
        print('This book is already borrowed.')
    else:
        df.loc[book_index, 'Status'] = 'BORROWED'
        df.loc[book_index, 'Borrower ID'] = borrower_id
        due_date = get_date(BORROW_PERIOD)
        df.loc[book_index, 'Due Date'] = due_date
        print(df.loc[book_index])
        print("Book borrowed successfully. Due Date:", due_date)

    pd.read_csv(CSV_FILE_PATH).to_csv(CSV_FILE_PATH, index=False)

def return_book():
    borrower_id = input('Please input the ID: ')
    df = pd.read_csv(CSV_FILE_PATH)
    
    if borrower_id not in df['Borrower ID'].values:
        print('No books have been borrowed by this ID.')
        return
    
    borrowed_books = df[df['Borrower ID'] == borrower_id]
    print('The borrowed books are:')
    print(borrowed_books[['Book Code', 'Book Title', 'Due Date']])
    
    book_code = input('Enter the book code of the book to be returned: ')
    
    if book_code not in borrowed_books['Book Code'].values:
        print('Please enter a valid book code.')
        return
    
    book_index = borrowed_books[borrowed_books['Book Code'] == book_code].index[0]
    
    due_date = df.loc[book_index, 'Due Date']
    return_date = get_date()
    
    fine_amount = calculate_fine(due_date, return_date)
    
    df.loc[book_index, 'Status'] = 'AVAILABLE'
    df.loc[book_index, 'Borrower ID'] = ''
    df.loc[book_index, 'Due Date'] = ''
    
    print('Book returned successfully.')
    print('LATE SUBMISSION FINE: {} Rupees'.format(fine_amount))

# Main menu loop
while True:
    print('''
    ********************************************************************
                       LIBRARY MANAGEMENT SYSTEM
    Date: {}
    ********************************************************************
    
    Enter 1. To Display all the books
    Enter 2. To Display the available books
    Enter 3. To Borrow a book
    Enter 4. To Return a book
    Enter 5. To Quit
    '''.format(get_date()))
    
    option = input('Enter your choice: ')
    
    if option == '1':
        df = pd.read_csv(CSV_FILE_PATH)
        print('{:<40} {:<12} {:<10} {:<20} {:<10}'.format('TITLE', 'Book Code', 'Status', 'Borrower ID', 'DUE DATE'))
        for index, row in df.iterrows():
            print('{:<40} {:<12} {:<10} {:<20} {:<10}'.format(row['TITLE'], row['Book Code'], row['Status'], row['Borrower ID'], row['DUE DATE']))
    elif option == '2':
        display_available_books()
    elif option == '3':
        borrow_book()
    elif option == '4':
        return_book()
    elif option == '5':
        pd.read_csv(CSV_FILE_PATH).to_csv(CSV_FILE_PATH, index=False)
        exit()
    else:
        print('Please enter a valid option.')
    
    pd.read_csv(CSV_FILE_PATH).to_csv(CSV_FILE_PATH, index=False)
    input("Press ENTER to continue...")
