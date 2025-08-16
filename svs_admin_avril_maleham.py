# ============== Selwyn Vet Services MAIN PROGRAM ==============
# Student Name: Avril Maleham
# Student ID : 1167041
# NOTE: Make sure your two files are in the same folder
# =================================================================================

from svs_data import col_invoices,col_customers,col_treatments,col_services,db_customers,db_treatments,db_services,unique_id,display_formatted_row   # svs_data.py MUST be in the SAME FOLDER as this file!
                    # spb_data.py contains the data
import datetime     # We areusing date times for this assessment, and it is
                    # available in the column_output() fn, so do not delete this line
    
def list_customers(customer_id=None):
    """
    List the ID, name, telephone number, and email of all customers
    or a single customer if customer_id is provided.
    """
    
    # Convert the dictionary data into a list that displays the required data fields
    #initialise an empty list which will be used to pass data for display
    display_list = []
    
    # Determine which customers to display
    if customer_id is not None:
        customers_to_display = [customer_id]
    else:
        customers_to_display = db_customers.keys()
        # display a heading for the output
        print("\nCustomer List\n")
    
    #Iterate over all the customers 
    for cid in customers_to_display:
         #append to the display list the ID, Name, Telephone and Email
        display_list.append((cid,
                             db_customers[cid]['details'][0],
                             db_customers[cid]['details'][1],
                             db_customers[cid]['details'][2]))
    
    format_columns = "{: >4} | {: <20} | {: <15} | {: <12}"
  
    # Use col_Customers for display
    display_formatted_row(list(col_customers.keys()), format_columns)
    for row in display_list:
        # An example of how to call column_output function
        display_formatted_row(row, format_columns)
    
    # Pauses the code to allow the user to see the output
    input("\nPress Enter to continue.")


def list_items(data_dict, col_dict, title):
    """
    Helper function for list_treatments() and list_services().
    Display a formatted table of items from the given data dictionary in alphabetical order.

    Args:
        data_dict (dict): Dictionary containing items with ID as keys and [Name, Cost] as values.
        col_dict (dict): Dictionary defining the column names and types.
        title (str): Title to display above the table.
    """
    
    # Initialise an empty list to hold the data for display
    display_list = []

    # Iterate over all items in the dictionary
    for item_id in data_dict.keys():
        # Append the ID, Name, and Cost to the display list
        display_list.append((item_id,
                             data_dict[item_id][0],
                             data_dict[item_id][1]))

    # Sort by name (alphabetically) 
    display_list.sort(key=lambda x: x[1])  

    # Formatting for display
    format_columns = "{:<4} | {:<15} | {:<8}"
    
    # Heading
    print(f"\n{title}\n")
    # Column headings
    display_formatted_row(list(col_dict.keys()), format_columns)
    # Loop through display list and print each row
    for row in display_list:
        display_formatted_row(row, format_columns)

    input("\nPress Enter to continue.")


def list_treatments():
    """
    Show all available treatments with ID, name, and cost in a formatted table.
    Displays treatments in alphabetical order by name.
    """
    list_items(db_treatments, col_treatments, "Treatment List")


def list_services():
    """
    Show all available services with ID, name, and cost in a formatted table.
    Displays services in alphabetical order by name.
    """
    list_items(db_services, col_services, "Service List")


def add_customer():
    """
    Allow user to add multiple customers to the database with input validation.
    Loops continuously until user types 'back' to return to main menu.
    """
    
    print("\nAdd a new customer")
    print("(Type 'back' at any time to return to the main menu)")
    
    # Main loop - keeps adding customers until user types 'back'
    while True: 
        
        # Create empty list for this customer's details
        customer_details = []  

        # Validate customer first name: letters only
        # Assuming we are only using English alphabet for purpose of this assignment
        while True:
            first_name = input("\nPlease enter the customer first name: ").strip() # remove leading/ trailing whitespace
            if first_name.lower() == "back":
                return
            if first_name.isalpha():
                first_name = first_name.capitalize()
                break
            print("Error: Name must be letters only.")
            
        # Validate customer last name: letters only
        # Assuming we are only using English alphabet for purpose of this assignment
        # and no double barrelled last names
        while True:
            last_name = input("\nPlease enter the customer last name: ").strip()
            if last_name.lower() == "back":
                return
            if last_name.isalpha():
                last_name = last_name.capitalize()
                break
            print("Error: Name must be letters only.")
            
        # Create full name and add to customer_details list as one entry
        full_name = f"{first_name} {last_name}"
        customer_details.append(str(full_name))

        # Validate telephone number: digits only, between 7 and 15 digits
        while True:
            telephone = input("\nPlease enter the customer telephone number: ").strip()
            if telephone.lower() == "back":
                return
            if telephone.isdigit():
                if len(telephone) >= 7 and len(telephone) <= 15:  
                    customer_details.append(str(telephone))
                    break
                else:
                    print("Error: Telephone number must be between 7 and 15 digits.")
            else:
                print("Error: Telephone number must be numbers only.")

        # Validate email to ensure format is like 'avril@email.com'
        while True:
            email = input("\nPlease enter the customer email: ").strip()
            if email.lower() == "back":
                return
            
            # Check email as a whole
            if "@" not in email or email.count("@") != 1:
                print("Error: Email must contain exactly one '@' symbol.")
                continue
            
            # Check email as a whole
            if ".." in email:
                print("Error: Email cannot contain consecutive periods ('..').")
                continue
            
            # Check email in correct format
            local_part, domain_part = email.split("@")

            # Check local and domain parts
            if not local_part or not domain_part or " " in local_part or " " in domain_part:
                print("Error: Local and domain parts cannot be empty or contain spaces.")
                continue

            # Check domain part
            if "." not in domain_part:
                print("Error: Domain part must contain at least one '.'")
                continue

            # Check domain part
            if domain_part[0] == "." or domain_part[-1] == ".":
                print("Error: Domain cannot start or end with a '.'")
                continue
            
            # Check local part
            if local_part[0] == "." or local_part[-1] == ".":
                print("Error: Local part cannot start or end with a '.'")
                continue
            
            # Passed all checks
            customer_details.append(str(email))
            break

        # Generate new unique customer ID
        new_id = unique_id()

        # Add customer to db_customers dict
        new_customer = {new_id: {'details': customer_details, 'bookings': {}}}
        db_customers.update(new_customer)

        print("\nSuccess! Customer created.\n")
        list_customers(new_id)
        
        # Allow user to continue or exit
        continue_input = input("\nPress Enter to add another customer or type 'back' to return to main menu: ")
        if continue_input.strip().lower() == "back":
            return


def get_customer():
    """
    Helper function for add_booking() and pay_invoice() to retrieve a customer by ID.
    Prompts user to enter customer ID and validates it exists in the database.

    Returns:
        tuple[int, dict]: Customer ID and customer data dictionary if found.
        tuple[None, None]: None values if user types 'back' or customer not found.
    """
    
    list_customers()
    
    while True:
        # Assuming for the purpose of this assignment that customers are selected by ID, not name
        # Validate customer ID: numbers only
        user_input = input("Please enter the customer ID: ").strip()
        if user_input.lower() == "back":
            return None, None
        if not user_input.isdigit():
            print("Error: ID must be numbers only.")
            continue
        
        # Convert valid numeric input to integer
        customer_id = int(user_input)
        
        # Check if the customer ID exists in the database
        if customer_id in db_customers:
            customer = db_customers[customer_id]
            
            # Display confirmation to the user
            print(f"Customer found: {customer['details'][0]}")
            return customer_id, customer
        else:
            # If not found, ask again
            print("Error: No customer with that ID. Please try again.")


def get_booking_date(must_be_future=True):
    """
    Helper function for add_booking() and pay_invoice() to retrieve and validate a booking date.
    Ensures the date is valid, in the future, and properly formatted.

    Returns:
        datetime.date: Valid booking date entered by user.
        None: If user types 'back' or validation fails.
    """
     
    # Assuming as the import is the whole module in this file, you expect us to use it like this
    today = datetime.date.today()
    print("\nEnter booking date:")
    
    # Validate year: numbers only, in the 4 digit format
    while True:
        year_input = input("Year (YYYY): ").strip()
        if year_input.lower() == "back":
            return None
        if not year_input.isdigit():
            print("Error: Year must be numbers only.")
            continue
        if len(year_input) != 4:
            print("Error: Year must be exactly 4 digits (e.g., 2025).")
            continue
        year = int(year_input)
        break
    
    # Validate month: numbers between 1-12 only
    while True:
        month_input = input("Month (1-12): ").strip()
        if month_input.lower() == "back":
            return None
        if not month_input.isdigit():
            print("Error: Month must be numbers only.")
            continue
        month = int(month_input)
        if month < 1 or month > 12:
            print("Error: Month must be between 1 and 12.")
            continue
        break
    
    # Validate day: numbers between 1-31 only
    while True:
        day_input = input("Day (1-31): ").strip()
        if day_input.lower() == "back":
            return None
        if not day_input.isdigit():
            print("Error: Day must be numbers only.")
            continue
        day = int(day_input)
        if day < 1 or day > 31:
            print("Error: Day must be between 1 and 31.")
            continue
        break
    
    # Validate complete date, must be a valid date and must be in the future
    try:
        input_date = datetime.date(year, month, day)
    except ValueError:
        print("Error: Invalid date, please try again.")
        return get_booking_date()

    # Validate complete date, must be in the future if being used for add_booking()
    if must_be_future and input_date < today:
        print("Error: Date must be today or later.")
        return get_booking_date(must_be_future=must_be_future)

    return input_date
    
    
def get_items(data_dict, item_type):
    """
    Generic helper function for add_booking() to get services or treatments and their costs.
    Prompts user to enter item IDs one at a time until they type 'done'.

    Args:
        data_dict (dict): Dictionary containing items with ID as keys and [Name, Cost] as values.
        item_type (str): String describing the type of item being selected (e.g., "service" or "treatment").

    Returns:
        tuple: A tuple containing (selected_items, item_costs) where:
               - selected_items is a tuple of selected item IDs
               - item_costs is a list of corresponding costs
        None: If user types 'back' to cancel the operation
    """
    if item_type == "service":
        list_services()
    else:
        list_treatments()
    
    # Assuming for the purpose of this assignment that treatments/ services are selected by ID, not name
    print(f"\nEnter IDs of {item_type}s you would like to book one at a time.")
    print("Type 'done' when finished.")
    
    selected_items = []
    item_costs = []
    
    while True:
        # Validate item ID: numbers only
        item_id = input(f"\nPlease enter a {item_type} ID: ").strip()
        if item_id.lower() == 'back':
            return None 
        if item_id.lower() == 'done':
            break
        if not item_id.isdigit():
            print("Error: ID must be numbers only.")
            continue
        # Convert valid numeric input to integer
        item = int(item_id)
        # Check if the item ID exists in the database
        if item not in data_dict:
            print(f"Error: No {item_type} with that ID. Please try again.")
            continue
        
        selected_items.append(item)
        item_costs.append(data_dict[item][1])
        # Confirmation message
        print(f"{item_type.capitalize()} added to booking.")
    
    return tuple(selected_items), item_costs


def add_booking():
    """
    Add a new booking for an existing customer.
    Guides user through selecting customer, date, services, and treatments.
    Calculates total cost and saves booking to customer record.
    """
    
    print("\nAdd a new booking for an existing customer")
    print("(Type 'back' at any time to return to the main menu)")
    
    # Loop until a valid booking is made
    while True: 

        # Step 1 - Get the customer by ID
        customer_id, customer = get_customer()
        if customer_id is None:
            print("Booking cancelled.")
            return

        # Step 2 - Get the booking date
        booking_date = get_booking_date(must_be_future=True)
        if booking_date is None:
            print("Booking cancelled.")
            return
        
        #Inner loop to ensure at least one service or treatment added to booking
        while True: 
            # Step 3 - Get selected services and their costs
            services_result = get_items(db_services, "service")
            if services_result is None:
                print("Booking cancelled.")
                return
            selected_services, service_costs = services_result
            
            # Step 4 - Get selected treatments and their costs
            treatments_result = get_items(db_treatments, "treatment")
            if treatments_result is None:
                print("Booking cancelled.")
                return
            selected_treatments, treatment_costs = treatments_result
            
            # Step 5 - Check that at least one service or treatment was selected
            if not selected_services and not selected_treatments:
                print("\nError: You must select at least one service or treatment.")
                print("Please try again.\n")
                continue  # Restart the while loop to try again
        
            break 
        
        # Step 6 - Calculate total cost of booking (to two decimal places)
        total_cost = round(sum(service_costs) + sum(treatment_costs), 2)

        # Step 7 - Save the booking to the customer's record
        customer['bookings'][booking_date] = [selected_services, selected_treatments, total_cost, False]

        # Step 8 - Show success message 
        print(f"\nSuccess! Booking for {customer['details'][0]} ({customer_id}) created on {booking_date}")
        if selected_services:
            service_names = [db_services[s_id][0] for s_id in selected_services]
            print(f"Services booked: {', '.join(service_names)}")
        if selected_treatments:
            treatment_names = [db_treatments[t_id][0] for t_id in selected_treatments]
            print(f"Treatments booked: {', '.join(treatment_names)}")
        print(f"Total cost: ${total_cost}")
    
        # Pauses the code to allow the user to see the output
        input("\nPress Enter to continue.")     
        break


def invoices_to_pay(customer_id = None):
    """
    Display unpaid invoices with customer details in a formatted table.
    Sorted by booking date. Can show all unpaid invoices or just those for a specific customer.
    Used as a function in its own right and also as a helper to pay_invoice().

    Args:
        customer_id (int, optional): Specific customer ID to show unpaid invoices for.
                                   If None, shows unpaid invoices for all customers.

    Returns:
        bool: True if there are unpaid invoices to display, False if none found.
    """
    
    display_list = []
    
    # Store the original customer_id parameter to check later
    specific_customer = customer_id
    
    # Determine which customers to process
    if customer_id is not None:
        # Process only the specified customer
        customers_to_process = [customer_id]
    else:
        # Process all customers
        customers_to_process = db_customers.keys()
    
    # Retrieve each customer
    for customer_id in customers_to_process:
        customer_details = db_customers[customer_id]['details']
        customer_name = customer_details[0]
        customer_phone = customer_details[1]
        
        # Check each booking for this customer
        bookings = db_customers[customer_id]['bookings']
        for booking_date, booking_data in bookings.items():
            amount = booking_data[2]
            paid_status = booking_data[3]
            
            # If booking is unpaid, add to display list
            if paid_status == False:
                display_list.append((customer_name, customer_phone, booking_date, amount))
                
    # Sort by date 
    display_list.sort(key=lambda x: x[2])
    
    # Only display if there are unpaid invoices
    if display_list:
        # Format columns 
        format_columns = "{: <18} | {: <12} | {: <12} | {: >8}"
        
        print("\nOutstanding Invoices:\n")
        
        # Display header using col_invoices keys
        display_formatted_row(list(col_invoices.keys()), format_columns)
        
        # Display each unpaid invoice
        for row in display_list:
            display_formatted_row(row, format_columns)
            
        input("\nPress Enter to continue.")
        return True 
    else:
        if specific_customer is not None:
            print("\nNo unpaid invoices for this customer.")
            
        else:
            print("\nNo unpaid invoices found.")
    
        input("\nPress Enter to continue.")   
        return False


def pay_invoice():
    """
    Process payment for an unpaid invoice.
    Allows user to select a customer, view their unpaid invoices,
    and mark a specific invoice as paid.
    """
    
    print("\nPay an invoice for selected customer")
    print("(Type 'back' at any time to return to the main menu)")

    # Step 1 - Get the customer by ID
    customer_id, customer = get_customer()
    if customer_id is None:
        print("Payment cancelled.")
        return
    
    # Step 2 - Use invoices_to_pay to display unpaid invoices in table format
    has_unpaid_invoices = invoices_to_pay(customer_id)
    
    # Step 3 - Ask for date of invoice to be paid if there are unpaid invoices
    if not has_unpaid_invoices:
        return
    
    print("\nSelect the date of the invoice you wish to pay or type 'back' to return to main menu")
    booking_date = get_booking_date(must_be_future=False)
    if booking_date is None:
        print("Payment cancelled.")
        return
    
    # Step 4 - Update the invoice to paid
    if booking_date not in customer['bookings']:
        print(f"\nError: No invoice found for date {booking_date}")
        input("\nPress Enter to continue.") 
        return
    
    # Step 5 - Customer feedback success message
    customer['bookings'][booking_date][3] = True
    print(f"Success! Invoice for {booking_date} has been marked as paid.")
    input("\nPress Enter to continue.") 
    

# function to display the menu
def disp_menu():
    print("==== WELCOME TO SELWYN VET SERVICES ===")
    print(" 1 - List Customers")
    print(" 2 - List Services")
    print(" 3 - List Treatments")
    print(" 4 - Add Customer")
    print(" 5 - Add Booking")
    print(" 6 - Display Unpaid Invoices")
    print(" 7 - Pay Invoice")
    print(" X - eXit (stops the program)")


# ------------ This is the main program ------------------------

# Display menu for the first time, and ask for response
disp_menu()
response = input("Please enter menu choice: ")

# Don't change the menu numbering or function names in this menu
# Repeat this loop until the user enters an "X"
# x can be upper or lower case and leading/trailing whitespace removed
while response.strip().upper() != "X":
    if response == "1":
        list_customers()
    elif response == "2":
        list_services()
    elif response == "3":
        list_treatments()
    elif response == "4":
        add_customer()
    elif response == "5":
        add_booking()
    elif response == "6":
        invoices_to_pay()
    elif response == "7":
        pay_invoice()
    else:
        print("\n***Invalid response, please try again (enter 1-7 or X)")

    print("")
    disp_menu()
    response = input("Please select menu choice: ")

print("\n=== Thank you for using Selywn Vet Services! ===\n")
