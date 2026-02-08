from question2 import Vehicle, Car, ElectricCar

def test_car_inherits_vehicle():
    c = Car()
    assert isinstance(c, Vehicle)
