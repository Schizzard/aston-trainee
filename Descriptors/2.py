# flake8: noqa

class Rubles:
    def __get__(self, instance, owner):
        return instance.__dict__['rubles']
    def __set__(self, instance, value):
        if value is not None:
            instance.__dict__['rubles'] = value

class Dollars:
    def __get__(self, instance, owner):
        return round(instance.rubles / instance.EXCH, 2)
    def __set__(self, instance, value):
        if value is not None:
            instance.__dict__['rubles'] = round(value * instance.EXCH, 2)


class Salary:
    EXCH = 65
    rubles = Rubles()
    dollars = Dollars()
    def __init__(self, rubles=None, dollars=None):
        self.rubles = rubles
        self.dollars = dollars


sal1 = Salary(rubles=35000)
sal2 = Salary(dollars=10)
pass
