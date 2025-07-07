class Car:
    def __init__(self, carid : int, brand: str,  model : str, price_per_day: float, avaliable: bool):
        self.carid = carid
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.avaliable = avaliable

    def __str__(self):
        status  = "Avaliable"  if self.avaliable else "Rented"
        return f"{self.carid}: {self.brand} {self.model} - {status}"

class Customer:
    def __init__(self, name: str, car: Car, days: int):
        self.name = name
        self.car = car
        self.days = days
        self.returned = False

    def __str__(self):
        status = "Returned" if self.returned else "Rented"
        return f"{self.name} rented {self.car.brand} {self.car.model} for {self.days} day(s) - {status}"


class Rental_Service:
    def __init__(self):
        self.cars = []
        self.customers = []

    def add_cars(self, car: Car):
        self.cars.append(car)

    def display_avaliable_cars(self):
        print("\n Avaliable Cars: ")
        avaliable = False
        for car in self.cars:
            if car.avaliable:
                print(car)
                avaliable = True
            if not avaliable:
                print("No Cars Avaliable")

    
    def rent_car(self,carid : int):
        for car in self.cars:
            if car.carid == carid and car.avaliable:
                try:
                    name = input("Enter your name: ").strip()
                    days = int(input(f"\n Enter the Amount of Days You are Renting: {car.brand} {car.model}: "))
                    if days <= 0:
                        print("Number of Days Should be Atleast One")
                        return
                    total_cost = days * car.price_per_day
                    car.avaliable = False
                    customer = Customer(name, car, days)
                    self.customers.append(customer)
                    print(f"\n You have just Rented {car.brand} {car.model} for {days} day(s).")
                    print(f"\n Total Cost is {total_cost} Rupees.")
                    return 
                except ValueError:
                    print("Invalid Number of Days")
                    return
        print("\n Car is not Avaliable")


    def return_car(self,carid: int):
        for car in self.cars:
            if car.carid == carid and not car.avaliable:
                car.avaliable = True
                for customer in self.customers:
                    if customer.car.carid ==  carid and not customer.returned:
                        customer.returned = True
                print(f"\n You have Successfully Return {car.brand} {car.model}")
                return
            else:
                print("\n Invalid Return")


    def show_rentals(self):
        print("\n Customer Rentals: ")
        if not self.customers:
            print("No Rentals Yet")
            return
        for cust in self.customers:
            print(cust)



service  = Rental_Service()

car_list = [
    (1, "Toyota", "Corolla", 3000),
    (2, "Honda", "Civic", 3200),
    (3, "Ford", "Mustang", 5000),
    (4, "Hyundai", "Creta", 2800),
    (5, "Kia", "Seltos", 2900),
    (6, "BMW", "X5", 7000),
    (7, "Audi", "A4", 6800),
    (8, "Mercedes", "C-Class", 7200),
    (9, "Tesla", "Model 3", 7500),
    (10, "Volkswagen", "Polo", 2500),
    (11, "Nissan", "Magnite", 2600),
    (12, "Renault", "Kwid", 2000),
    (13, "Skoda", "Kushaq", 2700),
    (14, "MG", "Hector", 3100),
    (15, "Mahindra", "XUV700", 3300)
]

for car_id, brand, model, price in car_list:
    service.add_cars(Car(car_id, brand, model, price, True))




while True:
    print("\n ===== Car Rental Service =====")
    print("1. Show Avaliable Cars")
    print("2. Rent a Car")
    print("3. Return a Car")
    print("4. Exit")
    print("5. Show all Rentals")


    choice = int(input("\n Please Enter An Option from 1 to 5  "))

    if choice == 1:
        service.display_avaliable_cars()

    elif choice == 2:
        try:
            car_id = int(input("Enter the ID of the Car you want to Rent: "))
            service.rent_car(car_id)
        except ValueError:
                print("Invalid input. Please Enter Correct ID")

    elif choice == 3:
        try:
            car_id = int(input("Enter the ID of the Car you want to Return: "))
            service.return_car(car_id)
        except ValueError:
            print("Invalid Input. Pleaser Enter Correct ID")
    

    elif choice == 4:
        break

    elif choice == 5:
        service.show_rentals()

    else:
        print("Invalid Input")
