import abc


class NetworkPacket(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_structure(self):
        pass


class NetworkPacketDecorator(NetworkPacket, metaclass=abc.ABCMeta):
    def __init__(self, network_packet):
        self.network_packet = network_packet

    def get_structure(self):
        pass


class EthernetPacket(NetworkPacket):
    def get_structure(self):
        return "[ethernet]"


class IpPacket(NetworkPacketDecorator):
    def get_structure(self):
        return self.network_packet.get_structure() + "[ip]"


class TcpPacket(NetworkPacketDecorator):
    def get_structure(self):
        return self.network_packet.get_structure() + "[tcp]"


class HttpPacket(NetworkPacketDecorator):
    def get_structure(self):
        return self.network_packet.get_structure() + "[http]"


def main():
    ethernet_packet = EthernetPacket()
    ip_packet = IpPacket(ethernet_packet)
    tcp_packet = TcpPacket(ip_packet)
    http_packet = HttpPacket(tcp_packet)
    print(http_packet.get_structure())


if __name__ == "__main__":
    main()
