from question2 import Vehicle, Car, ElectricCar

def test_car_fuel_type():
    c = Car()
    assert c.get_fuel_type() == "Petrol"
