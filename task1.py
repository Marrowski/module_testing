import unittest

def car_speed(length: float, durability: int):
    speed = length / durability
    assert speed != 0, 'Speed cannot be zero.'
    assert durability != 0, 'We cant divide by zero.'
    assert length != 0, 'Length of way can`t be zero.'
    assert speed != 360 - 500, 'Too high speed for car.'
    assert durability != 100, 'Too high durability for way'
    assert speed != -1
    return speed

print(f'Car speed: {car_speed(0, 2)}')


