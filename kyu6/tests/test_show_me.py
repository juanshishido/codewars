import unittest

from kyu6.show_me import show_me


class TestShowMe(unittest.TestCase):

    def test_Vehicle(self):
        class Vehicle:
            def __init__(self, seats, wheels, engine):
                self.seats = seats
                self.wheels = wheels
                self.engine = engine
        porsche = Vehicle(2, 4, 'Gas')
        answer = ("Hi, I'm one of those Vehicles! "
                  "Have a look at my engine, seats and wheels.")
        self.assertEquals(answer, show_me(porsche))

    def test_Planet(self):
        class Planet:
            def __init__(self, moon):
                self.moon = moon
        earth = Planet('moon')
        answer = "Hi, I'm one of those Planets! Have a look at my moon."
        self.assertEquals(answer, show_me(earth))
