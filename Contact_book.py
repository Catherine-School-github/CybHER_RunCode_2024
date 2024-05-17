choice = 1
while (choice != 0):
    #menu to let user chose what they want
    print("\n\n\tMenu:")
    print("Press 1 to view all the contacts")
    print("Press 2 to view a specific person")
    print("Press 3 to add a contact")
    print("Press 4 to remove a contact")
    print("Press 5 to delete all contacts")
    print("Press 0 to quit")    
    choice = int(input("Your decision: "))

    while (choice < 0 or choice > 5):
        print("\n\n\tInvalid choice")
        print("Press 1 to view all the contacts")
        print("Press 2 to view a specific person")
        print("Press 3 to add a contact")
        print("Press 4 to remove a contact")
        print("Press 5 to delete all the contacts")
        print("Press 0 to quit")
        choice = int(input("Your decision: "))

    #if user viewed all contacts
    if (choice == 1):
        csv_file = open("contacts.csv", 'r')
        print("\n\n\tViewing All Contacts")
        for information in csv_file:
            print(information)
        csv_file.close()

    #if user wanted to view a specific person
    elif (choice == 2):
        csv_file = open ("contacts.csv", 'r')
        person_found = False
        print("\n\n\tLooking For A Specific Contact")
        full_name = input("What is the name of the person you want to look up: ")
    
        for line in csv_file:
            row = line.strip().split(',')
            if row[0] == full_name:
                person_found = True
                print("\n\n\tPerson Found:")
                for information in row:
                    print(information.strip())
    
        if (person_found == False):
            print("That person is not in the contact book")

        csv_file.close()

    #if user wanted to add a new contact
    elif (choice == 3):
        print("\n\n\tAdding A New Contact")
        csv_file = open ("contacts.csv", 'a', newline = '\n')
        name = input("What is the name of the person you want to add: ")
        email_address = input("What is the email address of the person you want to add: ")
        phone_number = input("What is the phone number of the person you want to add: ")
        notes = input("What are notes you want to add to this person (press enter to leave blank): ")
        csv_file.write(name + ', ' + email_address + ', ' + phone_number + ', ' + notes + "\n")
        csv_file.close()
    

    #if the user wanted to delete a contact
    elif(choice == 4):
        print("\n\n\tRemoving A Contact")
        name = input("What is the name of the person you want to delete: ")

        csv_file = open("contacts.csv", 'r')
        lines = csv_file.readlines()
        csv_file.close()
        csv_file = open("contacts.csv", 'w')

        for information in lines:
            row = information.strip().split(',')
            if (row[0] == name):
                print("Name found, deleting the contact")
            else:
                csv_file.write(information)

        csv_file.close()

    #if the user wanted to delete everyone
    elif (choice == 5):
        print("\n\n\tDeleting All Contacts")
        csv_file = open("contacts.csv", 'w')
        csv_file.close()

    else:
        print("Exiting the program")
