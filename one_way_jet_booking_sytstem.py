# Asks the user for their flight type choice
flight_choice = str(input("Welcome to the One Way Jet Booking System! "
                          + "What type of flight would you like to book? (Domestic/International): ")).lower()

if flight_choice == "domestic":  # Domestic flight booking process
    print("\nBelow are the available domestic flights:\n")

    # Domestic flight options list
    domestic_flight_list = [
        "Monterey Regional Airport to Sacramento International Airport",
        "Monterey Regional Airport to San Francisco International Airport"
    ]
    print("1. " + domestic_flight_list[0])
    print("2. " + domestic_flight_list[1])

    flight_choice = int(
        input("\nPlease choose your flight from the options above (1, 2):\n"))

    domestic_flight_list = domestic_flight_list[flight_choice - 1]

    # Asks the user how many passengers they are booking for, maximum of 7 passengers per booking
    num_passengers = int(input(
        "\nHow many passengers will be flying? Maximum of 7 passengers per booking: "))
    if num_passengers < 1 or num_passengers > 7:
        print("Please enter a valid number of passengers currently, you can only book for 1-7 passengers at a time.")
        num_passengers = int(input("\nHow many passengers will be flying? "))

    print(
        f"\nYou have indicated that {num_passengers} passenger(s) will be flying.")

    # Asks the user their preferred departure date in MM/DD/YYYY format
    valid_date = False # Flag to track if a valid date has been entered
    
    while not valid_date:
        departure_date = input(
            "\nPlease enter your preferred departure date (MM/DD/YYYY): ")

        parts = departure_date.split("/")

        month, day, year = parts # Split the date into month, day, and year
        month_int = int(month)
        day_int = int(day)
        year_int = int(year)

        if len(parts) != 3 or not all(part.isdigit() for part in parts): # Basic format check for MM/DD/YYYY
            print(
                "\nInvalid date format. Please enter the date in MM/DD/YYYY format. ")
            continue
        if month_int < 1 or month_int > 12: # Month must be between 1 and 12
            input("\nInvalid month. Please enter a valid month (1-12). ")
            continue
        if day_int < 1 or day_int > 31: # Day must be between 1 and 31
            input("\nInvalid day. Please enter a valid day (1-31). ")
            continue
        if len(year) != 4 or not year.isdigit(): # Year must be 4 digits
            input("\nInvalid year. Please enter a valid year (4 digits). ")
            continue
        if month_int == 2 and day_int > 29: # February check for 28 days noninclusive
            input("\nFebruary cannot have more than 29 days. Please enter a valid date. ")
            continue
        if month_int in [4, 6, 9, 11] and day_int > 30: # Months with 30 days
            input(
                "\nThe selected month cannot have more than 30 days. Please enter a valid date. ")
            continue
        if year_int < 2026: # Year validation to prevent past dates
            input(
                "\nThe year cannot be in the past. Please enter a valid year (2026 or later). ")
            continue
        
        valid_date = True # A valid date has been entered if all checks are passed

        print(
            f"\nYou have selected a departure date of {month_int:02d}/{day_int:02d}/{year}.")

    if flight_choice == 1:  # Departure times for MRY to SMF
        print("\nWhat is your preferred departure time for your flight?")
        print("Departure time options:\n"
              "6:30 am\n"
              "12:00 pm\n"
              "5:30 pm\n")

        departure_times = ["6:30 am", "12:00 pm", "5:30 pm"]

        departure_time_choice = input(
            "Enter your preferred departure time from the list: ").lower()

        if departure_time_choice in departure_times:
            selected_departure_time = departure_time_choice
            print(
                f"\nYou have selected a departure time of {selected_departure_time}.")
        elif departure_time_choice not in departure_times:
            selected_departure_time = input(
                "\nWe don't have that departure time. Please enter a time from the departure list. ")
            print(
                f"\nYou have selected a departure time of {selected_departure_time}.")

    elif flight_choice == 2:  # Departure times for MRY to SFO
        print("\nWhat is your preffered departure time for your flight?")
        print("Departure time options:\n"
              "4:00 am\n"
              "9:30 am\n"
              "3:00 pm\n"
              "8:30 pm\n")

        departure_times = ["4:00 am", "9:30 am", "3:00 pm", "8:30 pm"]

        departure_time_choice = input(
            "Enter your preferred departure time from the list: ").lower()

        if departure_time_choice in departure_times:
            selected_departure_time = departure_time_choice
            print(
                f"\nYou have selected a departure time of {selected_departure_time}.")
        elif departure_time_choice not in departure_times:
            selected_departure_time = input(
                "\nWe don't have that departure time. Please enter a time from the departure list. ")
            print(
                f"\nYou have selected a departure time of {selected_departure_time}.")

    # Ask the user what cabin class they would like to book
    # Varies based on flight choice
    print("\nWhat cabin class would you like to book?")
    if flight_choice == 1:
        print(f"\nAvailable cabin classes for the MRY to SMF flight on {departure_date} at {selected_departure_time}: "
              + "\nEconomy $215"
              + "\n     22 lbs carry-on bag"
              + "\n     30 inches of legroom"
              + "\nBusiness $277"
              + "\n     33 lbs carry-on bag"
              + "\n     50 lbs checked bag"
              + "\n     35 inches of legroom"
              + "\n     Complimentary snack and drink service"
              + "\n     Priority boarding")
        economy = 215  # Economy ticket price for MRY to SMF
        business = 277  # Business ticket price for MRY to SMF
    elif flight_choice == 2:
        print(f"Available cabin classes for the MRY to SFO flight on {departure_date} at {selected_departure_time}: "
              + "\nEconomy $173"
              + "\n     22 lbs carry-on bag"
              + "\n     30 inches of legroom"
              + "\nBusiness $223"
              + "\n     33 lbs carry-on bag"
              + "\n     50 lbs checked bag"
              + "\n     35 inches of legroom"
              + "\n     Complimentary snack and drink service"
              + "\n     Priority boarding")
        economy = 173  # Economy ticket price for MRY to SFO
        business = 223  # Business ticket price for MRY to SFO

    # Cabin class selection process
    cabin_classes = ["Economy", "Business"]

    cabin_class_choice = input(
        "\nEnter your preferred cabin class from the available options: ").lower().capitalize()

    if cabin_class_choice in cabin_classes:
        selected_cabin_class = cabin_class_choice
        print(f"\nYou have selected {selected_cabin_class} class.")
    elif cabin_class_choice not in cabin_classes:
        input("\n Invalid choice. Please enter a valid cabin class from the list. ")

    # Asks the user to input passenger details
    passenger_details = []  # Store passenger details

    for i in range(num_passengers):
        print(f"\nPlease enter the details for passenger {i+1}:")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        passenger_details.append(
            {"First Name": first_name, "Last Name": last_name})

    print("\nYou have entered the following passenger details:")
    for i, passenger in enumerate(passenger_details):
        print("Passenger " + str(i+1) + ": " +
              passenger["First Name"] + " " + passenger["Last Name"])

    # Seat selection process
    economy_seats_available = 20  # total number of economy seats available
    business_seats_available = 10  # total number of business seats available
    economy_cabin = cabin_class_choice == "Economy"
    business_cabin = cabin_class_choice == "Business"

    booked_seats = []  # List to keep track of booked seats

    if selected_cabin_class == "Economy":
        economy_cabin_layout = ["E", "F", "G", "H", "I"]
        seats_per_row = 4
        print(f"\nFor an additional $25 you can select a seat, if not say \"skip\" and no seat will be selected. "
              + f"\nAvailable seats in {selected_cabin_class} class:\n")
        for row in economy_cabin_layout:
            for seat in range(1, seats_per_row + 1):
                print(row + str(seat), end=" ")
            print()
        for i in range(num_passengers):
            while True:
                seat_choice = input(
                    f"\nSelect seat for {passenger_details[i]['First Name']} {passenger_details[i]['Last Name']} or type 'skip': ").upper()
                if seat_choice == "SKIP":
                    print(
                        f"No seat selected for {passenger_details[i]['First Name']} {passenger_details[i]['Last Name']}.")
                    break
                elif seat_choice in booked_seats:
                    print("That seat is already taken. Choose another.")
                elif (seat_choice[0] in economy_cabin_layout and
                      seat_choice[1:].isdigit() and
                      1 <= int(seat_choice[1:]) <= seats_per_row):
                    booked_seats.append(seat_choice)
                    print(
                        f"Seat {seat_choice} booked for {passenger_details[i]['First Name']} {passenger_details[i]['Last Name']}.")
                    break
                else:
                    input("Invalid seat. Please select a valid seat. ")
            print(
                f"\nYou have booked the following seat(s): {', '.join(booked_seats)}")
    if selected_cabin_class == "Business":
        business_cabin_layout = ["A", "B", "C", "D"]
        seats_per_row = 4
        print(f"\nFor an additional $25 you can select a seat, if not say \"skip\" and no seat will be selected. "
              + f"\nAvailable seats in {selected_cabin_class} class:\n")
        for row in business_cabin_layout:
            for seat in range(1, seats_per_row + 1):
                print(row + str(seat), end=" ")
            print()
        for i in range(num_passengers):
            while True:
                seat_choice = input(
                    f"\nSelect seat for {passenger_details[i]['First Name']} {passenger_details[i]['Last Name']} or type 'skip': ").upper()
                if seat_choice == "SKIP":
                    print(
                        f"No seat selected for {passenger_details[i]['First Name']} {passenger_details[i]['Last Name']}.")
                    break
                elif seat_choice in booked_seats:
                    print("That seat is already taken. Choose another.")
                elif (seat_choice[0] in business_cabin_layout and
                      seat_choice[1:].isdigit() and
                      1 <= int(seat_choice[1:]) <= seats_per_row):
                    booked_seats.append(seat_choice)
                    print(
                        f"Seat {seat_choice} booked for {passenger_details[i]['First Name']} {passenger_details[i]['Last Name']}.")
                    break
                else:
                    input("Invalid seat. Please select a valid seat. ")
        print(
            f"\nYou have booked the following seat(s): {', '.join(booked_seats)}")

    # Asks the user if they would like to add extra baggage, food, drinks, wifi, or priority boarding
    passenger_services = {}
    extra_service_options = {
        "50 lbs checked baggage": 30,
        "In-flight Meal": 15,
        "In-flight Drink": 10,
        "WiFi Access": 12,
        "Priority Boarding": 20
    }
    # Displays available extra services
    for i, passengers in enumerate(passenger_details):
        passenger_name = f"{passengers['First Name']} {passengers['Last Name']}"
        print(
            f"\nAvailable extra services for {passengers['First Name']} {passengers['Last Name']}:")
        for idx, (service, price) in enumerate(extra_service_options.items(), start=1):
            print(f"{idx}. {service} - ${price}")
        add_ons = input(
            f"\nWhich services does {passenger_name} want? Enter numbers separated by commas (or 'none' to skip):\n")

        selected_add_ons = []
        if add_ons != 'none':
            selected_indices = [int(x.strip())
                                for x in add_ons.split(',') if x.strip().isdigit()]
            for index in selected_indices:
                if 1 <= index <= len(extra_service_options):
                    service = list(extra_service_options.keys())[index - 1]
                    selected_add_ons.append(service)
                    print(f"\n{service} added to {passenger_name}'s booking.")

        passenger_services[passenger_name] = selected_add_ons
        print(f"\nYou have selected the following extra services for {passenger_name}: " + ", ".join(
            selected_add_ons) if selected_add_ons else "No extra services selected.")

    # Calculate total fare cost for the booking
    if selected_cabin_class == "Economy":
        base_fare = economy
    elif selected_cabin_class == "Business":
        base_fare = business
    total_cost = base_fare * num_passengers
    for services in passenger_services.values():
        for service in services:
            total_cost += extra_service_options[service]
    if booked_seats:
        total_cost += 25 * len(booked_seats)
    print(f"\nThe total cost of your booking is: ${total_cost}")

    # Final booking details
    print("\nYour final booking details are as follows:\n")
    print("Your total fare is: $" + str(total_cost)
          + "\nFlight: " + domestic_flight_list
          + "\nDeparture Date: " + departure_date
          + "\nDeparture Time: " + selected_departure_time
          + "\nCabin Class: " + selected_cabin_class
          + "\nNumber of Passengers: " + str(num_passengers)
          + "\nPassenger Details")
    for i, passenger in enumerate(passenger_details):
        print(f"Passenger {i+1}: " +
              f"{passenger['First Name']} {passenger['Last Name']} (Seat: " + (booked_seats[i] if i < len(booked_seats) else "No seat selected") + ")")
    print("Extra Services")
    for passenger_name, services in passenger_services.items():
        print(f"{passenger_name}: " +
              (", ".join(services) if services else "No extra services selected"))

    import random  # Allows for random selection of letters

    # Asks the user to confirm their booking
    confirm_booking = input(
        "\nDo you want to confirm your booking? (yes/no): ").lower()
    if confirm_booking == "yes":  # Generates booking confirmation number
        used_codes = []  # Store codes to avoid duplicates
        letters_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        bookings = 1  # Only one booking confirmation number needed
        if bookings == 1:
            code = ""
            while code in used_codes or code == "":
                # 2 Letters
                letter1 = random.choice(letters_list)
                letter2 = random.choice(letters_list)

                # Generates 4 random numbers between 0 and 9999
                n = random.randint(0, 9999)
                numbers = str(n).zfill(4)

                # Combine letters and numbers
                code = letter1 + letter2 + numbers

            used_codes.append(code)
            print("\nBooking confirmation number:", code)
        print("\nThank you for booking with One Way Jet! Your booking has been confirmed. We look forward to flying with you.\n")
    elif confirm_booking == "no":
        print("\nBooking cancelled. Thank you for considering One Way Jet!\n")

else:
    print("Currently, we only support domestic flight bookings. Please check back later for international flight options.")
