import abc


class VlanEncapsulation(metaclass=abc.ABCMeta):
    def __init__(self, name):
        self.name = name

    @abc.abstractmethod
    def get_encapsulation_name(self):
        pass


class Dot1qEncapsulation(VlanEncapsulation):
    def get_encapsulation_name(self):
        return self.name


class NoEncapsulation(VlanEncapsulation):
    def get_encapsulation_name(self):
        return self.name


class VlanEncapsulationData():
    def prepare_encapsulation(self, encap):
        if encap == "dot1q":
            return Dot1qEncapsulation("dot1q")
        return NoEncapsulation("")


def main():
    vlanEncap = VlanEncapsulationData()
    print(vlanEncap.prepare_encapsulation("dot1q").get_encapsulation_name())


if __name__ == "__main__":
    main()
