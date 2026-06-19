from vehicles import Car,Bike
from exceptions import Exception
ex = Exception()
from decorators import Decorators

print("\nWelcome to Ride Sharing System:\n")
while True:
    print("=="*40)
    print("1. Book a rider")
    print("2. Preview ride history")
    print("3. Clearing ride history")
    print("4. For exit")

    user_choice = int(input("\nEnter your choice: "))
    if user_choice == 1:
        d_name = input("Enter the name of rider: ").strip().title()
        v_type = input("Enter the type of vehicle you want to book (c for car, b for bike): ").strip().lower()
        distance = float(input("Enter the distance (in km): "))
        u_rating = float(input("Enter your rating: "))
        d = Decorators(u_rating)
        d.ride_logger
        if v_type[0] == "c":
            car = Car(d_name,"car",distance)
            car.print_details()
            data = f"\n\nRide Data:\nDriver Name: {d_name}\nVehicle Booked: Car\nDistance Travelled: {distance}\nRating Provided: {int(u_rating)}\nPrice: Rs.{car.calculate_fare()}"
            try:
                with open("ride_history.txt","a") as f:
                    f.write(data)
            except FileNotFoundError:
                ex.file_error()
        elif v_type[0] == "b":
            bike = Bike(d_name,"bike",distance)
            bike.print_details()
            data = f"\n\nRide Data:\nDriver Name: {d_name}\nVehicle Booked: Car\nDistance Travelled: {distance}\nRating Provided: {int(u_rating)}\nPrice: Rs.{bike.calculate_fare()}"
            try:
                with open("ride_history.txt","a") as f:
                    f.write(data)
            except FileNotFoundError:
                ex.file_error()
        else:
            ex.type_error()
    elif user_choice == 2:
        try:
            with open("ride_history.txt","r") as f:
                data = f.read()
                print(data)
        except FileNotFoundError:
            ex.file_error()
    elif user_choice == 3:
        try:
            with open("ride_history.txt","w") as f:
                f.write("")
                print("Successfully removed all the datas\n")
        except FileNotFoundError:
            ex.file_error()
    elif user_choice == 4:
        print("Exitting.....")
        break   
    else:
        ex.type_error()
        continue