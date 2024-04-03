import datetime
import os

# In-memory storage for events
events = []

# Clears the  command line
def  clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    
def main_menu():
    # Display the menu for event calendar
    print("\nEvent Calendar")
    print("1. Add event")
    print("2. List events")
    print("3. Delent event")
    print("4. Search event")
    print("5. Edit event")
    print("6. Exit")
    choice = input("Enter choice from the above(1-6): ")
    clear()
    return choice
# Prompts user for event details and validates date and time.   
def get_event_details():
    title = input("Enter event title: ")
    description = input("Enter event description: ")
    while True:
        date = input("Enter event date (YYYY-MM-DD): ")
        if is_valid_date(date):
            break
    else:
        print("Invalid date format. Please use YYYY-MM-DD.")
    while True:
        time = input("Enter event time (HH:MM): ")
        if is_valid_time(time):
            break
        else:
            print("Invalid time format. Please use HH:MM.")
    return title, description, date, time 

# Checks if the date string is in YYYY-MM-DD format.
def is_valid_date(date_str):
    try:
        datetime.datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False

# Checks if the time string is in HH:MM format.
def is_valid_time(time_str):
    try:
        datetime.datetime.strptime(time_str, '%H:%M')
        return True
    except ValueError:
        return False

# Function to add a new event
def add_event(title, description, date, time):
    try:
        # Validate date and time format
        datetime.datetime.strptime(date, '%Y-%m-%d')
        datetime.datetime.strptime(time, '%H:%M')
    except ValueError:
        print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
        return
    
    events.append({
        'title': title,
        'description': description,
        'date': date,
        'time': time
    })
    print("Event added successfully!")

# Function to display all events sorted by date and time
def list_events():
    if not events:
        print("No events found.")
        return
    
    sorted_events = sorted(events, key=lambda x: (x['date'], x['time']))
    for event in sorted_events:
        print(f"Title: {event['title']}")
        print(f"Description: {event['description']}")
        print(f"Date: {event['date']}")
        print(f"Time: {event['time']}")
        print()

# Function to delete an event by title
def delete_event(title):
    global events
    updated_events = [event for event in events if event['title'] != title]
    if len(updated_events) == len(events):
        print("Event not found.")
    else:
        events = updated_events
        print("Event deleted successfully!")

# Function to search events by date or keyword
def search_events(keyword):
    found_events = [event for event in events if keyword in event['title'] or keyword in event['description'] or keyword == event['date']]
    if not found_events:
        print("No events found.")
        return
    
    for event in found_events:
        print(f"Title: {event['title']}")
        print(f"Description: {event['description']}")
        print(f"Date: {event['date']}")
        print(f"Time: {event['time']}")
        print()

# Function to edit an existing event
def edit_event(title, new_title=None, new_description=None, new_date=None, new_time=None):
    for event in events:
        if event['title'] == title:
            if new_title:
                event['title'] = new_title
            if new_description:
                event['description'] = new_description
            if new_date:
                event['date'] = new_date
            if new_time:
                event['time'] = new_time
            print("Event edited successfully!")
            return
    print("Event not found.")

# Sample unit tests
def test_event_creation():
    add_event("Meeting", "Team meeting", "2024-04-02", "10:00")
    assert len(events) == 1

def test_event_deletion():
    delete_event("Meeting")
    assert len(events) == 0

while True:
    choice = main_menu()
    if choice == '1':
        title, description, date, time = get_event_details()
        add_event(title, description, date, time)
    elif choice == '2':
        list_events()
    elif choice == '3':
        title = input("Enter event title to delete: ")
        delete_event(title)
    elif choice == '4':
        keyword = input("Enter keyword to search (title, description, or date): ")
        search_events(keyword)
    elif choice == '5':
        title = input("Enter event title to edit: ")
        new_title = input("Enter new title (or leave blank to keep existing): ")
        new_description = input("Enter new description (or leave blank to keep existing): ")
        new_date = input("Enter new date (YYYY-MM-DD) (or leave blank to keep existing): ")
        new_time = input("Enter new time (HH:MM) (or leave blank to keep existing): ")
        edit_event(title, new_title, new_description, new_date, new_time)
    elif choice == '6':
        print("Exiting Event Calendar.")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")