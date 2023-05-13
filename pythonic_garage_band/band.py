class Musician:  # Super Class
    def __init__(self, name, instrument):
        self.name = name
        self.instrument = instrument

    def get_instrument(self):
        return self.instrument

    def play_solo(self):
        if self.get_instrument() == "guitar":
            return "face melting guitar solo"
        elif self.get_instrument() == "bass":
            return "bom bom buh bom"
        elif self.get_instrument() == "drums":
            return "rattle boom crash"


class Band:
    instances = []

    def __init__(self, name, members):
        self.name = name
        self.members = members
        Band.instances.append(self)

    def add_member(self, member):
        self.members.append(member)
        print(f"{member.name} added")

    def play_solos(self):
        solos = []
        for member in self.members:
            solos.append(member.play_solo())
        return solos

    @classmethod
    def to_list(cls):
        return cls.instances


class Guitarist(Musician):  # child
    def __init__(self, name):
        super().__init__(name, "guitar")

    def __str__(self):
        return f"My name is {self.name} and I play guitar"

    def __repr__(self):
        return f"Guitarist instance. Name = {self.name}"


class Bassist(Musician):  # child
    def __init__(self, name):
        super().__init__(name, "bass")

    def __str__(self):
        return f"My name is {self.name} and I play bass"

    def __repr__(self):
        return f"Bassist instance. Name = {self.name}"


class Drummer(Musician):  # child
    def __init__(self, name):
        super().__init__(name, "drums")

    def __str__(self):
        return f"My name is {self.name} and I play drums"

    def __repr__(self):
        return f"Drummer instance. Name = {self.name}"


if __name__ == "__main__":
    joan = Guitarist("Joan Jett")
    print(joan)
    print(joan.__repr__())
    sheila = Drummer("Sheila E.")
    print(sheila)
    print(sheila.__repr__())
    meshell = Bassist("Meshell Ndegeocello")
    print(meshell)
    print(meshell.__repr__())
    flea = Bassist("Flea")
    ginger = Drummer("Ginger Baker")

    nirvana = Band("Nirvana", [])
    nirvana.add_member(Guitarist("Kurt Cobain"))
    nirvana.add_member(Bassist("Krist Novoselic"))
    nirvana.add_member(Drummer("Dave Grohl"))
