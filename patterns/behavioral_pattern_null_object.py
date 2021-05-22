import abc


class VlanEncapsulation(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def getEncapsulation(self):
        pass


class Dot1qEncapsulation(VlanEncapsulation):
    def __init__(self, name):
        self.name = name

    def getEncapsulation(self):
        return self.name


class NoEncapsulation(VlanEncapsulation):
    def __init__(self, name):
        self.name = name

    def getEncapsulation(self):
        return self.name


class VlanEncapsulationData():
    def getEncapsulation(self, encap):
        if encap == "dot1q":
            return Dot1qEncapsulation("dot1q")
        return NoEncapsulation("")


def main():
    vlanEncap = VlanEncapsulationData()
    print(vlanEncap.getEncapsulation("dot1q").getEncapsulation())


if __name__ == "__main__":
    main()
