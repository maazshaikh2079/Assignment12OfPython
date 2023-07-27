# Info:-
# Name   : Maaz 
# Dept   : CO-B
# Batch  : 4
# Sub    : Python Assignment-12
# Topic  :-
# 1) Create a user-defined package to implement respective functions
# 2) The package should have at least 5 modules.
# 3) It should be a menu driven program
# 4) It should be a proper project, such as a management system or a login page
# (if it is a login page then it should navigate to that particular site)
# Note: you need to implement file handling and exception handling in this assignment
# (if you want you can use in-built modules such as tkinter or webbrowser or math
# it's optional)
# Date   : 27-07-2023

# Program:-
import package_assignment.filecreation as fc
import package_assignment.fileread as fr
import package_assignment.filewrite as fw
import package_assignment.fileappend as fa
import package_assignment.filedelete as fd


def menu():
    print("-------| MENU |-------")
    print("[1] Create a new file")
    print("[2] Read a file ")
    print("[3] Write to a file ")
    print("[4] Append to a file")
    print("[5] Delete a file ")
    print("[6] Exit ")
    try:
        choice = int(input("\nEnter your choice {1-6} : "))
        print();
        return choice
    except:
        print("Error: Invalid Input! Try Again.\n");
        menu();

while True:
    choice = menu()

    match choice:
        case 1:
            fc.creation_of_file()
        case 2:
            fr.reading_of_file()
        case 3:
            fw.writing_of_file()
        case 4:
            fa.appending_of_file()
        case 5:
            fd.deleting_of_file()
        case 6:
            print("Thank You Have A Nice Day!\n")
            print("exiting...\n");
            break
        case _:
            print("Invalid choice. Please try again.")

    print("\n")


# Output:-
# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 1

# Enter the file name: File_By_Maaz
# File created successfully


# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 3

# Enter the file name: File_By_Maaz
# Enter the content to write: Hello World! This Is Maaz.
# Content written successfully


# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 2

# Enter the file name: File_By_Maaz
# File content:
# Hello World! This Is Maaz.


# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 4

# Enter the file name: File_By_Maaz
# Enter the content to append:  From Somewhere On The Earth.
# Content appended successfully


# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 2

# Enter the file name: File_By_Maaz
# File content:
# Hello World! This Is Maaz.
#  From Somewhere On The Earth.


# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 5

# Enter the file name: File_By_Maaz
# File deleted successfully


# -------| MENU |-------
# [1] Create a new file
# [2] Read a file
# [3] Write to a file
# [4] Append to a file
# [5] Delete a file
# [6] Exit

# Enter your choice {1-6} : 6

# Thank You Have A Nice Day!

# exiting...