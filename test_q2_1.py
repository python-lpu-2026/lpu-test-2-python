from question2 import Vehicle, Car, ElectricCar

def test_vehicle_base_class():
    v = Vehicle()
    assert v.get_fuel_type() == "Unknown"

