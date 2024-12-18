tickets = {}
ticket_id = 1

def book_ticket():
    global ticket_id
    name = input("Enter passenger name: ")
    flight = input("Enter flight number: ")
    destination = input("Enter destination: ")
    tickets[ticket_id] = {
        'Name': name,
        'Flight': flight,
        'Destination': destination
    }
    print(f"Ticket booked successfully! Ticket ID: {ticket_id}")
    ticket_id += 1

def display_ticket():
    tid = int(input("Enter Ticket ID: "))
    if tid in tickets:
        print("\nTicket Details:")
        for key, value in tickets[tid].items():
            print(f"{key}: {value}")
    else:
        print("Invalid Ticket ID!")

def cancel_ticket():
    tid = int(input("Enter Ticket ID to cancel: "))
    if tid in tickets:
        del tickets[tid]
        print("Ticket canceled successfully!")
    else:
        print("Invalid Ticket ID!")

def display_all_tickets():
    if tickets:
        print("\nAll Tickets:")
        for tid, details in tickets.items():
            print(f"\nTicket ID: {tid}")
            for key, value in details.items():
                print(f"{key}: {value}")
    else:
        print("No tickets available.")

def main():
    while True:
        print("\nSimple Ticket Management System")
        print("1. Book Ticket")
        print("2. Display Ticket")
        print("3. Cancel Ticket")
        print("4. Display All Tickets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_ticket()
        elif choice == '2':
            display_ticket()
        elif choice == '3':
            cancel_ticket()
        elif choice == '4':
            display_all_tickets()
        elif choice == '5':
            break
        else:
            print("Invalid choice! Try again.")

main()