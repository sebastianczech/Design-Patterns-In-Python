import copy


class Prototype:
    def __init__(self, name):
        self.name = name

    def __str__(self) -> str:
        return "class: " + str(self.__class__) + ", hash: " + str(self.__hash__())


class PrototypeFactory:
    @staticmethod
    def get_prototype_clone(object_2_clone):
        return copy.deepcopy(object_2_clone)


def main():
    prototype = Prototype("test")
    print(prototype)

    factory = PrototypeFactory()
    prototype_copy = factory.get_prototype_clone(prototype)
    print(prototype_copy)


if __name__ == "__main__":
    main()
