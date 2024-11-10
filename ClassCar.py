class car:
    def __init__(self,make,model,year,fuel_level=100):
        self.make=make
        self.model=model
        self.year=year
        self.fuel_level=fuel_level
        self.engine_running=False

    def start_engine(self):
        if not self.engine_running:
            self.engine_running=True
            print(f"The {self.make} {self.model}`s engine is started")
        else:
            print(f"The {self.make} {self.model}`s already running")

    def drive(self,miles):
        if not self.engine_running:
            print("You need to started engine first!")
            return
        fuel_consumed=miles*0.5
        if fuel_consumed>self.fuel_level:
            print("Not enough fuel to drive that far!")
        else:
            self.fuel_level-=fuel_consumed
            print(f"Drove {miles} miles.Fuel level is now {self.fuel_level:.2f}.")

    def refuel(self,amount):
        self.fuel_level+=amount
        print(f"Added {amount} of units of fuel.Fuel level is now {self.fuel_level:.2f}")

    def get_fuel_level(self):
        return self.fuel_level

    def get_car_info(self):
        print(f"Get car info: {self.make} {self.model} {self.year}.")

    def stop_engine(self):
        if self.engine_running:
            self.engine_running=False
            print(f"The {self.make} {self.model} engine has been stopped.")
        else:
            print(f"The {self.make} {self.model} engine already off.")

My_car=car("marcedeez","Toyota",2020)
My_car.get_car_info()
My_car.start_engine()
My_car.drive(50)
My_car.refuel(20)
print(My_car.fuel_level)
print(My_car.get_fuel_level())
My_car.stop_engine()



