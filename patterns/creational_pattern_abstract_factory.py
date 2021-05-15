import abc


class AbstractFactory(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create_port(self):
        pass

    @abc.abstractmethod
    def create_chassis(self):
        pass


class FactoryCisco(AbstractFactory):
    def create_port(self):
        return PortCisco()

    def create_chassis(self):
        return ChassisCisco()


class FactoryJuniper(AbstractFactory):
    def create_port(self):
        return PortJuniper()

    def create_chassis(self):
        return ChassisJuniper()


class AbstractPort(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info(self):
        pass


class PortCisco(AbstractPort):
    def info(self):
        return "Port Cisco"


class PortJuniper(AbstractPort):
    def info(self):
        return "Port Juniper"


class AbstractChassis(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def info(self):
        pass


class ChassisCisco(AbstractChassis):
    def info(self):
        return "Chassis Cisco"


class ChassisJuniper(AbstractChassis):
    def info(self):
        return "Chassis Juniper"


def main():
    cisco_factory = FactoryCisco()
    cisco_port = cisco_factory.create_port()
    cisco_chassis = cisco_factory.create_chassis()

    print(cisco_port.info())
    print(cisco_chassis.info())


if __name__ == "__main__":
    main()
