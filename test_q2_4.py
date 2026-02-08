from question2 import Vehicle, Car, ElectricCar

def test_electric_car_fuel_type():
    e = ElectricCar()
    assert e.get_fuel_type() == "Electric"
