class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  
        self.rear = None  

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = Node(data)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print(f"Car '{data}' has been parked successfully. (Enqueued)")

    def dequeue(self):
        if self.is_empty():
            print("Parking is empty! No cars to move.")
            return None
        data = self.front.data
        self.front = self.front.next
        if self.front is None:
            self.rear = None
        print(f"Car '{data}' has moved from the parking. (Dequeued)")
        return data

    def peek(self):
        if self.is_empty():
            print("Parking is empty.")
            return None
        print(f"Next car to move: {self.front.data}")
        return self.front.data

    def size(self):
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        print(f"Total cars currently parked: {count}")
        return count

    def display(self):
        if self.is_empty():
            print("Queue elements: Parking lot is currently empty.")
            return
       
        current = self.front
        cars = []
        while current:
            cars.append(current.data)
            current = current.next
        print("Queue elements:",",".join(cars))

if __name__ == "__main__":
    parking_queue = Queue()
    while True:
        print("\n--- Car Parking System Menu ---")
        print("1. Park a Car")
        print("2. Move Car from Parking")
        print("3. View Next Car to Move")
        print("4. Display Parked Cars")
        print("5. Show Total Parked Cars")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            car_no = input("Enter Car Number:")
            if car_no:
                parking_queue.enqueue(car_no)
            else:
                print("Car number cannot be empty!")
            parking_queue.display()
        elif choice == '2':
            parking_queue.dequeue()
            parking_queue.display()
        elif choice == '3':
            parking_queue.peek()
            parking_queue.display()
        elif choice == '4':
            parking_queue.display()
        elif choice == '5':
            parking_queue.size()
            display()
        elif choice == '6':
            print("Exiting Car Parking System. Goodbye!")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 6.")

