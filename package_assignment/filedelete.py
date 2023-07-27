import os

def deleting_of_file():
    filename = input("Enter the file name: ")
    try:
        os.remove(filename)

        print("File deleted successfully")


    except:

        print("Error deleting file")

