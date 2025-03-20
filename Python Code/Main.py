# imports the modules needed for this program
import os
import datetime
try:
    # This block of code tries to import the Room, Customer, and
    # RoomAllocation classes from the Room_Module, Customer_Module, and RoomAllocation_Module modules
    from Room_Module import Room
    from Customer_Module import Customer
    from RoomAllocation_Module import RoomAllocation
# The except block catches this exception and prints an error message to the user.
except ModuleNotFoundError as ex:
    print(ex)
    print("Please check your modules")

# A list to store the rooms that are available for allocation.
listOfRooms = []
# The number of rooms that are available for allocation.
noOfRooms = 0
# List of allocated rooms
listOfRoomAllocations = []
# The path to the file where the room allocation data is stored.
filepath = ""
# The path to a backup of the room allocation file.
filePathBackUp = ""


def main():
    global noOfRooms, filepath, filePathBackUp
    # The path to the user's Documents folder.
    folder_path = os.path.expanduser("~/Documents")
    # This code joins the path to the user's Documents folder with the filename lhms_Matthew.text to the
    # room allocation file.
    filepath = os.path.join(folder_path, "lhms_764705436.text")
    # Code is the same but creates a backup of the room allocation file with the same filename.
    filePathBackUp = os.path.join(folder_path, "lhms_764705436_backup.text")
    menu()

def menu():
    """Displays a menu to the user and allows them to select an option."""
    try:
        choice = -1
        # while loop for menu
        while choice != 0:
            # Display menu options
            print("************************************************************************************")
            print("                  LANGHAM HOTEL MANAGEMENT SYSTEM                  ")
            print("************************************************************************************")
            print("0. Exit")
            print("1. Add Rooms")
            print("2. Delete Rooms")
            print("3. Display Rooms Details")
            print("4. Allocate Rooms")
            print("5. Display Room Allocation Details")
            print("6. Billing & De-Allocation")
            print("7. Save The Room Allocation to a File")
            print("8. Show the Room Allocation from a File")
            print("9. Backup")
            print("************************************************************************************")
            # Asking user to pick a number for choice a from menu
            choice = int(input(" Enter Your Choice of Number Here (0-9): "))
            if choice == 0:
                # To exit from application
                exit(0)
            elif choice == 1:
                # Add rooms
                add_room()
            elif choice == 2:
                # Delete rooms
                delete_room()
            elif choice == 3:
                # Display rooms details
                display_room_details()
            elif choice == 4:
                # Allocate rooms
                allocate_rooms()
            elif choice == 5:
                # Display room allocation details
                display_room_allocations_details()
            elif choice == 6:
                # Billings and De-Allocation of rooms
                Billing_and_De_Allocation()
            elif choice == 7:
                # Save room allocations to file
                save_room_allocations()
            elif choice == 8:
                # Show room allocation from file
                show_room_allocations()
            elif choice == 9:
                # Backup file
                backup()
            else:
                # If user enters invalid input
                print("Please enter a valid number 0-9")
    except SystemError as e:
        print(f"Syntax Error : {e}")
    except ValueError as e:
        print(f"Value Error :{e}")

def add_room():
    # Global variables
    global noOfRooms, listOfRooms
    # Try to convert the user's input to an integer. If the input is not an integer,
    # display an error message and prompt the user to try again.
    try:
        print("You have selected 'ADD ROOMS' from menu")
        noOfRooms = int(input("Please enter the total number of rooms in the Hotel: "))
        # Print the number of rooms that the user entered.
        print(f"Hotel has {noOfRooms} rooms in total")
        print("************************************************************************************")
        # Check if there are any existing rooms in the list. If there are, get the index of the last room.
        if len(listOfRooms) > 0:
            y = len(listOfRooms)
        else:
            y = 0
        # Add new rooms to the list.
        for x in range(noOfRooms):
            room = Room()
            listOfRooms.append(room)
        # Get the details of each room.
        for i in range(y, y + noOfRooms):
            obj_room = listOfRooms[i]
            print(f"Room Allocation {i + 1}:")
            obj_room.RoomNo = int(input(f"Please enter room number {i + 1} :"))
            obj_room.IsAllocated = False
            listOfRooms[i] = obj_room
            # Check if the room number that the user entered is already present in the list. If it is,
            # display an error message and prompt the user to enter a new room number.
            if i > 0:
                for j in range(i):
                    while listOfRooms[i].RoomNo == listOfRooms[j].RoomNo:
                        print(f"Same room number already exist")
                        obj_room.RoomNo = int(input(f"Please enter a new room number {i + 1}:"))
                        obj_room.IsAllocated = False
                        listOfRooms[i] = obj_room
    except ValueError as e:
        # If the user enters an invalid input, display an error message and prompt the user to try again.
        print(f"Value error : {e} ")
        print("Invalid input, Please try again ")
        add_room()

def delete_room():
    # Deletes a room from the list of rooms.
    global listOfRooms
    if listOfRooms:
        # If there are rooms in the list, prompt the user to enter the room number that they want to delete.
        print("You have selected the option to 'DELETE ROOM' from menu")
        print("************************************************************************************")
        room_number = int(input("Please enter the room number that you want to delete"))

        # Try to find the room in the list. If the room is found, remove it from the list.
        try:
            for obj_room in listOfRooms:
                if obj_room.RoomNo == room_number:
                    listOfRooms.remove(obj_room)
                    print(f"Room with Room Number : {room_number} has been deleted successfully")
                    break
        except ValueError as e:
            # If the room is not found, display an error message and prompt the user to try again.
            print(f"Value error : {e} ")
            print("Invalid input, Please try again ")
            delete_room()
    else:
        # If there are no rooms in the list, display a message informing the user that there are no rooms to delete.
        print("No rooms to delete\nPlease aff rooms first")

def display_room_details():
    # Displays the details of all rooms.
    global listOfRooms
    if listOfRooms:
        print("You have selected the option to 'DISPLAY ROOMS' from menu")
        print("************************************************************************************")
        print(f"Following rooms have been added")
        for obj_room in listOfRooms:
            # For each room in the list, display the room number.
            print(f"Room Number : {obj_room.RoomNo}")
    else:
        # If there are no rooms in the list, display a message informing the user that there are no rooms to delete.
        print("No rooms to delete\nPlease aff rooms first")

def allocate_rooms():
    # Allocates rooms to customers
    # Global variables
    global noOfRooms, listOfRooms, listOfRoomAllocations
    try:
        # Prompt the user to enter the number of rooms that they want to allocate.
        print("You have selected the option to 'ALLOCATE ROOMS' from menu")
        allocate_room = int(input("How many rooms would you like to allocate: "))
        # Validate the user's input. Ensure that the user cannot allocate more rooms
        # than the total number of rooms in the hotel.
        while allocate_room > len(listOfRooms):
            print(f"You cannot allocate more rooms than the total number of rooms in the Hotel\n"
                  f"Please enter a number between 1--{len(listOfRooms)}: ")
            allocate_room = int(input("How manu rooms would you like to allocate?: "))
        print(f"You are allocating {allocate_room} room(s)")
        # Iterate over the number of rooms that the user wants to allocate.
        i = 0
        while i < allocate_room:
            # Create a new `RoomAllocation` object.
            roomAllocation = RoomAllocation()
            # Create a new `Customer` object.
            customer = Customer()
            # Prompt the user to enter the room number that they want to allocate.
            print("************************************************************************************")
            searchRoom = int(input("Please search Room Number to allocate: "))
            # Search for the room in the list of rooms.
            for j in range(len(listOfRooms)):
                if searchRoom == listOfRooms[j].RoomNo:
                    # If the room is found, check if it is already allocated.
                    if not listOfRooms[j].IsAllocated:
                        # If the room is not allocated, allocate the room to the customer.
                        print(f"Room {listOfRooms[j].RoomNo} is empty ")
                        customer.CustomerNo = int(input("Please enter Customer Number to allocate: "))
                        customer.CustomerName = input("Please enter Customer Name to allocate")
                        listOfRooms[j].IsAllocated = True
                        print("Allocation has been done")
                        # Update the `RoomAllocation` object with the allocated room number and customer.
                        roomAllocation.AllocatedRoomNo = searchRoom
                        roomAllocation.AllocatedCustomer = customer
                        # Append the `RoomAllocation` object to the list of room allocations.
                        listOfRoomAllocations.append(roomAllocation)
                        # Increment the counter.
                        i += 1
                        # Break the loop.
                        break
                    else:
                        # If the room is already allocated, display an error message
                        print(f"Room {listOfRooms[j].RoomNo} is already occupied\n"
                              f'Please enter another room to allocate')
                        i -= 1
                        break
                else:
                    # If the room is not found in the list of rooms, display an error message
                    while j == len(listOfRooms) - 1:
                        print(f"Could not find matching room number to allocate\n" +
                              f"Please enter correct room number or add room first")
                        i -= 1
                        break
    except ValueError:
        # If the user enters an invalid input, display an error message and prompt the user to try again.
        print("Invalid input. Please try again. ")
        allocate_rooms()

def display_room_allocations_details():
    global listOfRoomAllocations
    # Check if there are any rooms to display.
    if listOfRoomAllocations:
        print("You have selected 'DISPLAY ROOMS ALLOCATION DETAILS' from menu.")
        print("************************************************************************************")
        print("Following rooms have been allocated:")

        # Iterate over the list of all allocated rooms and print the
        # following information for each room:
        for obj_room in listOfRoomAllocations:
            print(f"Allocated Room Number: {obj_room.AllocatedRoomNo}")
            print(f"Customer Number: {obj_room.AllocatedCustomer.CustomerNo}")
            print(f"Customer Name: {obj_room.AllocatedCustomer.CustomerName}")
    else:
        print("No allocated rooms to display\nPlease allocate rooms first")

def Billing_and_De_Allocation():
    global listOfRoomAllocations

    try:
        print("You have selected the option 'Billing and De-Allocation' from menu")
        print("************************************************************************************")
        Room_no = int(input("Please enter the customers room number here:  "))

        for obj_roomAllocated in listOfRoomAllocations:
            if obj_roomAllocated.AllocatedRoomNo == Room_no:
                Days = int(input("Enter how many days has customer stayed in hotel:  "))
                Fee = 100
                Billing_Fee = Days * Fee
                print(f"Customer detail {Room_no}:  ")
                print(f"Days stayed: {Days}")
                print(f"Daily fee: {Fee}")
                print(f"Total room fee due: {Billing_Fee}")
                listOfRoomAllocations.remove(obj_roomAllocated)
                print(f"Room has been De-Allocated for customer {Room_no}")
                break
            else:
                print(f"Allocated room has no matching room number {Room_no}")
    except SystemError as ex:
        print(ex)
        print("Please try again")
        Billing_and_De_Allocation()
    except IOError as ex:
        print(ex)
        print("Please try again")
        Billing_and_De_Allocation()
    except TypeError as ex:
        print(ex)
        print("Please try again")
        Billing_and_De_Allocation()

def save_room_allocations():
    # Saves the room allocations to a file.
    # Global variables
    global filepath
    try:
        # Inform the user that they have selected the option to save the room allocations to a file.
        print("You have selected 'SAVE THE ROOM ALLOCATIONS TO A FILE' from menu.")
        print("************************************************************************************")
        # Open the data file for writing.
        with open(filepath, "w") as file:
            # Get the current date and time.
            now = str(datetime.datetime.now())
            # Iterate over the list of room allocations and write each one to the file.
            for obj_roomAllocated in listOfRoomAllocations:
                add_to_file = f"********************************************************************\n" \
                              f"Room Number: {obj_roomAllocated.AllocatedRoomNo}\n" \
                              f"Customer Number: {obj_roomAllocated.AllocatedCustomer.CustomerNo}\n" \
                              f"Customer Name: {obj_roomAllocated.AllocatedCustomer.CustomerName}\n" \
                              f"Current date and time is {now}"
                # Write the room allocation to the file.
                file.write(add_to_file + "\n")
        # Inform the user that the room allocations have been saved successfully.
        print("FIle saved as 'lhms_764705436.text' under Documents folder")

    except FileNotFoundError as ex:
        # If the data file does not exist, display an error message and prompt the user to try again.
        print(ex)
        print("Please try again")
    except IOError as ex:
        print(ex)
        print("Please try again")
    except Exception as ex:
        print(ex)
        print("Please try again")


def show_room_allocations():
    # Displays the room allocations to the console.
    # Global variables
    global filepath
    try:
        # Inform the user that they have selected the option to show the room allocations to a file.
        print("You have selected 'SHOW THE ROOM ALLOCATIONS FROM THE FILE' from menu.")
        print("************************************************************************************")
        # Open the data file for reading.
        with open(filepath, "r") as file:
            # Read the first line of the file.
            lines = file.readline()
            # Iterate over the lines in the file and print them to the console.
            for obj_roomAllocated in listOfRoomAllocations:
                print(f"Room Number: {obj_roomAllocated.AllocatedRoomNo}")
                print(f"Customer Number: {obj_roomAllocated.AllocatedCustomer.CustomerNo}")
                print(f"Customer Name: {obj_roomAllocated.AllocatedCustomer.CustomerName}")


    except FileNotFoundError as ex:
        # If the data file does not exist, display an error message and prompt the user to try again.
        print(ex)
        print("Please try again")

    except IOError as ex:
        print(ex)
        print("Please try again")

    except EOFError as ex:
        print(ex)
        print("Please try again")

def backup():
    # Backs up the room allocation data to a file.
    global filepath, filePathBackUp
    try:
        print("You have selected the option 'BACK UP' from menu")
        print("************************************************************************************")
        while os.path.exists(filePathBackUp):
            # If the backup file exists, prompt the user to delete it.
            print("'lhms_backup.txt' file already exist \nExisting file will be deleted")
            os.remove(filePathBackUp)


        # Rename the original file to the backup file.
        os.rename(filepath, filePathBackUp)
        # Print a success message.
        print("Your file 'lhms.txt' is saved as 'lhms_backup.txt'\n" + "Original file will be deleted")
    except FileNotFoundError as ex:
        print(ex)
        print("Error try again")


if __name__ == '__main__':
    main()
