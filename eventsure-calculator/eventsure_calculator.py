"""EventSureNZ -Ticket Fee Calculator"""

#-----Function 1: get_customer_input()-----#
#-----Purpose: Collecting and validating all customer booing information-----#

def get_customer_input():
    """Collects all the customer bookig details and validates the input data
    This function gathers all the information from the user and validates each input to 
    ensure data integrity. Repetition (while loops) are used to keep asking for input until valid data is provided.
    Selection (if-else) to check validity conditions .

    Returns:
        tuple: (ordered unchangeable collection of items used to storef mutiple elements in a single variable)
        Contains(customer_name, event_type, num_tickets, ticket_price, customer_age)
        -customer_name (str): The full name of the customer.
        -event_type (str): The type of event the customer is booking for.(Concert, Sports or Conference
        -num_tickets (int): Number of tickets the customers want to purchase.
        -ticket_price (float): Price of per ticket in NZD.
        -customer_age (int): Age of the customer in years (0-120)

    Programming constructs:
        Repetition: while loops for validating input.
        Selection: if-else statements to validate each valid conditions.
        Error handling: try-except blocks to catch and handle exceptions during input.
    """

    # Section Header display design.
    print("" + "*"*50)
    print("Enter Customer Booking Details")
    print("*"*50)

    # Get Customer name. No validation needed as any text is acceptable for name.
    customer_name = input("Enter Customer Name: ")

    # Get Event type with validation to ensure business requirement
    # Repetition: Loop will continue until valid event type is entered.
    valid_event = False     #flag to control valid_event loop.
    while not valid_event:
        event_type = input("Enter Event Type (Concert, Sports, Conference): ") #This makes validation case-insensitive as user can enter in any case for example: concert or CONCERT. 

        # Standarding input to validate case-insensitive
        event_type = event_type.capitalize()

        if event_type == "Concert" or event_type == "Sports" or event_type == "Conference": #Used for validating if user enters one upper case and rest lower case for event type.
            valid_event = True #Exit loop if valid event type is entered.
        else:
            #Error message for clear message to guide user to enter valid event type.
            print(" Invalid Input ! Please enter the following three: Concert, Sports or Conference")
    # Get number of tickets with valid number of tickets.
    # Requirement: User must enter a positive integer for number of tickets as customer atleast have to buy one ticket to attend the event.
    # Repetition : Loop will continue until valid number of tickets are entered. 
    valid_ticket = False #Flag to control valid_ticket loop.
    while not valid_ticket: 
        try:   
            #Used for error handling if user enters text for number of tickets. Preventing program crash. 
            num_tickets = int(input("Enter Number of Tickets: "))
            if num_tickets> 0: #validation for user not to enter zero or negative number for number of tickets as it is not possible to book zero or negative tickets.
                valid_ticket = True
            else:
                print("Ticket number must be greater than 0!") #Error message if user enters zero or negative number for number of tickets.
        except: 
            print(" Invalid Input ! Please enter valid ticket number") #Showing error message if user enters text for number of ticket.
    
    # Get ticket price and validate.
    # Rquirement : Must be a positive number as ticket price cannot be negative or zero.
    valid_price= False #Flag to control valid_price loop.
    while not valid_price:
        try:    #Used for error handling if user enters text for ticket price furthermore preventing program crash. 
            ticket_price = float(input("Enter Ticket Price (NZD): ")) #Allows user to enter decimal values for ticket price such as 69.69$.
            
            #Selction to validate if user enters positive number for ticket price.Negative price or free tickers is not valid. 
            if ticket_price >0:
                valid_price = True #Exit loop if valid ticket price is entered.
            else: #Error message if user enters zero or negative number for ticket price.
                print(" Invalid Input ! Please enter a valid number for ticket price")
        except:
            print(" Invalid Input ! Please enter valid number for ticket price") #Error message if user enters text for ticket price.

    # Get customer age and validate.
    # Requirement: Age must be between 0 to 120 years as it is not possible for a person to be negative age or more than 120 years old to attend an event.
    # Repetition : Loop will continue until valid age is entered.
    valid_age = False #Flag to control valid_age loop.
    while not valid_age:
        try:
            #Used for error handling if user enters text for customer age. Preventing program crash.
            customer_age = int(input("Enter Customer Age: "))
            #Selection to validate if user enters age between 0 and 120 years.
            if customer_age >=0 and customer_age <=120: #AND operator used to check if age is within valid range (0 - 120).
                valid_age = True #Exit loop if valid age is entered.
            else: 
                print(" Please enter valid age between 0 to 120 years") #Error message if user enters age outside valid range (0-120).    
        except:
            print(" Invalid Input ! Please enter valid number for customer age") #Error message if user enters text for customer age.
    
    # Returning all the collected and validated customer booking details as a tuple.
    return (customer_name, event_type, num_tickets, ticket_price, customer_age) #Returning a tuple to store multiple elements in a single variable for other funcitions to use. 

#-----Function 2: calculate_total_fee()-----#
#-----Purpose: Calculate total ticket fee based on booking details and set rules-----#
#Recieve the required parameters to calculate total fee as per business rules such as the number of tickers, ticket price and customer age.
def calculate_fees(num_tickets, ticket_price, customer_age):
    """
    Calculates total protection fees based on the number of tickets, ticket price and customer age using specified rules.

    This function implements business logic for fee caluclation based on the following rules:
    Uses selection(if-else statements) to apply conditional surcharges based on ticket value and customer age. 

    Parameters:
        num_tickets(int): The number of tickets the customer will purchase.
        ticket_price(float): The price of ticket in NZD each.
        customer_age(int): The age of the customer in years.

        Returns:
            tuple: Contains (total_ticket_value, base_fee protection_fee, high_value_surcharge, age_surcharge, total_fee)
            ALL values are in floats to provide decimal number(for example: 69.99$) and  represent amounts in NZD

        Rules applied:
            1.Base fee is always : 25$ NZD.
            2. Protection fee: Always 5% of the toal ticket value
            3. High value surcharge: 40$ NZD if total ticket value exceeds 1000$ NZD.
            4. Age surcharge: 20$ NZD if customer age is above 65 years.
        
        Programming constructs:
            -operators: Used for calculating. 
            -selection: if-else statements to apply conditional surcharges. 
        """
    #Step 1 : Calculating total ticket value by multiplying number of tickets with ticket price.
    total_ticket_value = num_tickets * ticket_price

    #Step 2 : Applying base service fee. 25$ NZD is a fixed fee that always applies regardless of ticket value or customer age.
    base_fee = 25.00 #Constant value is given for clarity and easy modification in base fee changes in future.

    #Step 3 : Calculating protection fee
    # 5% of total ticket value.( 5/100 = 0.05)
    protection_fee = total_ticket_value * 0.05

    #Step 4 : Finding out  high value surcharge 
    # Selection : Check if total exceeds 1000$ NZD. If yes, apply surcharge of 40$ NZD.
    # Rule : High value surcharge is applied only if total ticket value exceeds 1000$ NZD.
    if total_ticket_value>1000:
        #apply surcharge if booking is high value.
        high_value_surcharge = 50.00
    else: 
        #apply no surcharge if booking is not high value.
        high_value_surcharge = 0.00

    #Step 5 : Finding out age surcharge
    # Selection : Check if customer age is above 65 years. If yes, apply surcharge of 20$ NZD.
    if customer_age > 65:
        #apply surcharge if customer is above 65 years.
        age_surcharge = 40.00
    else:
        #apply no surcharge if customer is below 65 years. 
        age_surcharge = 0.00

    #Step 6 : Calculate total protection fee. 
    #Sum all the calculated fees to get total fee.(base fee + protection fee + high value surcharge + age surcharge)
    # Usig addition operator to combile all fees.
    total_fee = base_fee + protection_fee + high_value_surcharge + age_surcharge 

    #Returning all the calculated fees as a tuple for other functions to use.
    return total_ticket_value, base_fee, protection_fee, high_value_surcharge, age_surcharge, total_fee

#-----Function 3 : display_results()-----#
#-----Purpose: Display calculated fee breakdown in clear, formatted output-----#
def display_results(customer_name, event_type, num_tickets, ticket_price, total_ticket_value, base_fee, protection_fee,high_value_surcharge, age_surcharge, total_fee):

    """Displays descreptive fee breakdown with clear formatting.

    This function preents all the booking and fee information to the user in organized manner maintaing easy to read format. It uses selection to display surcharges (if applicable).

    Parameters: 
        customer_name (str): The full name of the customer.
        event_type (str): The type of event (Concert, Sports or Conference).
        num_tickets (int): The number of tickets.
        ticket_price (float): The price of each ticket in NZD.
        total_ticket_value (float): The total value of the tickets in NZD.
        base_fee (float): The base fee in NZD.
        protection_fee (float): The protection fee in NZD.
        high_value_surcharge (float): The high value surcharge in NZD (if applicable).
        age_surcharge (float): The age surcharge in NZD (if applicable).
        total_fee (float): The total fee in NZD.

    Returns:
        None: This function does not return any value and directly prints the output to the console.

    Programming constructs:
        -OUTPUT : Used to display results .
        -String formatting : Used to str() and round() functions to format the output for better readability.
        -Selection : If statements to show only applicable surcharges in the output. 
        """
    
    #Display header design 
    print("" + "*"*50)
    print("Booking Summary and Fee Breakdown")
    print("*"*50)

    #Display booking details and confirming details with the customer.
    print("Customer Name: ", customer_name)
    print("Event Type: ", event_type)

    #Format ticket information clearly 
    #Using str() to convert numbers to string value and round() to round the total ticket value to 2 decimal places for better readability.
    print("Tickets:", num_tickets, "x $", str(round(ticket_price, 2)))

    #Display total ticket value 
    #Base amount before protection fees.
    print("Total Ticket Value: $" + str(round(total_ticket_value, 2)))

    #Display itemized fee breakdown for clarity.
    print("-"*50)
    print("Fee Breakdown")
    print("-"*50)

    #Always show base fee and protection fee 
    # Apply to all bookings 
    print("1. Base Service Fee: $" + str(round(base_fee, 2)))
    print("2. Protection Fee (5%) $" + str(round(protection_fee, 2)))

    #Selection: Conditional display high value surcharge if applicable.
    if high_value_surcharge > 0:
        print("3. High Value Surcharge: $" + str(round(high_value_surcharge, 2)))
        print(" (Applied: Total value exceeds 1000$")

    #Selection: Conditional display age surcharge if applicable.
    if age_surcharge > 0:
        print("4. Age Surcharge: $" + str(round(age_surcharge, 2)))
        print(" (Applied: Customer age is above 65 years)")
    
    #Display total fee to be paid by the customer.
    print("-"*50)
    print("Total Protection Fee : $" + str(round(total_fee, 2)))
    print("*"*50)

#-----Function 4: ask_continue()-----#
#-----Purpose: Ask user if they want to calculate fee for another customer-----#
def ask_continue():
    """ Asks the user if they want to perform another calculation for a different customer.

    This function uses REPETITION(while loop) and SELECTION(if-elif-else statements) to validate user input and return appropriate boolean value.

    Returns:
        bool: True if user wants to continue, False otherwise exit loop.

    Programming constructs:
        - Repetition: while loop to keep asking until valid input is received.
        -Selection: if-elif-else statements to validate user choice.
        -String methods: lower() for case insensitive comparison. 
    """

    # Repetition: Loop will continue until user enters valid input (yes or no).
    valid_choice = False #Flag to control valid_choice loop.
    while not valid_choice:
        #Get user input and validate if they want to continue or not.
        choice = input("Calculate fee for another customer? (yes/no): ")

        #convert to lowercase for case-insensitive comparison. 
        choice = choice.lower()  
        # This allows "Yes", "YES", "yes" to be treated as true.
       
        #Selection: check what the user entered
        # Using 'or' operator to accept mutiple variations of yes and no.
        if choice == 'yes' or choice == 'y':
            return True #User wants to continue with only entering 'y'.
        elif choice == 'no' or choice == 'n':
            return False #User wants to exit with only entering 'n'.
        else:
            #Invalid input message to guide user to enter valid inputs.
            print(" Invalid Input ! Please enter 'yes' or 'no'")
    # Note: This function will always return within if-else-else block until valid selection between yes or no is selected. 

#-----Function 5: main()-----#
#-----Main Prgram controller which coordinated with all other functions-----#
def main():
    """
    Main program function that calls all other functions in the correct sequence. It uses REPETITION (while loop) to allow processing multiple customers in one single session. 

    Program Flow: 
        1. Display welcome message 
        2. Loop: for each customer 
            a. Get customer input (calls get_customer_input)
            b. Calculate fees ( calls calculate_fees)
            c. Display results (calls display_results)
            d. Ask to continue (calls ask_continue)
        3. Display goodbye message 
    
    Returns: 
        No return on this function. User will choose to exit the loop or not.

    Programming Constructs: 
        -COMPOSITION: calls all other functions. 
        -REPETITION : While loop for procesing multiple customers. 
        -FUNCTIONS : Main coordinator function 
    """

    #Display Welcome Message Design for professional introduction
    print("*"*50)
    print("EVENTSURENZ - TICKET PROTECTION CALCULATOR")
    print("*"*50)
    print("Welcome! This system provides calculation of protection fees")
    print("for event ticket bookings")
    print("*"*50)

    #Repetition : Main program LOOP
    continue_program = True #Flag to control the main loop. 

    while continue_program:
        #Step 1 : Get customer information 
        #Composition : Calling get_customer_input() function 
        #Unpack returned tupel into individual variables for easier use :
        customer_name, event_type, num_tickets, ticket_price, customer_age = get_customer_input()

        #Step 2 : Calculate fees based on customer input
        #Composition : Calling calculate_fees() function and passing required parameters.
        #This function needs both input data and calculated fees 
        total_ticket_value, base_fee, protection_fee, high_value_surcharge, age_surcharge, total_fee = calculate_fees(num_tickets, ticket_price, customer_age)

        #Step 3: Display results to the user in clear format.
        #Composition : Calling display_results() function with customer data.
        display_results(customer_name, event_type, num_tickets, ticket_price, total_ticket_value, base_fee, protection_fee, high_value_surcharge, age_surcharge, total_fee)

        #Step 4 : Ask user if they want to calculate fee for another customer.
        continue_program = ask_continue() #This will update the flag based on user choice to continue or exit.

    #Display goodbye message when user chooses to exit the program.
    print("" + "*"*50)
    print("Thank you for using EventSureNZ Ticket Protection Calculator!")
    print("Goodbye!")
    print("*"*50)
main()



