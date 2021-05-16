class GlobalNetworkParameters(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class HomeNetworkParameters(metaclass=GlobalNetworkParameters):
    pass


def main():
    home1 = HomeNetworkParameters()
    home2 = HomeNetworkParameters()
    assert home1 is home2


if __name__ == "__main__":
    main()
