# Library management system
# A-simple-Library-Management-system-using-Python
## Libraries used: Pandas and Datetime.
### This program uses a CSV file as the database to handle the list of books and their borrower/due date/availability details. The Terminal is used to operate the program and doesn't use a GUI. 

This is a simple library management system that an admin can operate to  
 -> view the list of books and their availability  
 -> lend books  
 -> return books    
 -> view the list of books borrowed by a certain student (while returning a book)  
 -> automatically calculate the FINE to be paid for late return of book beyond the due date.  
 
 -> errors such as lending a book which isn't available, trying to return a book which isn't borrowed by that student are also handled.  
 -> new books can be added to the database by directly editing the CSV file.
 
 ## Instructions to run the program:
 Put both the main_lms.py and Book_list.csv file in a single folder and run the python file using command "python main_lms.py".

 """
Library Management System

This Python script implements a comprehensive library management system that allows users to manage a library's book inventory, track borrowing, and handle returns.

Table of Contents:
1. Requirements
2. Installation
3. Usage
    3.1. Running the System
    3.2. Main Menu Options
4. Data Storage
5. Customization
6. Error Handling
7. Notes
8. Author Information

1. Requirements:
- Python 3.x
- pandas library (install using 'pip install pandas')

2. Installation:
- Ensure that Python is installed on your system.
- Install the pandas library by running 'pip install pandas' in your terminal.

3. Usage:

3.1. Running the System:
- Place the 'Book_list.csv' file in the same directory as this script. This CSV file stores book data.
- Run the script in your terminal:
    $ python library_management.py

3.2. Main Menu Options:
   - Enter one of the following menu options (1 to 5) to perform actions:
     1. Display all books in the library.
     2. Display available books.
     3. Borrow a book.
     4. Return a book.
     5. Quit the system.

   - Follow on-screen prompts for each option:
     - Enter the appropriate information when prompted, such as borrower IDs and book codes.
     - The system will provide feedback, update the book database, and calculate fines for late returns.

4. Data Storage:
- The system uses a CSV file ('Book_list.csv') to store and manage book data. The CSV file includes the following columns:
  - TITLE: Book titles.
  - Book Code: Unique book identifiers.
  - Status: Book availability (AVAILABLE or BORROWED).
  - Borrower ID: Borrower identification (empty for available books).
  - Due Date: Date by which borrowed books should be returned (empty for available books).

5. Customization:
- You can customize the following constants in the code to tailor the system to your needs:
  - FINE_PER_DAY: Defines the fine rate per day for late returns (default: 1).
  - BORROW_PERIOD: Specifies the default borrowing period in days (default: 15).

6. Error Handling:
- The system handles common errors, but user inputs should be valid to prevent unexpected behavior.
- Enhance error handling and validation as needed for your specific requirements.

7. Notes:
- Borrowers can borrow multiple books, but they must return them within the specified due date to avoid fines.
- The system enforces borrowing limits for each borrower.

8. Author Information:
- Author: Himanshu Kumar
- GitHub Repository: https://github.com/kalyugwasi/Library-management-system

For any questions or issues, please contact [opyaaz@gmail.com].

"""

 
 
 
