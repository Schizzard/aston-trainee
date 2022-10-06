from typing import Dict, List, Set


class Employe(object):
    _interns: Dict[str, 'Employe'] = {}

    def __new__(cls, *args, **kwargs):
        name = '-'.join(args[:2])
        if name not in cls._interns:
            obj = object.__new__(cls)
            cls._interns[name] = obj
            return obj
        else:
            return cls._interns[name]

    def __init__(self, firstname, lastname, grade) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.grade = grade
        self.salary = 0
        self._skills: Set[str] = set()
        self.hiden_field1_accessed = 0

    @property
    def skills(self):
        return self._skills

    @skills.setter
    def skills(self, value):
        self._skills.add(value)

    @skills.deleter
    def skills(self, value):
        self._skills.discard(value)

    @property
    def fullname(self):
        return f'{self.firstname} {self.lastname}'

    @staticmethod
    def info():
        print("Employe('firstname', 'lastname', 'grade')")

    @classmethod
    def total_objects(cls):
        return len(cls._interns)

    def __del__(self):
        name = f'{self.firstname}-{self.lastname}'
        del self.__class__._interns[name]

    def __gt__(self, other):
        if isinstance(other, self.__class__):
            return self.grade > other.grade
        return NotImplementedError

    def __add__(self, other):
        if isinstance(other, self.__class__):
            return self.salary + other.salary
        elif isinstance(other, (int, float)):
            return self.salary + other

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return self.salary * other.salary
        elif isinstance(other, (int, float)):
            return self.salary * other

    def __repr__(self) -> str:
        return f"Intern('{self.firstname}', '{self.lastname}', '{self.grade}')"

    def __str__(self) -> str:
        return f"{self.fullname} ({self.grade})"

    def __getattr__(self, item):
        self.__dict__[item] = 500
        return 500

    def __getattribute__(self, item):
        if item.startswith('hiden'):
            raise AttributeError
        return object.__getattribute__(self, item)


class EmployeList:
    def __init__(self) -> None:
        self.data: List[Employe] = []

    def __iter__(self):
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index < len(self.data):
            x = self.data[self.current_index]
            self.current_index += 1
            return x
        raise StopIteration

    def __getitem__(self, index):
        return self.data[index]

    def add(self, emp: Employe):
        self.data.append(emp)

    def delete(self, emp):
        self.data.remove(emp)


class Department(object):
    def __init__(self, name) -> None:
        self.name = name
        self.count = 0
        self.employes = EmployeList()

    def __iter__(self):
        return iter(self.employes)

    def __len__(self):
        return len(self.employes)

    def add_emp(self, emp: Employe):
        self.count += 1
        self.employes.add(emp)

    def remove_emp(self, emp: Employe):
        self.count -= 1
        self.employes.delete(emp)

    def __call__(self):
        for emp in self.employes:
            print(f'{str(emp)} работает')


if __name__ == "__main__":
    # demo
    intern1 = Employe('Evgeniy', 'Korzunov', 'Intern')
    intern2 = Employe('Ivan', 'Ivanov', 'M2')
    intern3 = Employe('Evgeniy', 'Korzunov', 'Intern')
    print(intern1 == intern3)
    print(intern3 > intern2)
    print(intern3 < intern2)

    print(str(intern1))
    print(repr(intern1))

    intern1.skills = "python"
    intern1.salary = 30000
    intern2.salary = 200000
    print(intern1 + 5000)
    print(intern2.salary - 2000)

    dep = Department("Backend")
    dep.employes.add(intern1)
    dep.employes.add(intern2)
    dep()
