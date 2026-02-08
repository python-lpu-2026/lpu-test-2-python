from question2 import Vehicle, Car, ElectricCar

def test_electric_car_is_vehicle():
    e = ElectricCar()
    assert isinstance(e, Vehicle)
