# Classes
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Male(Human):
    def __init__(self, name, age, sport):
        super().__init__(name, age)
        self.sport = sport


class Female(Human):
    def __init__(self, name, age, pregnant):
        super().__init__(name, age)
        self.pregnant = pregnant


pam = Female("pam", 32, False)
rafa = Male("rafa", 35, "box")
print("TYPE OF PAM: ", type(pam))
print("PAM IS MALE: ", pam is Male)
print("PAM IS HUMAN: ", issubclass(type(pam), Human))
print("TYPE OF RAFA: ", type(rafa))
print("RAFA IS HUMAN: ", isinstance(rafa, Human))


