def creation_of_file():
    filename = input("Enter the file name: ")
    try:
        with open(filename, 'w'):
            print("File created successfully")

    except:
        print("Error creating file")





