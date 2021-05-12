import abc


class RoutingProtocol(metaclass=abc.ABCMeta):
    def __init__(self):
        self.name = None

    def protocol_name(self):
        return self.name


class BgpRoutingProtocol(RoutingProtocol):
    def __init__(self):
        super().__init__()
        self.name = "BGP"


class OspfRoutingProtocol(RoutingProtocol):
    def __init__(self):
        super().__init__()
        self.name = "OSPF"


class Router(metaclass=abc.ABCMeta):
    def __init__(self):
        self.routing_protocol = self._factory_method()

    @abc.abstractmethod
    def _factory_method(self):
        pass


class CiscoRouter(Router):
    def _factory_method(self):
        return BgpRoutingProtocol()


class JuniperRouter(Router):
    def _factory_method(self):
        return OspfRoutingProtocol()


def main():
    router = CiscoRouter()
    print(router.routing_protocol.protocol_name())


if __name__ == "__main__":
    main()
