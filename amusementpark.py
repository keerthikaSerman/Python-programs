from math import ceil
class VisitorQueue:
    def __init__(self):
        self.visitors = []

    def enqueue(self, name):
        self.visitors.append(name)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.visitors.pop(0)

    def is_empty(self):
        return len(self.visitors) == 0

    def size(self):
        return len(self.visitors)

    def display(self):
        if self.is_empty():
            print("No visitors are waiting.")
        else:
            for i, name in enumerate(self.visitors, start=1):
                print(f"{i}. {name}")
class RideHistory:
    def __init__(self):
        self.history = []

    def push(self, record):
        self.history.append(record)

    def pop(self):
        if not self.history:
            print("No ride history to remove.")
            return
        print("Removed history:", self.history.pop())

    def display(self):
        if not self.history:
            print("No completed rides yet.")
            return

        print("\nRecent completed rides (latest first):")
        for record in reversed(self.history):
            print(record)

class Ride:
    def __init__(self, name, duration, capacity):
        self.name = name
        self.duration = duration
        self.capacity = capacity
        self.queue = VisitorQueue()

    def estimated_wait(self, group_size=1):
        people_waiting = self.queue.size()

        if people_waiting == 0:
            return 0

        cycles_before_group = (people_waiting + self.capacity - 1) // self.capacity

        return cycles_before_group * self.duration
    

class RideNode:
    def __init__(self, ride):
        self.ride = ride
        self.next = None


class RideLinkedList:
    def __init__(self):
        self.head = None

    def add_ride(self, ride):
        new_node = RideNode(ride)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

    def find_ride(self, name):
        current = self.head

        while current is not None:
            if current.ride.name.lower() == name.lower():
                return current.ride
            current = current.next

        return None

    def display_rides(self):
        current = self.head

        print("\n========== PARK RIDES ==========")
        while current is not None:
            ride = current.ride
            print(
                f"{ride.name} | Cycle: {ride.duration} min"
                f" | Capacity: {ride.capacity}"
                f" | Waiting: {ride.queue.size()}"
            )
            current = current.next

park = RideLinkedList()
history = RideHistory()

park.add_ride(Ride("Roller Coaster", 3, 10))
park.add_ride(Ride("Ferris Wheel", 5, 8))
park.add_ride(Ride("Water Ride", 4, 6))
park.add_ride(Ride("Fun House", 2, 5))


def get_ride():
    name = input("Enter ride name: ").strip()
    ride = park.find_ride(name)

    if ride is None:
        print("Ride not found. Check the ride name.")
    return ride


def join_queue():
    ride = get_ride()

    if ride is None:
        return

    try:
        group_size = int(
            input("How many people are in your group? ")
        )

        if group_size <= 0:
            print("Group size must be at least 1.")
            return

    except ValueError:
        print("Please enter a valid whole number.")
        return

    names = []

    for i in range(group_size):
        name = input(
            f"Enter name of visitor {i + 1}: "
        ).strip()

        if not name:
            print("Name cannot be empty. Registration cancelled.")
            return

        names.append(name)

    wait = ride.estimated_wait(group_size)

    
    for name in names:
        ride.queue.enqueue(name)

    print("\n========== REGISTRATION SUCCESSFUL ==========")
    print(f"Ride: {ride.name}")
    print(f"Group size: {group_size}")
    print(f"Estimated waiting time: {wait} minutes")

    if wait == 0:
        print("You can proceed to the boarding area.")
    else:
        print(f"Please return in approximately {wait} minutes.")

    print("Enjoy your amusement park visit!")


def show_queue():
    ride = get_ride()
    if ride is not None:
        print(f"\nQueue for {ride.name}:")
        ride.queue.display()


def serve_visitor():
    ride = get_ride()
    if ride is None:
        return

    visitor = ride.queue.dequeue()

    if visitor is None:
        print("The queue is empty.")
    else:
        record = f"{visitor} - {ride.name}"
        history.push(record)
        print(f"{visitor} is now boarding {ride.name}.")


def show_wait():
    ride = get_ride()
    if ride is not None:
        wait = ride.estimated_wait()
        print(f"Current people waiting: {ride.queue.size()}")
        print(
            f"Estimated wait for a new visitor: "
            f"{wait} minutes"
        )


def main():
    while True:
        print("\n================================")
        print(" SMART AMUSEMENT PARK SYSTEM")
        print("================================")
        print("1. View all rides")
        print("2. Join a ride queue")
        print("3. View a ride queue")
        print("4. Estimate waiting time")
        print("5. Serve next visitor")
        print("6. View completed ride history")
        print("7. Remove latest history entry")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            park.display_rides()
        elif choice == "2":
            join_queue()
        elif choice == "3":
            show_queue()
        elif choice == "4":
            show_wait()
        elif choice == "5":
            serve_visitor()
        elif choice == "6":
            history.display()
        elif choice == "7":
            history.pop()
        elif choice == "8":
            print("Thank you for using Smart Amusement Park!")
            break
        else:
            print("Invalid choice. Please enter 1 to 8.")


if __name__ == "__main__":
    main()
