import abc


class NetworkController:
    def __init__(self):
        self.port_configurator = None

    def prepare_port_configuration(self, port_configurator):
        self.port_configurator = port_configurator
        self.port_configurator.configure_encapsulation()
        self.port_configurator.configure_speed()


class PortConfigurator(metaclass=abc.ABCMeta):
    def __init__(self):
        self.port = Port()

    @abc.abstractmethod
    def configure_encapsulation(self):
        pass

    @abc.abstractmethod
    def configure_speed(self):
        pass


class PortConfiguratorNoEncap100Mb(PortConfigurator):
    def configure_encapsulation(self):
        self.port.encapsulation = "none"

    def configure_speed(self):
        self.port.speed = "100 Mbps"


class PortConfiguratorDot1qEncap1Gb(PortConfigurator):
    def configure_encapsulation(self):
        self.port.encapsulation = "dot1q"

    def configure_speed(self):
        self.port.speed = "1 Gbps"


class Port:
    def __init__(self):
        self.encapsulation = None
        self.speed = None

    def __str__(self):
        return "Port speed {} encapsulation {}".format(self.speed, self.encapsulation)


def main():
    port_conf_no_enc_100mb = PortConfiguratorNoEncap100Mb()
    network_controller = NetworkController()
    network_controller.prepare_port_configuration(port_conf_no_enc_100mb)
    port = port_conf_no_enc_100mb.port
    print(port)


if __name__ == "__main__":
    main()
